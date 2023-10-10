# How to install anaconda or miniconda

## anaconda

### on windows

To install Anaconda on a Windows operating system, follow these steps:

1. **Download Anaconda**: Go to the Anaconda website at https://www.anaconda.com/products/distribution and download the Windows version of Anaconda. Sometimes network download speed is slow,  you can chose other source in china, such as https://mirror.tuna.tsinghua.edu.cn.
2. **Run the Installer**: Locate the downloaded executable file (e.g., `Anaconda3-<version>-Windows-x86_64.exe`) and double-click on it to start the installation process.
3. **Setup Wizard**: The Anaconda installation wizard will open. Follow the prompts and click "Next."
4. **Read and Accept the License Agreement**: Carefully read the license agreement and select "I agree" if you agree to the terms.
5. **Select Installation Type**: Choose whether to install Anaconda for "Just Me" (only for the current user) or "All Users" (for all users on the system). Click "Next."
6. **Select Installation Location**: Choose the installation directory. The default location is usually fine. Click "Next."
7. **Advanced Options (Optional)**: Optionally, you can choose to add Anaconda to your system PATH, which allows you to run Anaconda commands from the command line. It's recommended to check the box that says "Add Anaconda to my PATH environment variable." Click "Install."
8. **Install**: The installer will start installing Anaconda. This may take a few minutes.
9. **Completion**: Once the installation is complete, click "Next."
10. **Start Anaconda Navigator (Optional)**: You can choose to start Anaconda Navigator, a graphical user interface for managing your environments and packages. If selected, click "Finish."
11. **Verify Installation**: Open a command prompt or Anaconda Prompt and type `conda --version`. If Anaconda is installed correctly, it will display the version number.

Anaconda is now successfully installed on your Windows system. You can create and manage Python environments, install packages, and run Python code using Anaconda.

### on Mac

To install Anaconda on a Mac, follow these steps:

1. **Download Anaconda**: Go to the Anaconda website at https://www.anaconda.com/products/distribution and download the macOS version of Anaconda.
2. **Open the Installer**: Locate the downloaded `.pkg` file (e.g., `Anaconda3-<version>-MacOSX-x86_64.pkg`) and double-click on it to start the installation process.
3. **Begin the Installation**: The Anaconda installation wizard will open. Click "Continue."
4. **Read and Accept the License Agreement**: Carefully read the license agreement and click "Continue." Then, click "Agree" to accept the terms.
5. **Select Installation Location**: Choose the installation location. The default location is usually fine. Click "Install."
6. **Enter Admin Password**: Enter your administrator password to allow the installation process to make changes. Click "Install Software."
7. **Installation in Progress**: The installer will start installing Anaconda. This may take a few minutes.
8. **Installation Complete**: Once the installation is complete, click "Close."
9. **Verify Installation**: Open a terminal and type `conda --version`. If Anaconda is installed correctly, it will display the version number.

Anaconda is now successfully installed on your Mac. You can create and manage Python environments, install packages, and run Python code using Anaconda.

## Miniconda

Miniconda is a lightweight version of Anaconda that includes only Conda (the package manager) and Python. Here's how you can install Miniconda on both Windows and macOS:

###  on Windows:

1. **Download Miniconda**: Go to the Miniconda website at https://docs.conda.io/en/latest/miniconda.html and download the Windows installer (e.g., `Miniconda3-Windows-x86_64.exe` for 64-bit Windows).
2. **Run the Installer**: Locate the downloaded executable file and double-click on it to start the installation process.
3. **Setup Wizard**: The Miniconda installation wizard will open. Follow the prompts and click "Next."
4. **Read and Accept the License Agreement**: Carefully read the license agreement and select "I agree" if you agree to the terms.
5. **Select Installation Type**: Choose whether to install Miniconda for "Just Me" (only for the current user) or "All Users" (for all users on the system). Click "Next."
6. **Select Installation Location**: Choose the installation directory. The default location is usually fine. Click "Next."
7. **Advanced Options (Optional)**: Optionally, you can choose to add Miniconda to your system PATH, which allows you to run Conda commands from the command line. It's recommended to check the box that says "Add Anaconda to my PATH environment variable." Click "Install."
8. **Install**: The installer will start installing Miniconda. This may take a few minutes.
9. **Completion**: Once the installation is complete, click "Finish."
10. **Verify Installation**: Open a command prompt and type `conda --version`. If Miniconda is installed correctly, it will display the version number.

### on macOS:

1. **Download Miniconda**: Go to the Miniconda website at https://docs.conda.io/en/latest/miniconda.html and download the macOS installer (e.g., `Miniconda3-MacOSX-x86_64.sh`).

2. **Open the Terminal**: Open the Terminal application on your macOS.

3. **Run the Miniconda Installer Script**: Navigate to the directory where you downloaded the Miniconda installer using the `cd` command. For example:

   ```bash
   cd Downloads
   ```

4. **Run the Installer Script**: Run the Miniconda installer script using the following command:

   ```bash
   bash Miniconda3-MacOSX-x86_64.sh
   ```

5. **Follow the Installation Process**: Follow the prompts to accept the license agreement, choose the installation location, and complete the installation process.

6. **Verify Installation**: Open a new terminal window and type `conda --version`. If Miniconda is installed correctly, it will display the version number.

Miniconda is now successfully installed on your system, and you can use it to create and manage Python environments and install packages using Conda.