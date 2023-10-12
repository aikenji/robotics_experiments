# How to use spatialmath package to calculate motion of rigid body

## Preliminaries

To create a new directory (folder) using the Command Prompt (cmd) in Windows, follow these steps:

1. **Open the Command Prompt:**

   - Press `Win + R` on your keyboard to open the Run dialog.
   - Type `cmd` and press Enter, or click OK.

2. **Navigate to the location where you want to create the directory:**

   - Use the `cd` command to change the directory (if needed) to the location where you want to create the new directory. For example, to go to the desktop, you can use:

     ```
     cd Desktop
     ```

3. **Create the new directory:**

   - Use the `mkdir` command followed by the desired directory name to create a new directory. For example:

     ```
     mkdir Robotics
     ```

After executing the `mkdir` command, you'll have created a new directory with the specified name Robotics in the location you navigated to.



## Hello robotics world

Write the first robotics simulation code in python:

1. Open a blank file named 'hello_robotics_world.py'

   ```bash
   touch hello_robotics_world.py
   ```

2. Use your favourite editor to open the file. Import the spatialmath package, and check whether the package is installed correctly

   ```python
   import spatialmath as sm
   ```

3. Show all contents in the spatialmath package and print the version of packages 

   ```python
   dir(sm)
   sm.__version__
   ```

    

4. Read the tutorial and docs of spatialmath package https://bdaiinstitute.github.io/spatialmath-python/intro.html#group-operations

The package provides classes to represent pose and orientation in 3D and 2D space:

| Represents  | in 3D                               | in 2D          |
| ----------- | ----------------------------------- | -------------- |
| pose        | `SE3` `Twist3` `UnitDualQuaternion` | `SE2` `Twist2` |
| orientation | `SO3` `UnitQuaternion`              | `SO2`          |

More specifically:

- `SE3` matrices belonging to the group for position and orientation (pose) in 3-dimensions
- `SO3` matrices belonging to the group for orientation in 3-dimensions
- `UnitQuaternion` belonging to the group for orientation in 3-dimensions
- `Twist3` vectors belonging to the group for pose in 3-dimensions
- `UnitDualQuaternion` maps to the group for position and orientation (pose) in 3-dimensions
- `SE2` matrices belonging to the group for position and orientation (pose) in 2-dimensions
- `SO2` matrices belonging to the group for orientation in 2-dimensions
- `Twist2` vectors belonging to the group for pose in 2-dimensions

These classes provide convenience and type safety, as well as methods and overloaded operators to support:

- composition, using the `*` operator
- point transformation, using the `*` operator
- exponent, using the `**` operator
- normalization
- inversion
- connection to the Lie algebra via matrix exponential and logarithm operations
- conversion of orientation to/from Euler angles, roll-pitch-yaw angles and angle-axis forms.
- list operations such as append, insert and get

These are layered over a set of base functions that perform many of the same operations but represent data explicitly in terms of `numpy` arrays.

The class, method and functions names largely mirror those of the MATLAB toolboxes, and the semantics are quite similar.

## Questions

1. Use SE2 packages to calculate the inverse of the homogenous matrix $T$ as showed below 
   $$
   T = 
   \begin{pmatrix}
   0 & -1 & 1\\
   1  & 0 & 0 \\
   0 & 0 & 1
   \end{pmatrix}
   $$
    print the answer and show the graph of the frame presented by the inverse.

   

2. Calculate  homogeneous matrix representing the two operations in homework 2.1. Draw the two frames presenting these operations in the same graph by different colors. 