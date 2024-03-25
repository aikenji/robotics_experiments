# How to install anaconda or miniconda

## anaconda

### on windows

在Windows操作系统上安装Anaconda，请按照以下步骤进行：

1. **下载Anaconda**：访问Anaconda网站 https://www.anaconda.com/products/distribution 并下载Anaconda的Windows版本。有时网络下载速度较慢，您可以选择中国其他来源，例如 https://mirror.tuna.tsinghua.edu.cn。
2. **运行安装程序**：找到已下载的可执行文件（例如 `Anaconda3-<version>-Windows-x86_64.exe`）并双击它以开始安装过程。
3. **设置向导**：Anaconda安装向导将打开。按照提示点击“下一步”。
4. **阅读并接受许可协议**：仔细阅读许可协议，如果同意条款，请选择“我同意”。
5. **选择安装类型**：选择是否为“仅自己”（仅适用于当前用户）或“所有用户”（适用于系统上的所有用户）安装Anaconda。点击“下一步”。
6. **选择安装位置**：选择安装目录。通常默认位置即可。点击“下一步”。
7. **高级选项（可选）**：可选择将Anaconda添加到系统路径中，这样您就可以从命令行运行Anaconda命令。务必选中“将Anaconda添加到我的PATH环境变量”复选框。点击“安装”。
8. **安装**：安装程序将开始安装Anaconda。这可能需要几分钟。
9. **完成**：安装完成后，点击“下一步”。
10. **启动Anaconda Navigator（可选）**：您可以选择启动Anaconda Navigator，这是一个用于管理环境和软件包的图形用户界面。如果选中，请点击“完成”。
11. **验证安装**：进入Anaconda Prompt，键入 `conda --version`。如果Anaconda安装正确，它将显示版本号。

Anaconda现已成功安装在您的Windows系统上。您可以使用Anaconda创建和管理Python环境，安装软件包，并运行Python代码。

## Jupyter

0. 安装jupyter notebook, 进入命令行输入:

   ```bash
   conda install jupyter
   ```

1. 在experiments文件夹输入以下命令下打开jupyter notebook

   ```bash
   jupyter notebook
   ```

2. 新建一个txt file，重命名为hello.py, 输入以下代码并保存

   ```python
   def hello(name):
     print(f"Hello, {name}!")
           
   hello("robotics world")
   ```

3. 关闭jupyter，在命令行中按`ctrl+c`退出，在experiments文件夹下通过命令行输入

   ```bash
   python hello.py
   ```

执行代码

