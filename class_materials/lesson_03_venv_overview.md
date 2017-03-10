# Virtual Environments

Virtual environments enable you to create a standalone environment for your project so that you can avoid conflicts between one project and another in terms of Python versions as well as the versions of other libraries that your project might depend upon.

# Objectives

Through participating in this session, attendees will be able to:
* Identify what a virtual environment is AND when using a virtual environment is a suitable solution to a task
* Create a virtual enviroment
* Populate a virtual environment with the software necessary to complete a programming/development task

# Lecture/Demos

## What is a virtual environment?

Virtual environments (also called virtualenvs) are tools used to keep projects separate, especially in terms of keeping different Python versions separate and different library versions separate. Virtualenvs prevent Python's site packages folder  from getting disorganized and cluttered AND prevents problems that arise when one project needs version x.x of a library but another project needs version y.y of the same library. At their core, virtualenvs are glorified directories that use scripts and metadata to organize and control the environment. You are allowed to have an unlimited number of virtualenvs. And as you will see, they are very easy to create using the various command line tools, such as conda.

## When should we use a virtual environment?

As noted above, anytime you have more than one project and there is a possibility of conflicts between your libraries, it is a good time to use a virtualenv. Having said that, many programmers use virtual environments for **all but the most trivial** programming tasks. Especially for beginners, using virtualenvs early on in your learning career will build a valuable skill AND help eliminate sneaky bugs related to version discrepancies. Bugs that can be hard to diagnose.

## How do you create a virtual environment?

There are several programs or libraries that can generate virtualenvs (see the [Resources](#resources) section for a list). For today's lesson, we will be using the `conda` package manager, which includes the capability to simply and easily produce virtualenvs.

Presuming you have `conda` installed, the following steps will enable you to create your first virtual environment.

```python
$ conda create -n mycalc python=3
```
`conda` runs the conda program.

`create` tells it to create a virtualenv

`-n` identifies the name of the virtualenv, in this case, `mycalc`

`python=3` tells conda that you want to install Python version 3 in this virtualenv

NOTE: you can use version 2.x or version 3.x of Python and regardless which you choose, conda will default to the most recent version of Python. Sorta, [see footnotes](#footnotes).



## How do you populate it with the right software versions and libraries?

Once you have created a virtualenv you need to activate it AND then populate it with software.

### Activating your virtualenv

#### Linux\Mac OSX version

```bash
$ source activate mycalc
```

#### Windows version

```bat
rem typical windows
C:\> activate mycalc
```

## adding software

To add software to the virtualenv, you can use a tool call pip, which comes by default in modern versions of Python. For example, to install IPython, you can use the following command:

```
pip install ipython
```

## How do you get out of the virtual environment when you are done?

When you are done working in your virtualenv, you can deactivate it using the following command:

### Linux\Mac OSX version

```bash
# typical linux
(mycalc) $ deactivate
```

### Windows version

```bat
rem typical windows
(mycalc) C:\> deactivate
```

# HANDS-ON

# Resources

For more information, try these resources:

[Conda Docs](http://conda.pydata.org/docs/get-started.html)



Other tools include `virtualenv` and `venv` The exact method may vary depending on your system, the tool you choose to use and your version of Python. 



|[<<< Previous Lesson: Tool Installation](./lesson_02_tool_installation.md)|[Next Lesson: Github Overview >>>](./lesson_04_github_overview.md)|
|:--|--:|

# Footnotes
[1]: the maintainers of conda put together packages for the most recent versions of Python as they get released, but sometimes there may be a short lag.