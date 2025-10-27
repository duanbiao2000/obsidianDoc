
### ✅ 4. 压缩视频（15MB → 3.3MB，几乎无损）
```bash
ffmpeg -i large-video.mp4 -c:v libx264 -crf 23 -c:a aac output.mp4
```
- `libx264`：业界最广泛使用的 H.264 编码器  
- `-crf 23`：默认最佳平衡值（0=无损，63=极低质量）  
- **压缩比**：15.2MB → **3.3MB**（**减少 78%**）  
- **画质感知**：普通用户无法分辨差异

✅ **CRF 值参考表**：

| CRF | 质量 | 文件大小 | 适用场景 |
|-----|------|-----------|----------|
| 18 | 极高 | 大 | 专业存档 |
| 23 | 高 | 中 | **推荐日常使用** |
| 28 | 中 | 小 | 网络分享 |
| 35 | 低 | 很小 | 社交媒体上传 |

## ⚠️ 四、FFmpeg 使用避坑指南（血泪教训）

| 错误做法 | 正确做法 | 原因 |
|----------|----------|------|
| 使用在线 GIF 制作网站 | 用 FFmpeg 本地生成 | 避免隐私泄露、广告插件、恶意脚本 |
| 用 HandBrake 压缩视频 | 用 FFmpeg 直接控制 | HandBrake 是封装工具，无法精细调节 |
| 用 Photoshop 批量压缩图片 | 用 FFmpeg 一行命令 | 一次处理 100 张图，耗时 < 30 秒 |
| 拖拽视频到 Premiere 导出 | 用 `-c copy` 快速裁剪 | 无需重新编码，节省 90% 时间 |
| 用 Obsidian 录屏 | 用 `ffmpeg -f avfoundation` | 更稳定、更高帧率、无延迟 |

## 🌐 五、FFmpeg 在互联网中的真实地位（震撼数据）

| 平台 | 是否使用 FFmpeg | 说明 |
|------|------------------|------|
| YouTube | ✅ 是 | 所有上传视频均经 FFmpeg 转码 |
| Netflix | ✅ 是 | 海量视频转码引擎 |
| TikTok | ✅ 是 | 视频压缩、滤镜、特效底层 |
| Zoom | ✅ 是 | 录屏、音频编码 |
| OBS Studio | ✅ 是 | 核心编解码库 |
| VLC | ✅ 是 | 播放器内核 |
| Adobe Premiere | ✅ 是 | 内部调用 FFmpeg 插件 |
| WhatsApp | ✅ 是 | 视频压缩与格式转换 |

> 🌟 **真相**：  
> **“你每天观看的每一个视频，至少被 FFmpeg 处理过 3 次。”**

---

### 4. 📦 视频压缩（平衡画质与体积）
```bash
# H.264 压缩（推荐默认参数）
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k output.mp4

# 极致压缩（适合网络传输）
ffmpeg -i input.mp4 -c:v libx264 -crf 28 -preset fast -c:a aac -b:a 64k output_small.mp4
```
> ✅ **CRF 值指南**：  
> - 18-23：高质量（适合存档）  
> - 24-28：平衡（适合网络）  
> - 29-35：高压缩（适合移动端）  

---

## 🛡️ 四、专业级技巧（提升 10 倍效率）

### 1. 硬件加速（NVIDIA/Intel）
```bash
# NVIDIA GPU 加速
ffmpeg -hwaccel cuda -i input.mp4 -c:v h264_nvenc -preset p7 -c:a copy output.mp4

# Intel Quick Sync
ffmpeg -hwaccel qsv -i input.mp4 -c:v h264_qsv -preset medium -c:a copy output.mp4
```

### 2. 无损剪辑（精确到帧）
```bash
# 从 00:01:30 开始，截取 30 秒
ffmpeg -ss 00:01:30 -i input.mp4 -t 30 -c copy output_clip.mp4

# 精确到帧（避免音画不同步）
ffmpeg -ss 00:01:30 -i input.mp4 -t 30 -c:v libx264 -c:a aac output_sync.mp4
```

### 3. 修复抖动视频
```bash
# 启用去抖动滤镜
ffmpeg -i shaky_video.mp4 -vf "vidstabdetect=shakiness=10:accuracy=15,vidstabtransform=input=transforms.trf:smoothing=30" -c:a copy stabilized.mp4
```

---

## 📊 五、参数速查表

| 场景 | 核心参数 | 推荐值 |
|------|----------|--------|
| **视频压缩** | `-crf` | 23（平衡）/ 18（高质量） |
| **GIF 生成** | `fps` | 10-15（流畅度） |
| **图片缩放** | `scale` | `1920:-1`（自动高度） |
| **音频提取** | `-vn -c:a` | `libmp3lame -q:a 2` |
| **屏幕录制** | `-f avfoundation` | `"1:0"`（macOS 设备号） |
| **硬件加速** | `-hwaccel` | `cuda` / `qsv` |

---

## 💡 终极心法

> **“不要记忆参数，要理解管道”**  
> FFmpeg 的本质是 **媒体处理流水线**：  
> 输入 → 滤镜链 → 编码器 → 输出  
>   
> 掌握这个思维，任何需求都能拆解组合！
