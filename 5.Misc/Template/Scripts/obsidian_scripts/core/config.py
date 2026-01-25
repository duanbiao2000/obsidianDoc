#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置管理模块

提供统一的配置加载和管理功能，支持：
- YAML 配置文件加载
- 环境变量覆盖
- 默认值管理
- 点号分隔的配置路径访问

作者: Claude Sonnet 4.5
创建时间: 2026-01-25
用途: Issue #4 - 自动化脚本体系优化
"""

import os
from pathlib import Path
from typing import Any, Dict, Optional, Union, List

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


class Config:
    """
    配置管理器

    从 YAML 文件加载配置，支持点号分隔的路径访问和环境变量覆盖。

    Attributes:
        config_path (Path): 配置文件路径
        _config (Dict): 配置数据字典

    Examples:
        >>> config = Config()
        >>> vault_root = config.get('vault_root')
        >>> include_dirs = config.get('scan.include_dirs')

        >>> # 使用默认值
        >>> verbose = config.get('output.verbose', False)

        >>> # 检查键是否存在
        >>> if config.has('encoding.utf8'):
        ...     print("UTF-8 编码已启用")
    """

    # 默认配置路径
    DEFAULT_CONFIG_PATH = Path(__file__).parent.parent.parent / 'config' / 'default.yaml'

    # 默认配置值（当配置文件不存在时使用）
    DEFAULT_CONFIG = {
        'vault_root': r"d:\迅雷下载\@同步文件\OneDrive\obsidianDoc",
        'scan': {
            'include_dirs': [
                "0.DailyNotes",
                "1.Projects",
                "2.Topics",
                "3.Resources",
                "4.Archives",
                "5.Misc",
                "6.Calendar",
                "Atlas"
            ],
            'exclude_patterns': [
                ".agent",
                ".git",
                ".obsidian",
                ".opencode",
                ".smart-env"
            ]
        },
        'backup': {
            'enabled': True,
            'directory': '.backup_enhance',
            'keep_days': 30
        },
        'encoding': {
            'utf8': True,
            'windows_compat': True
        },
        'output': {
            'verbose': False,
            'dry_run': False
        }
    }

    def __init__(self, config_path: Optional[Path] = None):
        """
        初始化配置管理器

        Args:
            config_path: 配置文件路径（默认使用 DEFAULT_CONFIG_PATH）
        """
        self.config_path = Path(config_path) if config_path else self.DEFAULT_CONFIG_PATH
        self._config: Dict[str, Any] = {}
        self.load()

    def load(self) -> None:
        """
        加载配置文件

        如果配置文件不存在或无法解析，使用默认配置。
        支持环境变量覆盖（格式：OBSIDIAN_<section>_<key>）。

        Examples:
            >>> config = Config()
            >>> config.load()  # 重新加载配置
        """
        # 首先加载默认配置
        self._config = self.DEFAULT_CONFIG.copy()

        # 如果配置文件存在，尝试加载
        if self.config_path.exists():
            try:
                if HAS_YAML:
                    with open(self.config_path, 'r', encoding='utf-8') as f:
                        file_config = yaml.safe_load(f)
                        if file_config:
                            self._merge_config(self._config, file_config)
                else:
                    print(f"警告: PyYAML 未安装，无法解析 {self.config_path}")
            except Exception as e:
                print(f"警告: 加载配置文件失败 ({self.config_path}): {e}")
                print("使用默认配置")

        # 应用环境变量覆盖
        self._apply_env_overrides()

    def _merge_config(self, base: Dict, override: Dict) -> None:
        """
        递归合并配置字典

        Args:
            base: 基础配置字典
            override: 覆盖配置字典
        """
        for key, value in override.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._merge_config(base[key], value)
            else:
                base[key] = value

    def _apply_env_overrides(self) -> None:
        """应用环境变量覆盖配置"""
        # 支持的环境变量格式：OBSIDIAN_<section>_<key>
        # 例如：OBSIDIAN_VAULT_ROOT, OBSIDIAN_OUTPUT_VERBOSE
        for key, value in os.environ.items():
            if key.startswith('OBSIDIAN_'):
                config_path = key[9:].lower().split('_')

                # 转换为嵌套字典结构
                current = self._config
                for part in config_path[:-1]:
                    if part not in current:
                        current[part] = {}
                    current = current[part]

                # 设置值（尝试转换为正确的类型）
                final_key = config_path[-1]
                current[final_key] = self._parse_env_value(value)

    def _parse_env_value(self, value: str) -> Any:
        """
        解析环境变量值，转换为正确的类型

        Args:
            value: 环境变量值（字符串）

        Returns:
            解析后的值（可能是 bool, int, 或 str）
        """
        # 布尔值
        if value.lower() in ('true', 'yes', '1'):
            return True
        if value.lower() in ('false', 'no', '0'):
            return False

        # 整数
        try:
            return int(value)
        except ValueError:
            pass

        # 字符串
        return value

    def get(self, key: str, default: Any = None) -> Any:
        """
        获取配置值（支持点号分隔的路径）

        Args:
            key: 配置键，支持点号分隔的路径（如 'scan.include_dirs'）
            default: 默认值（如果键不存在）

        Returns:
            配置值或默认值

        Examples:
            >>> config = Config()
            >>> vault = config.get('vault_root')
            >>> dirs = config.get('scan.include_dirs', [])
        """
        keys = key.split('.')
        value = self._config

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default

        return value if value is not None else default

    def has(self, key: str) -> bool:
        """
        检查配置键是否存在

        Args:
            key: 配置键，支持点号分隔的路径

        Returns:
            bool: 如果键存在返回 True

        Examples:
            >>> config = Config()
            >>> if config.has('backup.enabled'):
            ...     print("备份已启用")
        """
        return self.get(key) is not None

    @property
    def vault_root(self) -> Path:
        """获取 Vault 根目录"""
        return Path(self.get('vault_root'))

    @property
    def include_dirs(self) -> List[str]:
        """获取包含的目录列表"""
        return self.get('scan.include_dirs', [])

    @property
    def exclude_patterns(self) -> List[str]:
        """获取排除的模式列表"""
        return self.get('scan.exclude_patterns', [])

    @property
    def backup_enabled(self) -> bool:
        """检查备份是否启用"""
        return self.get('backup.enabled', True)

    @property
    def backup_dir(self) -> Path:
        """获取备份目录"""
        return Path(self.get('backup.directory', '.backup_enhance'))

    @property
    def verbose(self) -> bool:
        """检查是否启用详细输出"""
        return self.get('output.verbose', False)

    @property
    def dry_run(self) -> bool:
        """检查是否为预览模式"""
        return self.get('output.dry_run', False)

    def reload(self) -> None:
        """重新加载配置文件"""
        self.load()


if __name__ == "__main__":
    # 测试代码
    print("测试配置管理器...")

    config = Config()

    print(f"\n配置文件路径: {config.config_path}")
    print(f"配置文件存在: {config.config_path.exists()}")

    print("\n=== 配置值 ===")
    print(f"Vault 根目录: {config.vault_root}")
    print(f"包含目录: {config.include_dirs}")
    print(f"排除模式: {config.exclude_patterns}")
    print(f"备份启用: {config.backup_enabled}")
    print(f"备份目录: {config.backup_dir}")
    print(f"详细输出: {config.verbose}")
    print(f"预览模式: {config.dry_run}")

    print("\n=== 点号路径访问 ===")
    print(f"scan.include_dirs: {config.get('scan.include_dirs')}")
    print(f"backup.keep_days: {config.get('backup.keep_days')}")

    print("\n✓ 配置管理器工作正常")
