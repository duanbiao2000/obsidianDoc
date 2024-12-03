# 实用命令行
## 端口管理器
使用 `Get-Process` 和 `Get-NetTCPConnection` 组合

你可以结合 `Get-Process` 和 `Get-NetTCPConnection` 来查看哪些进程正在监听特定端口。

#### 查看所有监听的 TCP 端口及其对应的进程

```powershell
Get-NetTCPConnection -State Listen | Select-Object LocalAddress, LocalPort, @{Name="ProcessName";Expression={(Get-Process -Id $_.OwningProcess).Name}}
```

![image.png](https://cdn.jsdelivr.net/gh/duanbiao2000/BlogGallery@main/picture/20241007114034.png)
