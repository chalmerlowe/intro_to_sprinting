# Tools for Sprinting
Collaborating on sprints is fun and effective when people have tools that make them powerful and efficient. `git` and `miniconda` are the tools we will use to practice a sprint. 

# Quick download links

Download the git installer for:

* [Windows](https://git-scm.com/download/windows)
* [Mac](https://git-scm.com/download/mac)
* [Linux](https://git-scm.com/download/linux)

Download the miniconda installer (Python 3.5, 64-bit): 

* [Windows](https://repo.continuum.io/miniconda/Miniconda3-latest-Windows-x86_64.exe)
* [Mac](https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh)
* [Linux](https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh)

# Objectives
Through participating in this session, attendees will be able to:

* Download the tools that we will use for a test project
* Install and test the tools to ensure that they are installed properly
* Run a short series of commands that will demonstrate something useful with the tool 

# Git 

## What is git?
Git is a distrubuted version control system for managing files. It allows multiple people to work on collections of files (usually source code) and then easily *merge* other's work so everyone can have the most up to date version of the project. 

## Installing git
First check to see if git is already installed on your computer.

Open a command prompt and type `git`

If git is installed, you will see a terse help document explaining some of the most common git commands.

If git is not installed your command prompt will tell you. Follow the instructions below for your OS. 

### Windows

Download the [git installer](https://git-scm.com/download/windows) if you don't have it.

If you are unsure if you need the 32 or 64-bit version, you can [follow these steps](https://support.microsoft.com/en-us/help/15056/windows-7-32-64-bit-faq)

Run the .exe file that you downloaded and follow the instructions.

### Mac OS

Download the [git installer](https://git-scm.com/download/mac)  if you don't have it.

Open the .dmg file that you downloaded. Run the installer inside and follow the instructions.

### Linux

There is a good chance that you already have git installed. If it isn't, install it by typing one of these commands into your command prompt.

Red Hat based systems (Red Hat, centos, fedora) use:

```bash
$ sudo yum install git-all
```
Debian based systems (Ubuntu, debian) use:

```bash
$ sudo apt-get install git-all
```

## Testing Git
In a command prompt type `git config`. If git is installed you will see text explaining some of the common configuration options for git.

## Hands-on Git
In a command prompt complete the following steps. Your results should look similar to what is shown.

### Windows
TODO

### OS X and Linux
Create an empty folder named `sprint` and `cd` into it.

```bash
$ mkdir sprint 
$ cd sprint
```

Type `git init`


```bash
$ git init
Initialized empty Git repository in /Some/Path/sprint/.git/
```
Type `echo "new file" > handson.txt` This will create a tiny text file in sprint/.

```bash
$ echo "new file" > handson.txt
```

Type `git status` This will show you that git is aware of a new file in your project. It gives you a hint for what to do next.

```bash
$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

  handson.txt

nothing added to commit but untracked files present (use "git add" to track)
```

So try it. Type `git add handson.txt`

```bash
$ git add handson.txt
```

Type `git status` Git will tell you that it will be keeping track of changes to your handson.txt file.

```bash
$ git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

  new file:   handson.txt
```

Type `git commit -m'a new commit'` This will tell git to store a copy of this file in your repository. 

```bash
$ git commit -m'a new commit'
[master (root-commit) a69c665] a new commit
 1 file changed, 1 insertion(+)
 create mode 100644 handson.txt
```
Great work! You just created a git repository and commited your first file.


## Git Resources: Where can I learn more?

* [Git Immersion](http://gitimmersion.com/index.html)


# Miniconda
## What is miniconda?
Miniconda is a tool that installs and manages different versions of Python and optional libraries. It's a good idea to maintain a seperate environmenmt for each project you work on. We will give a deeper explanation in a later session.


## Installing miniconda
Follow the instructions for your operating system in the [miniconda quickstart guide](http://conda.pydata.org/docs/install/quick.html)

* [Windows](http://conda.pydata.org/docs/install/quick.html#windows-miniconda-install)
* [OS X](http://conda.pydata.org/docs/install/quick.html#os-x-miniconda-install)
* [Linux](http://conda.pydata.org/docs/install/quick.html#linux-miniconda-install)


## Testing miniconda
Let's check that both git and miniconda are installed and working.

In a command prompt type `conda env list`. You should see something similar this.

```bash
$ conda env list
# conda environments:
#
root                  *  /Users/jeff/miniconda3
```

## Hands-on miniconda

### Linux version
```bash
# typical linux
(mycalc) $ deactivate
```

### Windows version
```bat
rem typical windows
(mycalc) C:\> deactivate
```

## Miniconda Resources: Where can I learn more?

[Using conda](http://conda.pydata.org/docs/using/index.html)




