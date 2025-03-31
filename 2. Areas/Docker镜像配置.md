---
aliases: 
categories: 
important: false
tags:
---
![image.png](https://cdn.jsdelivr.net/gh/duanbiao2000/BlogGallery@main/picture/20240920102749.png)
这张图片显示的是Docker Desktop中创建一个新的MySQL容器的界面。为了正确地运行MySQL容器，你需要根据实际需求填写以下几个部分的信息：

1. **Container name** (容器名): 输入一个唯一的名称来标识你的MySQL容器。建议使用有意义的名字，比如`my-mysql-container`。

2. **Ports** (端口): 这个部分用来映射容器内的端口到主机上的端口。由于MySQL默认使用3306端口，所以你可以在Host port (主机端口) 中填入3306，这样容器内的3306端口就会映射到主机的3306端口。如果你想要公开更多的端口，可以继续添加新的映射。

   注意：如果你的主机上已经有其他服务使用了3306端口，为了避免冲突，你可以选择不同的主机端口号，比如33060。

3. **Volumes** (卷): 如果你想让MySQL的数据持久化存储在主机上，而不是只存在于容器内部，那么你可以在此处添加一个卷映射。例如，你可以添加一条记录，将主机的一个路径（比如`/path/to/mysql/data`）映射到容器内的MySQL数据目录（通常是`/var/lib/mysql`）。

   ```bash
   Host path: /path/to/mysql/data
   Container path: /var/lib/mysql
   ```

   注意：请确保主机路径存在且可写。

4. **Environment variables** (环境变量): MySQL需要知道其root用户的初始密码。为此，你需要添加一个环境变量`MYSQL_ROOT_PASSWORD`，并将值设为你想设定的密码。例如：

   ```bash
   Variable: MYSQL_ROOT_PASSWORD
   Value: your-secret-password
   ```

   注意：请确保密码足够复杂，以保证安全性。

5. 最后，点击右下角的**Run**按钮来启动MySQL容器。



### 使用卷的优点

**优点：**
- **数据持久化**：即使容器被删除或重建，只要卷还存在，数据就不会丢失。
- **易于管理和备份**：可以独立于容器进行备份和恢复。
- **更好的性能**：通常情况下，使用卷可以提供更好的I/O性能，尤其是在处理大量数据时。
- **共享数据**：可以在多个容器之间共享同一个卷。

### 在Windows上使用卷

如果你决定使用卷来持久化MySQL的数据，可以通过以下方式设置：

1. **创建一个本地目录**作为卷的挂载点，比如`C:\docker\mysql-data`。
2. **映射这个目录到容器内的MySQL数据目录**，通常是`/var/lib/mysql`。

在Docker Desktop的图形界面中，你可以在"Volumes"部分添加如下配置：
- **Host path**: `C:\docker\mysql-data`
- **Container path**: `/var/lib/mysql`

或者，如果你通过命令行来启动容器，可以使用`-v`选项来指定卷：

```bash
docker run --name my-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -v C:\docker\mysql-data:/var/lib/mysql -d mysql:latest
```

这样配置后，MySQL的数据会被存储在`C:\docker\mysql-data`目录下，即使容器停止或删除，这些数据仍然会保留在主机上。

### 结论

虽然直接将数据保存在容器内是可行的，但从长远来看，为了数据的安全性和管理方便，建议还是使用卷来持久化MySQL的数据。这不仅有助于防止意外的数据丢失，还能简化数据管理和迁移过程。