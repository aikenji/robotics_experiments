# 如何使用 spatialmath 包计算刚体的运动

## 准备工作

1. **打开命令提示符cmd：**

   - 进入robotics_experiments目录

2. **进入虚拟环境：**

     ```bash
     conda activate robotics
     ```

## 编写仿真代码

1. 在robotics_experiments目录下，用jupyter新建一个名为 'se2.py' 的空白脚步

2. 在py脚步中，导入 spatialmath 包，并检查包是否正确安装

   ```python
   import spatialmath as sm
   ```

3. 显示 spatialmath 包中的所有内容，并打印包的版本

   ```python
   dir(sm)
   sm.__version__
   ```

4. 阅读 spatialmath 包的教程和文档 https://bdaiinstitute.github.io/spatialmath-python/intro.html#group-operations

该包提供了用于在3D和2D空间中表示姿态和方向的类：

| 在3D中表示 | 在2D中表示 |
| ----------- | ---------- |
| 姿态        | `SE3` `Twist3` `UnitDualQuaternion` |
| 方向        | `SO3` `UnitQuaternion`              |

更具体地说：

- `SE3` 矩阵属于三维位置和方向（姿态）的群
- `SO3` 矩阵属于三维方向的群
- `UnitQuaternion` 属于三维方向的群
- `Twist3` 向量属于三维姿态的群
- `UnitDualQuaternion` 映射到三维位置和方向（姿态）的群
- `SE2` 矩阵属于二维位置和方向（姿态）的群
- `SO2` 矩阵属于二维方向的群
- `Twist2` 向量属于二维姿态的群

这些类提供了方便的类型安全方法和重载运算符来支持：

- 组合，使用 `*` 运算符
- 点变换，使用 `*` 运算符
- 指数，使用 `**` 运算符
- 归一化
- 反转
- 通过矩阵指数和对数运算连接李代数
- 将方向转换为/从欧拉角、滚动-俯仰-偏航角和角-轴形式。
- 列表操作，如附加、插入和获取

这些层次上的操作在一组基本函数上执行，这些函数执行许多相同的操作，但明确地表示数据是使用 `numpy` 数组。

类、方法和函数的名称在很大程度上与 MATLAB 工具箱的名称相似，语义也相似。

## 问题

1. 使用 SE2 包计算齐次矩阵 $T$ 的逆，如下所示：
   $$
   T =
   \begin{pmatrix}
   0 & -1 & 1\\
   1  & 0 & 0 \\
   0 & 0 & 1
   \end{pmatrix}
   $$
   打印答案，并显示逆矩阵表示的坐标系的图形。

2. 计算表示作业 2.1 中两个操作的齐次矩阵。在同一图中用不同颜色绘制表示这些操作的两个坐标系。

3. 使用SE3包生成三维旋转矩阵$R$, 并且打印和画图.
   $$
   R =
   \begin{pmatrix}
   0 & 0 & 1\\
   1  & 0 & 0 \\
   0 & 1 & 0
   \end{pmatrix}
   $$

4. 先绕z轴旋转90度,再绕y轴旋转90度,最后绕z轴旋转90度,计算其等效矩阵$R$.(tips:此处为固定角,不是欧拉角)
