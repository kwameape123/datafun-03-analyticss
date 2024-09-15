# Virtual Environment
## Overview
Virtual environment provide each project with an isolated environment or "hub". It allows each project to have 
unique packages and dependencies without affecting the main or central python environment. This is important
to prevent depencies conflicts.
Virtual environment folders are conventionally named .venv. 
When we are using virtual environment, we follow the steps below;
1. Create the virtual environment.
2. Activate the virtual environment.
3. Install packages to the virtual environment.

# Create the virtual environment
1. Open VS Code in a project folder.
2. Open Powershell terminal in VS Code.
3. Type the command below;
```shell
py -m venv .venv
```
4. Virtual environment is created

# Activate the virtual environment
1. Within the opened VS Code editor, type the command below;
```shell
.venv/Scripts/Activate
```
2. Virtual environment is active when the terminal shows the command below;
(.venv) PS C:\Users\kwame\Documents\datafun-03-analyticss

# Install packages to the virtual environment
1. We can install packages individually and then compile the 
list of installed packages. The commands for this approach is below;
``` shell
py -m pip install package_name #This step is repeated for all needed packages
pip freeze > requirements.txt
```
2. We can also list all needed packages and the versions in a requirements.txt file
and then install them at a go. We must make sure the packages and their version are in the 
format package==0.00.00(version). The commands for this approach is below;
```shell
py -m pip install -r requirements.txt
```





