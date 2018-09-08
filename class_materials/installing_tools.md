<!-- begin auto-generated title section -->
# Installing the Software You'll Need
<!-- end auto-generated section -->


## Time-box

15 Minutes


## Overview

Collaborating on sprints generally requires the use of software tools to truly be effective and efficient. For this workshop, we will focus on using `git`, and there is follow-on material on setting up additional tooling you'll use for different kinds of projects.

### Objectives

* Download the tools
* Install the tools
* Test for successful installation
* Review the purpose of the tools

## What to do

### Step One: Download and Install `git`

First check to see if `git` is already installed on your computer.

Open a command prompt/terminal and type `git`

You'll see one of these two things.

- **A whole bunch of text**, which is a document explaining some of the most common `git` commands. If you see this, jump to the instructions on [downloading and installing Conda.](#download-and-install-conda) because git is already installed.

- `git: Command not found.` This is good! It means that you **are going to follow our instructions to install git!** Keep reading.

#### <img src="images/windows_icon.jpg" width="24" height="24"> Windows 

1. Download the [git installer](https://git-scm.com/downloads) (**NOTE:** If you are unsure if you need the 32 or 64-bit version, you can [follow these steps](https://support.microsoft.com/en-us/help/15056/windows-7-32-64-bit-faq))

3. Run the .exe file that you downloaded and follow the instructions.

#### <img src = "images/mac_icon.png" width="24" height="24"> Mac OS 

1. Download the [git installer](https://git-scm.com/downloads)

2. Open the .dmg file that you downloaded. Run the installer inside and follow the instructions.

##### Alternately, install using homebrew

Many Mac users use [homebrew](http://brew.sh/) to install programs.

```bash
brew install git
```

#### <img src = "images/linux_icon.jpg" width="24" height="24"> Linux 

If you are running Linux, there is a good chance that you already have `git` installed. If it isn't, install it by typing one of these commands into your command prompt.

**Red Hat-based** systems (Red Hat, Centos, Fedora) use:

```bash
$ sudo yum install git-all
```

**Debian-based** systems (Ubuntu, Debian) use:

```bash
$ sudo apt-get install git-all
```

### Step Two: Confirm your `git` install

In a command prompt type `git config`. If `git` is installed properly, you will see text explaining some of the common configuration options for `git`.

### Troubleshooting

Here's a list of error messages & how to fix them.

- `git config: Command not found.` This means you need to quit & relaunch your terminal. If that doesn't fix it, ask for help. ([Details here.](https://unix.stackexchange.com/questions/86012/what-is-the-purpose-of-the-hash-command))

## Done with commands for now!

If you (if you're working in pairs, you and your partner) are done, then now you can put your green sticky up! This is how we know you're done with the commands.

![green sticky note](images/Sticky-Note-02-Green-300px.png)

If you like reading, you can also keep reading this page.

## The big picture

### What is `git` and why did we install it?

`git` is a distributed version control system for managing files. It allows multiple people to work on collections of files (usually source code) and then easily *merge* other's work so everyone can have the most up to date version of the project. A later lesson will provide more details on `git`.

## Resources

* [Pro Git](https://git-scm.com/book/en/v2): also called "The Git Book", Pro Git is the authoritative book on doing everything that Git can do. It can be read online and also downloaded in many formats so you can read it anywhere.

<!-- begin auto-generated nav-links section -->
| Previous | Up | Next |
|:---------|:---:|-----:|
| [Environment Set-up](./environment_overview.md) | [Environment Set-up](./environment_overview.md) | [Setting up GitHub and Forking a Repository](./github_setup.md) |
<!-- end auto-generated section -->
