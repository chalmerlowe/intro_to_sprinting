# Virtual Environments
Virtual environments enable you to create standalone environments for your project so that you can avoid conflicts between one project and another in terms of Python versions as well as the versions of other libraries that your project might depend upon.

# Objectives
Through participating in this session, attendees will be able to:
* Identify what a virtual environment is AND when using a virtual environment is a suitable solution to a task
* Create a virtual enviroment
* Populate a virtual environment with the software necessary to complete a programming/development task

# What is a virtual environment?
Virtual environments (virtualenv) are tools used to keep projects separate, especially in terms of keeping different Python versions separate and different library versions separate. Use of virtual environments helps to keep your global site packages organized and uncluttered AND prevents problems that arise when one project need version x.x of a library but another project needs version y.y of the same library.

# When should we use a virtual environment?
Many programmers use virtual environments for all but the most trivial programming tasks. Especially for beginners, tackling this early on builds a valuable skill AND helps eliminate sneaky bugs related to version discrepancies that can be hard to diagnose.

# How do you create a virtual environment?
The exact method may vary depending on your system and version of Python. See the Resources section for links to resources that can provide additional guidance. But for our purposes, we will use a tool package created by Continuum Analytics called miniconda ([download here](https://conda.pydata.org/miniconda.html)).

Miniconda allows you to make virtual enviroments as well as provides easy access to all the benefits you get from the heavyweight tool Anaconda.

Once you have miniconda (or Anaconda) installed, the general workflow for creating a virtual environment called 'mycalc' for our calculator program goes something like this:

```python
conda create -n mycalc python=3
```

# How do you populate it with the right software versions and libraries?
Once you have created a virtualenv you need to activate it AND then populate it with software.

## Activating your virtualenv
### Linux\Mac OSX version
```bash
$ source activate mycalc
```

### Windows version
```bat
rem typical windows
C:\> activate mycalc
```

## adding software
To add software to the virtualenv, you can use a tool call pip, which comes by default in modern versions of Python. For example, to install IPython, you can use the following command:

```
pip install ipython
```

# How do you get out of the virtual environment when you are done?
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

# Resources: Where can I learn more?

[Conda Docs](http://conda.pydata.org/docs/get-started.html)
