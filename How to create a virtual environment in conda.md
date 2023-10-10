# How to create a virtual env for robotics

## How to create a virtual environment in conda

Creating a virtual environment in Anaconda involves using the `conda` command to set up an isolated environment where you can install specific versions of packages without affecting the system-wide Python installation or other environments. Here are the steps to create a virtual environment in Anaconda on Windows:

1. **Open Command Prompt or Anaconda Prompt**:

   - Open the Start menu, type "cmd," and select "Command Prompt" to open a regular Command Prompt.
   - Open the Start menu, type "Anaconda Prompt," and select "Anaconda Prompt" to open a command prompt with Anaconda functionality.

2. **Create a Virtual Environment**:

   - To create a virtual environment named "myenv", run the following command:

     ```
     conda create --name myenv
     ```

   - You can also specify a particular Python version when creating the environment. For example, to create an environment with Python 3.8, you can use:

     ```
     conda create --name myenv python=3.8
     ```

3. **Activate the Virtual Environment**:

   - To activate the virtual environment, use the following command:

     ```
     conda activate myenv
     ```

   - Replace "myenv" with the name of your environment if it's different.

4. **Install Packages in the Virtual Environment**:

   - Once the environment is activated, you can install packages using 

     `conda` or `pip` within this isolated environment. For example:

     ```
     conda install package_name
     ```

     or

     ```
     pip install package_name
     ```

5. **Deactivate the Virtual Environment** (Optional):

   - To deactivate the environment and return to the base (root) environment, use the following command:

     ```
     conda deactivate
     ```

6. **Delete the Virtual Environment** (Optional):

   - To delete the environment, use the following command:

     ```
     conda remove --name myenv --all
     ```

     Replace "myenv" with the name of your environment.

By following these steps, you'll have successfully created a virtual environment in Anaconda on Windows and can start installing and working with packages within that environment.

7. **Check out all the environments on your system **

   ```
   conda env list
   ```

8. **List all installed packages in your envs**

   ```
   conda list
   ```

   for  some external packages installed by pip, you can use

   ```
   pip3 list
   ```

   

## Create a env for robotics

1. **Create a Virtual Environment for robotics**:

   - To create a virtual environment named "robotics" with  python  version 3.8, run the following command:

     ```zsh
     conda create -n robotics python=3.8
     ```

   - Activate this env:

     ```zsh
     conda activate robotics
     ```

2. **Install all needed packages for RTB**

   some baic packages for math and data analysis need to be installed firstly.

   such as, numpy, scipy and matplotlib.

   ```zsh
   conda install numpy scipy matplotlib
   ```

   after installation,  list  all packages installed by conda and checkout numpy, scipy and matplotlib are installed successfully.

   ```
   conda list
   ```

3. **Install RTB(robotics-toolbox) in robotics env**

   checkout detailed infomations on website https://github.com/petercorke/robotics-toolbox-python

   You will need Python >= 3.6

   ### [Using pip](https://github.com/petercorke/robotics-toolbox-python#using-pip)

   Install a snapshot from PyPI

   ```
   pip3 install roboticstoolbox-python
   ```

   

   Available options are:

   - `collision` install collision checking with [pybullet](https://pybullet.org/)

   Put the options in a comma separated list like

   ```
   pip3 install roboticstoolbox-python[optionlist]
   ```

   

   [Swift](https://github.com/jhavl/swift), a web-based visualizer, is installed as part of Robotics Toolbox.

   ### [From GitHub](https://github.com/petercorke/robotics-toolbox-python#from-github)

   To install the bleeding-edge version from GitHub

   ```
   git clone https://github.com/petercorke/robotics-toolbox-python.git
   cd robotics-toolbox-python
   pip3 install -e .
   ```

   