# Installing the Software You'll Need


## Time-box

15 Minutes


## Overview

Collaborating on sprints generally requires the use of software tools to truly be effective and efficient. For this workshop, we will use `git` and `miniconda (conda)` to practice our skills. 

### Objectives

* Download the tools
* Install the tools
* Test for successful installation
* Review the purpose of the tools

## What to do

### Download and Install `git`

First check to see if `git` is already installed on your computer.

Open a command prompt/terminal and type `git`

You'll see one of these two things.

- `git: Command not found.` This is good! It means that you **are going to follow our instructions to install git!** Keep reading.

- **A whole bunch of text**, which is a document explaining some of the most common `git` commands. If you see this, jump to the instructions on [downloading and installing Conda.](#download-and-install-conda) because git is already installed.


#### Windows

1. Download the [git installer](https://git-scm.com/downloads) (**NOTE:** If you are unsure if you need the 32 or 64-bit version, you can [follow these steps](https://support.microsoft.com/en-us/help/15056/windows-7-32-64-bit-faq))

3. Run the .exe file that you downloaded and follow the instructions.

#### Mac OS

1. Download the [git installer](https://git-scm.com/downloads)

2. Open the .dmg file that you downloaded. Run the installer inside and follow the instructions.

##### Alternately, install using homebrew

Many Mac users use [homebrew](http://brew.sh/) to install programs.

```bash
brew install git
```

#### Linux

If you are running Linux, there is a good chance that you already have `git` installed. If it isn't, install it by typing one of these commands into your command prompt.

**Red Hat-based** systems (Red Hat, Centos, Fedora) use:

```bash
$ sudo yum install git-all
```

**Debian-based** systems (Ubuntu, Debian) use:

```bash
$ sudo apt-get install git-all
```

### Confirm your `git` install

In a command prompt type `git config`. If `git` is installed properly, you will see text explaining some of the common configuration options for `git`.

### Download and Install `conda`

Follow the instructions for your operating system in the [miniconda quickstart guide](http://conda.pydata.org/docs/install/quick.html). Use a **Python 3** version of conda.

### Confirm your `conda` install

In a command prompt type `conda list`. If `conda` is installed properly, you will see a summary of the packages installed by `conda`.

### Troubleshooting

Here's a list of error messages & how to fix them.

- `conda: Command not found.` This means you need to quit & relaunch your terminal. If that doesn't fix it, ask for help. ([Details here.](https://unix.stackexchange.com/questions/86012/what-is-the-purpose-of-the-hash-command))

## Done with commands for now!

If you (if you're working in pairs, you and your partner) are done, then now you can put your green sticky up! This is how we know you're done with the commands.

![green sticky note](images/Sticky-Note-02-Green-300px.png)

If you like reading, you can also keep reading this page.

## The big picture

### What is `git` and why did we install it?

`git` is a distributed version control system for managing files. It allows multiple people to work on collections of files (usually source code) and then easily *merge* other's work so everyone can have the most up to date version of the project. A later lesson will provide more details on `git`.

### What is miniconda (`conda`) and why did we install it?

Miniconda contains the `conda` package manager and `Python`. `conda` is language agnostic, so you can also use it to support delivering this workshop with programming languages besides `Python`. Once miniconda is installed, you will be able to: 

* create virtual environments and 
* manage separate installations of `Python` 
* manage a large number of Python packages/libraries

Whenever you work on a new project, you should create a separate environment for that project. `conda` lets you do this easily and efficiently. A later lesson will provide more details on both virtual environments and the use of the `conda` package manager.

**NOTE** For this tutorial, we'll use `conda`. There are other tools that accomplish similar goals and work in similar ways, such as `venv`, `pip`, and `virtualenv`. During PyCon Sprints, make sure to use whatever virtual environment tool your project maintainer suggests. See Resources for more info.

## Resources

* [Using conda](http://conda.pydata.org/docs/using/index.html): A tutorial on how to use `conda`

* [conda cheatsheet](https://conda.io/docs/_downloads/conda-cheatsheet.pdf): A cheatsheet of the most common `conda` commands

* [Python's `venv` and `virtualenv` can also create virtual environments.](http://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)

* [`pip` is Python's package manager.](https://en.wikipedia.org/wiki/Pip_(package_manager))


| Previous | Up | Next |
|:---------|:---:|-----:|
| [Environment Set-up](./environment_overview.md) | [Environment Set-up](./environment_overview.md) | [Setting up Virtual Environments](./virtual_environments.md) |
