---
created: 2024-06-04T11:27:29 (UTC +08:00)
tags: []
source: https://ytcutter.cc/manual.php?s=158.6&d=88.6&id=tEFUNLFwPoM&f=video
author: 
---
[Cut and Download Youtube ...](https://ytcutter.cc/)
![](https://cdn.jsdelivr.net/gh/duanbiao2000/BlogGallery/picture/20240604113149.png)

# 剪切并下载 YouTube 视频 --- Cut and Download Youtube Videos

> ## Excerpt
> 您无法从此网站下载剪辑，但以下是如何自行创建剪辑的一些说明：

---
您无法从此网站下载剪辑，但以下是如何自行创建剪辑的一些说明：

1.  运行 cmd.exe - 它将打开一个控制台窗口。输入：`mkdir YTcutter`这将在 C: 驱动器上创建一个 YTcutter 文件夹，您将在其中保存所有必需的文件。
2.  然后输入： `cd YTcutter` 进入该文件夹。
3.  下载 YT-DLP，您将使用它从 YouTube 下载视频。  
      
    将下载的文件移动到 D:\\YTcutter。现在返回到控制台窗口并输入：`yt-dlp` 您应该会看到来自 yt-dlp 的一些使用信息。如果您看到类似“找不到命令”的内容，请检查您的 yt-dlp.exe 文件是否位于 D:\\YTcutter 文件夹中。
	>[!note]我的win11 Powershell中命令为:`.\yt-dlp.exe`
4.  同样下载 FFMPEG，您将用它来从下载的视频中剪切片段（Windows 操作系统的直接链接）。  
      
    在下载的存档中，您只对 bin\\ffmpeg.exe 文件感兴趣。将该文件提取到 D:\\YTcutter。  
      
    返回到控制台窗口并输入： 您应该看到 ffmpeg 的一些文本输出。如果您看到类似“找不到命令”的内容，请检查您的 ffmpeg.exe 文件是否位于 D:\\YTcutter 文件夹中。
    [!note]我的win11 Powershell中命令为:`.\ffmpeg.exe`
5.  如果一切正常，请转到控制台窗口并输入（复制并粘贴）：这会将整个视频下载到您的计算机。如果出现错误，请确保您拥有最新版本的 yt-dlp（它经常变化）
6.  现在运行 ffmpeg 来剪切片段：` ffmpeg -ss 158.6 -t 88.6 -i tEFUNLFwPoM.webm -y -c copy video-158.6-88.6-tEFUNLFwPoM.mp4`  
    您的片段现在位于文件夹 C:\\YTcutter 中的文件 video-158.6-88.6-tEFUNLFwPoM.mp4 中如果您想要此视频中的更多剪辑，下次请跳过步骤 1、3、4、5，仅运行步骤 2 和 6 中的命令。  
7. 如果完成，您可以删除下载的视频以节省磁盘空间： 
	`del tEFUNLFwPoM.webm`

  

