# Virtual Environments

Virtual environments enable you to create a standalone environment for your project so that you can avoid conflicts between one project and another in terms of software versions (ie. `python` or `ruby`) as well as the versions of other libraries that your project might depend upon.

# Objectives

Through participating in this session, attendees will be able to:

* Identify what a virtual environment is AND when using a virtual environment is a suitable solution to a task
* Create a virtual environment
* Populate a virtual environment with the software necessary to complete a programming/development task

# Lecture/Demos

## What is a virtual environment?

Virtual environments (also called virtualenvs) are tools used to keep projects separate, especially in terms of keeping different software versions separate and different library versions separate. For example, virtualenvs prevent Python's site packages folder from getting disorganized and cluttered AND prevents problems that arise when one project needs **version x.x** of a library but another project needs **version y.y** of the same library. At their core, virtualenvs are glorified directories that use scripts and metadata to organize and control the environment. You are allowed to have an unlimited number of virtualenvs. And as you will see, they are very easy to create using various command line tools, such as `conda`.

## When should we use a virtual environment?

As noted above, anytime you have more than one project and there is a possibility of conflicts between your libraries, it is a good time to use a virtualenv. Having said that, many programmers use virtual environments for **all but the most trivial** programming tasks. Especially for beginners, using virtualenvs early on in your learning career will build a valuable skill AND help eliminate sneaky bugs related to version discrepancies. Bugs that can be hard to diagnose.

## The big picture

Throughout this workshop, we will be looking at a series of images to help us understand what we are doing and what effect our changes will have.

We will try to highlight when we are interacting with local files OR with our Github Repository OR with the original project's repository, etc.

For this lesson, we can image a fairly typical directory/folder structure on your local computer. Note:

* a directory that **your project(s)** will be saved in
* a directory for **miniconda**

![Our Local Directories](images/basic_dir.png)

When you create a virtualenv, conda will make changes to the miniconda directory. It will create a directory that will contain:

* a database and metadata about the virtualenv
* software and libraries related to the project (i.e. Python and any modules you install in the virtualenv)

NOTE: these folders are **NOT** duplicates of each other, but they are tied to one another. The miniconda virtualenv folders will **NOT** contain your project code.


![Local Dirs with conda environments](images/conda_envs.png)


## How do you create a virtual environment?

There are several programs or libraries that can generate virtualenvs (see the [Resources](#resources) section for a list). For today's lesson, we will be using the `conda` package manager, which includes the capability to simply and easily produce virtualenvs.

Presuming you have `conda` installed, the following steps will enable you to create your first virtual environment.

```python
$ conda create -n mytest python=3
```
`conda` runs the conda program.

`create` tells it to create a virtualenv

`-n` identifies the name of the virtualenv, in this case, `mytest`

`python=3` tells conda that you want to install Python version 3 in this virtualenv

**NOTE**: you can use version 2.x or version 3.x of Python and regardless which you choose, conda will default to the most recent version of Python. Sorta... [see footnote 1](#footnotes). If you need to select a specific minor version of python, use the following syntax:

`python=3.2`

Conda will prepare to install python and any dependencies that Python relies upon. It will display output similar to the following. 

    MacComputer:intro_to_sprinting username$ conda create -n mytest python=3
    Fetching package metadata .......
    Solving package specifications: ..........
    
    Package plan for installation in environment /Users/username/miniconda3/envs/mytest:
    
    The following packages will be downloaded:
    
        package                    |            build
        ---------------------------|-----------------
        openssl-1.0.2k             |                1         3.0 MB
        python-3.6.0               |                0        11.7 MB
        setuptools-27.2.0          |           py36_0         523 KB
        wheel-0.29.0               |           py36_0          87 KB
        pip-9.0.1                  |           py36_1         1.7 MB
        ------------------------------------------------------------
                                               Total:        17.0 MB
    
    The following NEW packages will be INSTALLED:
    
        openssl:    1.0.2k-1
        pip:        9.0.1-py36_1
        python:     3.6.0-0
        readline:   6.2-2
        setuptools: 27.2.0-py36_0
        sqlite:     3.13.0-0
        tk:         8.5.18-0
        wheel:      0.29.0-py36_0
        xz:         5.2.2-1
        zlib:       1.2.8-3
    
    Proceed ([y]/n)?

To finish the creation of the virtualenv and install the software, press:

`y`

## Activate your virtualenv

Once you have created a virtualenv, you will need to activate it. Activation has several side effects:

* It temporarily changes your `$PATH` variable so calls to the `python` command (and similar commands) will look first in the virtualenv's `bin/` directory. 
* It temporarily changes your shell prompt to show which virtualenv you are using. Your prompt will likely look something like this, with the name of your virtualenv in parenthesis in front of the prompt:
    * `(mytest) $` OR 
    * `(mytest) C:\>`

To activate your virtualenv, run the appropriate command for your operating system:

### Linux\Mac OSX version

```bash
$ source activate mytest
```
### Windows version

```bat
C:\> activate mytest
```

## Adding software to your virtualenv 

To add more software to the virtualenv, you can use `conda` to install the software. The maintainers of conda provide access to many Python and non-Python libraries, but not all of them. If conda cannot install a particular library that you need, you can generally use `pip` or a similar package installation tool to install it instead (covering `pip` is outside the scope of this workshop).

For example, to install IPython, you can use the following `conda` command:

```
conda install ipython
```

Conda will prepare to install IPython and any dependencies that IPython relies upon. It will display output similar to the following (truncated to save space).


    Fetching package metadata .......
    Solving package specifications: ..........
    
    Package plan for installation in environment /Users/chalmerlowe/miniconda3:
    
    The following packages will be downloaded:
    
        package                    |            build
        ---------------------------|-----------------
        conda-env-2.6.0            |                0          601 B
        ...
        ipython-5.3.0              |           py35_0        1021 KB
        conda-4.3.14               |           py35_0         505 KB
        ------------------------------------------------------------
                                               Total:         3.8 MB
    
    The following NEW packages will be INSTALLED:
    
        appnope:          0.1.0-py35_0
        ...
        wcwidth:          0.1.7-py35_0
    
    The following packages will be UPDATED:
    
        conda:            4.1.11-py35_0 --> 4.3.14-py35_0
        conda-env:        2.5.2-py35_0  --> 2.6.0-0
        requests:         2.10.0-py35_0 --> 2.13.0-py35_0
    
    Proceed ([y]/n)?

To finish the installation of IPython and its dependencies, press:

`y`

### Multiple packages

Multiple packages can be installed at the same time, by separating the package names with spaces:

`conda install flake8 mock funcsigs`

## Leaving the virtualenv when you are done

When you are done working in your virtualenv, you can deactivate it using the following command:

### Linux\Mac OSX version

```bash
(mytest) $ source deactivate
$
```

### Windows version

```bat
(mytest) C:\> deactivate
C:\>
```

# Resources

For more information, try these resources:

## Conda
[Conda Docs](http://conda.pydata.org/docs/get-started.html): A getting started guide on how to use conda

## Other tools

Other tools include:

* `virtualenv` AND 
* `venv` 

Using either of these tools should be very similar to using conda, but there may be nuances depending on your system, the tool you choose to use and your version of Python. 

|[<<< Previous Lesson: Tool Installation](./lesson_02_tool_installation.md)|[Next Lesson: Github Overview >>>](./lesson_04_github_overview.md)|
|:--|--:|

# Footnotes

[1]: the maintainers of conda put together packages for the most recent versions of Python as they get released, but sometimes there may be a short lag.
