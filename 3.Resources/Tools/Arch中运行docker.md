---
date: 2025-06-11 21:57
tags:
  - Domain/Productivity/Tools
  - Status/TODO
---

在 **Arch Linux (WSL2)** 中直接安装 Docker（非 Docker Desktop）的步骤如下：

---

### **1. 清理已有 Docker Desktop 残留（如有）**

```bash
sudo pacman -Rns docker docker-desktop  # 移除旧版本
sudo rm -rf /var/lib/docker ~/.docker
```

---

### **2. 安装 Docker Engine 和依赖**

#### **(1) 安装基础依赖**

```bash
sudo pacman -Syu --needed docker containerd runc
```

#### **(2) 启动 Docker 服务**

```bash
sudo systemctl enable --now docker
```

#### **(3) 将用户加入 `docker` 组（避免每次用 `sudo`）**

```bash
sudo usermod -aG docker $USER
newgrp docker  # 立即生效（或重新登录）
```

---

### **3. 配置代理（如需）**

#### **(1) 为 Docker Daemon 设置代理**

```bash
sudo mkdir -p /etc/systemd/system/docker.service.d
sudo nano /etc/systemd/system/docker.service.d/http-proxy.conf
```

添加以下内容（替换为你的代理 IP 和端口）：

```ini
[Service]
Environment="HTTP_PROXY=http://172.X.X.1:7897"  # Windows 主机 IP
Environment="HTTPS_PROXY=http://172.X.X.1:7897"
Environment="NO_PROXY=localhost,127.0.0.1"
```

> **获取 Windows 主机 IP**：
>
> ```bash
> cat /etc/resolv.conf | grep nameserver | awk '{print $2}'
> ```

#### **(2) 重启 Docker**

```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```

---

### **4. 验证代理和 Docker 是否正常**

#### **(1) 检查代理配置**

```bash
sudo systemctl show docker --property Environment
# 应输出代理变量
```

#### **(2) 测试拉取镜像**

```bash
docker pull alpine
```

#### **(3) 运行测试容器**

```bash
docker run --rm alpine echo "Hello, Arch Docker!"
```

---

### **5. 常见问题解决**

#### **问题 1：`docker pull` 报 `connection refused`**

- **原因**：代理未生效或代理工具未允许 WSL2 访问。
- **解决**：
  - 确保代理工具（如 Clash/V2Ray）监听 `0.0.0.0`（非 `127.0.0.1`）。
  - 检查防火墙：
    ```powershell
    # Windows 端放行代理端口
    New-NetFirewallRule -DisplayName "Allow WSL2" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 7897
    ```

#### **问题 2：DNS 解析失败**

```bash
sudo nano /etc/docker/daemon.json
```

添加：

```json
{
  "dns": ["8.8.8.8", "1.1.1.1"]
}
```

重启 Docker：

```bash
sudo systemctl restart docker
```

#### **问题 3：Arch 特有依赖缺失**

```bash
sudo pacman -S fuse-overlayfs  # 解决存储驱动问题
```

---

### **6. 完全卸载 Docker**

```bash
sudo systemctl stop docker
sudo pacman -Rns docker containerd runc
sudo rm -rf /var/lib/docker /etc/docker
```

---

### **总结**

- **优势**：原生 Docker 性能更好，代理配置更直接。
- **关键点**：
  1. 通过 `systemd` 为 Docker Daemon 配置代理。
  2. 确保代理工具允许 WSL2 访问（监听 `0.0.0.0`）。
  3. 解决 Arch 特有依赖问题（如 `fuse-overlayfs`）。

如果仍有问题，请提供 `docker pull` 的具体错误日志。
