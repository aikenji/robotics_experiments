# Denavit-Hartenberg 模型

## 已发布的机器人模型

| 模型名称  | 描述                                                   |
| --------- | ------------------------------------------------------ |
| Ball      | 一个可以折叠成球形的 n 关节机器人                      |
| Cobra600  | 4 轴 Adept（现在是 OMRON）SCARA 机器人                 |
| IRB140    | 6 轴 ABB 机器人                                        |
| KR5       | 6 轴库卡机器人                                         |
| Panda     | 7 轴 Franka-Emika 机器人                               |
| Puma      | 6 轴 Unimation 机器人（带动力学数据）                  |
| Stanford  | 6 轴 Stanford 研究机器人，1 个棱柱关节（带动力学数据） |
| Threelink | ??                                                     |

## 使用 Denavit-Hartenberg 参数创建新的机器人模型

要开始，您需要知道：

1. 您机器人的 DH 参数。
2. 模型是否使用标准的 Denavit-Hartenberg 参数或修改过的 Denavit-Hartenberg 参数，分别为 DH 或 MDH。
3. 关节结构，它是否具有旋转关节、棱柱关节或两者兼有。

### 编写定义

创建一个名为 `MYROBOT.py` 的文件，其中 `MYROBOT` 是您机器人的描述性名称，必须是有效的文件名和 Python 类名。

将以下代码块剪切并粘贴到您的空文件中，随着操作的进行进行修改。我们从定义开始：

```python
from math import pi
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH, RevoluteMDH, PrismaticMDH
```

最后一行很重要，它定义了您可能需要的所有类。您不会使用所有类，为了保持整洁，您可以删除您不使用的那些类。这是它们的作用：

* `RevoluteDH` 用于使用标准 DH 参数的旋转关节
* `PrismaticDH` 用于使用标准 DH 参数的棱柱关节
* `RevoluteMDH` 用于使用修改过的 DH 参数的旋转关节
* `PrismaticMDH` 用于使用修改过的 DH 参数的棱柱关节

接下来，尽可能添加尽可能多的描述，查看此文件夹中的其他模型文件以获得启发。

```python
class MYROBOT(DHRobot):
    """
    创建 MYROBOT manipulator 的模型

       .
       .
       .

    :notes:
       .
       .
       .

    :references:
       .
       .
       .     

    """
```

始终添加关于使用的单位、DH 约定的说明，并包括模型来源的任何参考资料。

现在是主要部分：在 `__init__` 方法内部，通过创建适当的链接类的实例来定义一组链接变量。

```python
def __init__(self):

        deg = pi/180

        L0 = RevoluteDH(
            d=0,          # 链接长度（Dennavit-Hartenberg 符号）
            a=0,          # 链接偏移量（Dennavit-Hartenberg 符号）
            alpha=pi/2,   # 链接扭曲（Dennavit-Hartenberg 符号）
            I=[0, 0.35, 0, 0, 0, 0],  # 链接相对于质心的惯性张量 I = [L_xx, L_yy, L_zz,
                                      # L_xy, L_yz, L_xz]
            r=[0, 0, 0],  # 第 i 个原点到质心的距离 [x,y,z]，在链接参考框架中
            m=0,          # 链接质量
            Jm=200e-6,    # 电机惯性
            G=-62.6111,   # 齿轮比
            B=1.48e-3,    # 电机粘性摩擦系数（在电机上测量）
            Tc=[0.395, -0.435],  # 电机库仑摩擦系数，方向 [-,+]（在电机上测量）
            qlim=[-160*deg, 160*deg])    # 最小和最大关节角度

        L1 = RevoluteDH(
            d=0, a=0.4318, alpha=0,
            qlim=[-45*deg, 225*deg])

            .
            .
            .   

```

尽可能提供参数。上面的 `L0` 定义包括运动学和动力学参数，而 `L1` 只包括运动学参数。最小要求是运动学参数，您甚至不需要知道关节限制，因为只有少数 Toolbox 函数需要它们。

对于具有 N 个关节的机器人，必须定义 N 个关节实例。

接下来，我们调用超类构造函数来完成繁重的工作。

```python
        super().__init__(
            [L0, L1, L2, L3, L4, L5],
            name="MYROBOT",
            manufacturer="COMPANY THAT BUILDS MYROBOTs")
```

我们传入了一个有序列表，其中包含我们之前创建的所有关节对象，并添加了一些元数据。名称将用于绘图。

我们可能希望定义一些有用的关节配置，例如主页位置或用于拾取小部件的位置。您可以定义任意数量的这些配置，但模式如下所示：

```python
        # 零角度，L 形姿势
        self._MYCONFIG = np.array([1, 2, 3, 4, 5, 6])  # 创建实例属性

    @property
    def MYCONFIG(self):
        return self._MYCONFIG

```

其中 `MYCONFIG` 是这个特定配置的名称。定义一个包含 N 个元素的 NumPy 数组的实例属性，

它必须是关节配置。然后定义一个属性，该属性将返回该属性。

许多 Toolbox 模型都有一个称为 `qz` 的配置，它是零关节角的集合。

最后，我们可以使机器人定义为可执行脚本。我们通过在文件顶部添加一个 hashbang 行

```python
#!/usr/bin/env python
```

和在底部添加一个主代码块

```python
if __name__ == '__main__':

    robot = MYROBOT()
    print(robot)
```

这样，如果您从 shell 运行它

```
% ./Puma560.py 
┏━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━┓
┃   θⱼ    ┃   dⱼ    ┃   aⱼ   ┃  ⍺ⱼ   ┃
┣━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━╋━━━━━━━┫
┃q0 + 0.0 ┃   0.672 ┃      0 ┃  90.0 ┃
┃q1 + 0.0 ┃       0 ┃ 0.4318 ┃   0.0 ┃
┃q2 + 0.0 ┃ 0.15005 ┃ 0.0203 ┃ -90.0 ┃
┃q3 + 0.0 ┃  0.4318 ┃      0 ┃  90.0 ┃
┃q4 + 0.0 ┃       0 ┃      0 ┃ -90.0 ┃
┃q5 + 0.0 ┃       0 ┃      0 ┃   0.0 ┃
┗━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━┻━━━━━━━┛
```

我们可以看到 Denavit-Hartenberg 参数的表格。

### 测试

如果您将定义设置为可执行的 Python 脚本，如上所示，则运行它并检查参数是否符合预期。

如果您定义了一些配置，还可以测试它们是否正确。

```python
    myrobot = MYROBOT()  # 实例化您模型的实例
    print(myrobot)       # 显示其运动学参数
    print(myrobot.MYCONFIG)    # 检查关节配置是否正常工作
```

### 下一步

您现在可以利用 Toolbox 的功能来计算正向和逆向运动学、显示图形模型，并交互式地教授机器人。如果您定义了动态参数，则可以计算正向和逆向刚体动力学，并模拟机器人对施加的扭矩的响应。

祝你好运，玩得开心！

### 贡献您的模型

如果您认为您的模型可能对其他人有趣，请考虑提交拉取请求。
