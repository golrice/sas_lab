# sas_lab
## 安装依赖

要安装本项目所需的依赖，请遵循以下步骤：

1. **确保你拥有Python环境**：笔者的版本是3.10.2。


2. **安装部分依赖包**：

   使用以下命令安装`requirements.txt`文件中列出的所有依赖库：
   ```sh
   pip install -r requirements.txt
   ```

3. **验证安装**：

   安装完成后，你可以使用以下命令来验证依赖是否已正确安装：
   ```sh
   pip list
   ```

4. **安装ffmpeg**：

   在Unix/Linux系统上，你可以使用以下命令安装ffmpeg：
   ```sh
   sudo apt-get install ffmpeg
   ```

   安装完成后，你可以使用以下命令验证ffmpeg是否已正确安装：
   ```sh
   ffmpeg -h
   ```

   在Windows系统上，你可以从[ffmpeg官网](https://ffmpeg.org/download.html)下载安装包并安装。需要注意添加到系统路径当中。

请注意，如果你使用的是Python 2，请将上述命令中的`pip`替换为`pip3`。

## 使用说明
目录介绍：

- `bin`: 存放一些脚本文件。
- `requirements`: 存放项目所需的依赖库。
- `src`: 存放项目源码。
- `resouces`: 存放项目资源文件。
- `tests`: 存放项目测试用例。
- `README.md`: 项目说明文件。
- `LICENSE`: 项目许可证文件。

### bin目录

- `sound2matrix.py`: 将声音信号转换成矩阵形式存储，不需要在意
- `trans_format.py`: 转换存储声音的格式，不需要在意

### requirements目录

- `requirements.txt`: 项目所需的依赖库列表。

### src目录

- `main.py`: 主程序，用于处理音频文件。
- `example`: 课程提供的示例代码。

### resouces目录

- `eigenfunction`: 存放特征的信号
- `vocal`: 存放人声的声音文件
