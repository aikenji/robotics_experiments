# 如何为机器人学创建虚拟环境

## 如何在conda中创建虚拟环境

在Anaconda中创建虚拟环境涉及使用`conda`命令来设置一个隔离的环境，在这个环境中，您可以安装特定版本的软件包，而不会影响全局的Python安装或其他环境。以下是在Windows上在Anaconda中创建虚拟环境的步骤：

1. **打开命令提示符或Anaconda提示符**：

   - 打开“开始”菜单，键入“Anaconda Prompt”，然后选择“Anaconda Prompt”以打开具有Anaconda功能的命令提示符。

2. **创建虚拟环境**：

   - 要创建名为"myenv"的虚拟环境，请运行以下命令：

     ```
     conda create --name myenv
     ```

   - 您还可以在创建环境时指定特定的Python版本。例如，要创建一个使用Python 3.8的环境，您可以使用：

     ```
     conda create --name myenv python=3.8
     ```

3. **激活虚拟环境**：

   - 要激活虚拟环境，请使用以下命令：

     ```
     conda activate myenv
     ```

   - 如果环境名称不同，请用您环境的名称替换"myenv"。

4. **在虚拟环境中安装软件包**：

   - 一旦环境被激活，您就可以在这个隔离的环境中使用`conda`或`pip`安装软件包。例如：

     ```
     conda install package_name
     ```

     或者

     ```
     pip install package_name
     ```

5. **停用虚拟环境**（可选）：

   - 要停用环境并返回到基本（根）环境，请使用以下命令：

     ```
     conda deactivate
     ```

6. **删除虚拟环境**（可选）：

   - 要删除环境，请使用以下命令：

     ```
     conda remove --name myenv --all
     ```

     将"myenv"替换为您环境的名称。

通过按照这些步骤，您将成功在Windows上的Anaconda中创建了一个虚拟环境，并可以开始在该环境中安装和使用软件包。

7. **查看系统中所有的环境** 

   ```
   conda env list
   ```

8. **列出所有环境中安装的软件包**

   ```
   conda list
   ```

   对于一些由pip安装的外部软件包，您可以使用

   ```
   pip3 list
   ```

   

## 为机器人学创建一个环境

1. **为机器人学创建一个虚拟环境**：

   - 要创建一个名为"robotics"的虚拟环境，并使用Python 3.8版本，请运行以下命令：

     ```zsh
     conda create -n robotics python=3.8
     ```

   - 激活这个环境：

     ```zsh
     conda activate robotics
     ```

2. **安装RTB所需的所有软件包**

   首先需要安装一些用于数学和数据分析的基本软件包。

   例如，numpy、scipy和matplotlib。

   ```zsh
   conda install numpy scipy matplotlib
   ```

   安装完成后，列出conda安装的所有软件包，并检查numpy、scipy和matplotlib是否成功安装。

   ```
   conda list
   ```

3. **在机器人学环境中安装RTB（机器人工具箱）**

   查看网站https://github.com/petercorke/robotics-toolbox-python上的详细信息

   您将需要Python >= 3.6

   ### [使用pip](https://github.com/petercorke/robotics-toolbox-python#using-pip)

   从PyPI安装一个快照

   ```
   pip3 install roboticstoolbox-python
   ```

   

   可用选项包括：

   - `collision` 安装与[pybullet](https://pybullet.org/)的碰撞检查

   将选项放在逗号分隔的列表中，如

   ```
   pip3 install roboticstoolbox-python[optionlist]
   ```

   

   [Swift](https://github.com/jhavl/swift)，一个基于Web的可视化工具，作为Robotics Toolbox的一部分安装。

   ### [从GitHub安装](https://github.com/petercorke/robotics-toolbox-python#from-github)

   从GitHub安装最新版本

   ```
   git clone https://github.com/petercorke/robotics-toolbox-python.git
   cd robotics-toolbox-python
   pip3 install -e .
   ```

