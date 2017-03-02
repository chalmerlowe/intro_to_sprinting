# Tools for Sprinting
## TODO:
[ ] make sure that the lower-level objectives tie to the higher level objectives  
[ ] decide on an overall format for each lesson and ensure that each lesson matches that format:  

* [ ] intro to the lessons  
* [ ] objectives  
* [ ] lecture/demos  
* [ ] hands-on  
* [ ] resources  
[ ] Add navigation links? (previous lesson | next lesson) Do this for all pages.    

Collaborating on sprints generally requires the use of software tools to truly be effective and efficient. For this workshop, we will use `git` and `conda` to practice our skills. 

# Objectives
Through participating in this session, attendees will be able to:

* Download the tools that we will use for test project
* Install and test the tools to ensure that they are installed properly
* Run a short series of commands that will do something useful with the tool 

# What is git?
Git is a distrubuted version control system for managing files. It allows multiple people to work on collections of files (usually source code) and then easily *merge* other's work so everyone can have the most up to date version of the project. 

# What is miniconda?
Miniconda is a tool that installs and manages different versions of Python and optional libraries. It's a good idea to maintain a seperate environmenmt for each project you work on. We will give a deeper explanation in a later session.

# Installing git
First check to see if git is already installed on your computer.

Open a command prompt and type `git`

If git is installed, you will see a terse help document explaining some of the most common git commands.

If git is not installed your command prompt will tell you. Follow the instructions for your OS 

## Windows

Download the [git installer](https://git-scm.com/download/windows)

If you are unsure if you need the 32 or 64-bit version, you can [follow these steps](https://support.microsoft.com/en-us/help/15056/windows-7-32-64-bit-faq)

Run the .exe file that you downloaded and follow the instructions.

## Mac OS

Download the [git installer](https://git-scm.com/download/mac)

open the .dmg file that you downloaded. Run the installer inside and follow the instructions.

### Alternately, install using homebrew

Many Mac users use [homebrew](http://brew.sh/) to install programs.

```shell
brew install git
```

## Linux

There is a good chance that you already have git installed. If it isn't, install it by typing one of these commands into your command prompt.

Red Hat based systems (Red Hat, centos, fedora) use:
```bash
$ sudo yum install git-all
```
debian based systems (Ubuntu, debian) use:
```bash
$ sudo apt-get install git-all
```

# Installing miniconda
Follow the instructions in the [miniconda quickstart guide](http://conda.pydata.org/docs/install/quick.html#windows-miniconda-install)

* [Windows](http://conda.pydata.org/docs/install/quick.html#windows-miniconda-install)
* [OS X](http://conda.pydata.org/docs/install/quick.html#os-x-miniconda-install)
* [Linux](http://conda.pydata.org/docs/install/quick.html#linux-miniconda-install)


# Testing
Let's check that both git and miniconda are installed and working.

###Git
In a command prompt type `git config`. If git is installed you will see text explaining some of the common configuration options for git.

###Miniconda
In a command prompt type con


# HANDS-ON

##Git 



##Miniconda
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

# Resources: Where can I learn more?


[Using conda](http://conda.pydata.org/docs/using/index.html)




