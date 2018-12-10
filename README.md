
# BlenderProjectTemplate

Scripts and guidelines to manage multiple Blender projects on the same machine.

## What is this repository for

**Motivation:**
I develop, in parallel, many projects using Blender as core component. Each project requires its specific Blender version, different add-ons (or the same add-ons with different versions), different user preferences, different external editors, and must run on multiple operating systems. Conflicts of the Blender version, preferences, and add-on version among projects is inevitable.

_This project is a template structure helping the management of multiple Blender projects on the same machine._

**Key features:**

* No more conflicts between Blender versions;
* Per-project repository of add-ons;
* Per-project history of last opened scenes;
* Per-project user preferences;
* Support for external editors. (At the moment: PyCharm):
  - Support for Blender namespaces (`bpy`, `mathutils`, ...) in static code analysis;
  - Support debugging;
* Temporary files in a per-project controlled directory.

**Advantages:**

* Flawlessly use a specific version of Blender for each project;
* The add-ons that you develop for a project will not collide with other installations;
* All your Blender user settings will be local to the project, including the list of enabled add-ons and the list of recently opened scenes.

**Disadvantages:**

* A different copy of the Blender executable for each project (Disk space consuming).

Essentially, this project consists of a structured directory tree and a collection of scripts.
After setting up your new project, run Blender using the provided _LaunchBlender_ scripts and enjoy a non-interfering multiple-projects development.

## How to get it / Download / Clone

Get the project from:

* [BlenderProjectTemplate](https://github.com/fnunnari/BlenderProjectTemplate/) at GitHub.

## Setup

* Create a new directory that will be the root of your new project and copy all the directories in the new project directory:
  * MyProject/        (Renamed from BlenderProjectSkeleton)
    * BlenderConfig/
    * BlenderExe/
    * BlenderScenes/
      * \_LaunchBlenderMac.command
      * \_LaunchBlenderWin.bat
      * \_LaunchBlenderLinux.bat
    * BlenderScripts/
      * add-ons/
        * remote_debugger.py
    * BlenderTemp/
    * PyCharm-Blender

* Configure Blender:
  - Make a copy of your Blender editor in the `BlenderExe` directory
    - On Mac, copy the `Blender.app` directory inside BlenderExe
    - On Windows, copy the whole content of the directory containing the `blender.exe`;
    - On Linux, copy the whole content of the directory containing `blender`;

* If you develop a Blender add-on:
  - Create the new add-on file (e.g. _myaddon.py_), or module,  in the `BlenderScripts/addons/` directory.
  - Launch Blender and load it:
    - File -> User Preferences... -> tab _Add-ons_ ->
    - Look for your _myaddon_ in the list and enable it.

* Configure PyCharm:
  - Create a new project using the project root as project directory
  - Right click on directory `BlenderScenes` and `Mark Directory as --> Sources Root`
  - If you want to develop an add-on, right click on directory `BlenderScripts/addons` and `Mark Directory as --> Sources Root`

## How to use it

* Launch Blender by double clicking, or executing from a terminal, the provided _Launch_ scripts for your architecture. The scripts are in the `BlenderScenes`:
  - `cd path/to/MyProject/BlenderScene`
  - On Mac: From Terminal `sh \_LaunchBlenderMac.command`
    - If you run `chmod u+x _LaunchBlenderMac.command`, then you can double-click it from Finder
  - On Windows: From Command Prompt `\_LaunchBlenderWin.bat`
    - You can also double click it from the file explorer
  - On Linux: From a terminal `sh \_LaunchBlenderLinux.sh`

  These scripts will set all the environment variables needed to avoid conflict with other Blender instances in your system.

* Put all the blender scenes (`.blend`) in the `BlenderScenes/` directory

* If you develop stand-alone scripts:
  - Place the scripts (`.py`) in the same BlenderScene directory
  - Load the scripts in the blender scenes Text block
  - Edit the script with your favorite editor (e.g. PyCharm)
  - reload the script in the blender scene after modification

* If you work on an add-on:
  - Place the add-on file, or module in the `BlenderScripts/addons` directory
  - see in a later section on how to reload the add-on (without reloading Blender) if you modify its code .

## How to expose the Blender namespaces to PyCharm

This section explains how to see and used the Blander namespaces (bpy, mathutils) in the PyCharm editor.

This instructions are an adaptation of the Mutantbobs's [pycharm-blender](https://github.com/mutantbob/pycharm-blender) project documentation.

### Configure the python interpreter

Your PyCharm project must use the same python interpreter contained in your local Blender copy.

PyCharm Menu —> Preferences -> Project: … -> Project Interpreter -> “gear” icon -> Add local -> select the python executable in your blender editor (e.g.: `path/to/project/BlenderExe/blender.app/Contents/Resources/2.78/python/bin/python3.5m`)

### Generate Blender namespace stubs

This archive comes with some pre-computed stubs for several Blender versions.
The following instructions are an adaptation of the [pycharm-blender](https://github.com/mutantbob/pycharm-blender) project documentation.

If you need to create stubs for a new Blender version, go on with the following steps:

1. Locate the executable of the Blender version for which you want to create the namespace, e.g.,

   `path/to/project/BlenderExe/blender.app/Contents/MacOS/blender`

2. Open a terminal and `cd` to the `PyCharm-Blender` directory, containing the `python_api` directory.

   `cd path/to/project/PyCharm-Blender/`

3. From the Terminal, launch the Blender exe with the option to execute the generation script:

   `path/to/project/BlenderExe/blender.app/Contents/MacOS/blender -b -P python_api/pypredef_gen.py`

4. This will create a directory named `python_api/pypredef/`

5. Rename the newly generated API, e.g.:

   `mv python_api/pypredef python_api/pypredef-2.79`

This project comes with a set of pre-build namespaces in directory `PyCharm-Blender/python_api`.

### Configure the PyCharm to use the Blender namespace stubs

You must include the newly generated stubs in the search path of your python interpreter.

PyCharm Menu -> Preferences... -> Project: ... -> Project Interpreter -> Project Interpreter x.y.z _path_ Gear -> more... -> (bottom icon) Show paths for current interpreter -> (icon +) Add -> Select e.g. path/to/PyCharm-Blender/python_api/pypredef-2.79

## How to debug Blender code in PyCharm

It is possible to debug the execution of an add-on inside the PyCharm IDE. For it, you need a Professional version of PyCharm (you need the pycharm-debug-py3k.egg)

* Blender side:
  - Install the `Remote debugger` add-on developed by [Sybren A. Stüvel](https://github.com/sybrenstuvel/).
    - There is a version in this archive under `BlenderScripts/addons/remote_debugger.py`.
    - If needed, replace it with a fresh version of the `remote_debugger.py` file from [here](https://code.blender.org/2015/10/debugging-python-code-with-pycharm/) or [here](https://github.com/sybrenstuvel/random-blender-addons/blob/master/remote_debugger.py)
  - Enable the add-on in Blender: open the preferences and set the path to the PyCharm egg file `pycharm-debug-py3k.egg` (i.e., `/Applications/PyCharm.app/Contents/debug-eggs/pycharm-debug-py3k.egg`)

* PyCharm side:
  - Create a debug configuration (Edit configurations):
  	- Add a “Python remote debug”
  	- name, e.g., “Remote Debug”
  	- local host name: localhost
  	- port: 1090
  	- NO redirect output to console
  	- YES suspend after connect
  	- It will automatically fill the lines 2 and 3 with:
  		- Add the following import statement: import pydevd
  		- Add the following command to connect to the debug server: pydevd.settrace('localhost', port=1090)

* Debug:
  - In PyCharm, start the debugger configuration.
  - In Blender, in the 3D View press `space` and search and execute the command: `Connect to remote PyCharm debugger`
  - Now you can put your PyCharm breakpoints and execute your code from Blender.

## Reloading externally modified add-ons

When you edit an add-on in PyCharm (or another editor), it is handy to be able to update the
code without quitting and reloading Blender.

Here is a solution that I also published on a stack overflow question: [Recursive version of 'reload'](https://stackoverflow.com/questions/15506971/recursive-version-of-reload/38243403#38243403)

From Blender:

* Open the script `BlenderScene/ReloadAddOn.py`;
* Edit the last lines to match your module name(s);
* Run the script

## With whom do I talk to?

Fabrizio Nunnari <fab.nunnari@gmail.com>
