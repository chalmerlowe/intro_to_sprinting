# Cloning a Repository


## Time-box

<XX> Minutes


## Overview

With a copy of the project in your Github repository, it's time to clone the project to your local computer, so you have a local copy on your machine to do work on.


## What to do

Make sure you are in your project directory, if you are not there already.

```bash
$ cd /path/to/my/dev/directory
```

Use the `clone` command to clone a copy of the repository to your directory, using `git`.

**Note:** *ENSURE* that you change `<your_username>` to the name of *your* account.
```
$ git clone https://github.com/<your_username>/intro_to_sprinting_codeless_project.git
$ cd intro_to_sprinting_codeless_project
$ git remote add upstream https://github.com/chalmerlowe/intro_to_sprinting_codeless_project.git
```




## The big picture

Before you can start adding to a project, you will need to clone the project to your local computer in your local working directory.

![cloning](images/git.png)


## Deep dive

It's time to clone the project, so you have a copy on your machine to do work on.

Enter the following command on the command line, **ENSURE that you change `<your_username>`** to the name of your account:

```bash
$ cd /path/to/my/dev/directory
$ git clone https://github.com/<your_username>/intro_to_sprinting_codeless_project.git
$ cd intro_to_sprinting_codeless_project
```

This command creates a folder, which should be full of project files. Git will automatically set up `origin` as a **remote** repository, which points to **your** fork of the repository.

```bash
$ git remote -v
origin  https://github.com/myusername/intro_to_sprinting_codeless_project (fetch)
origin  https://github.com/myusername/intro_to_sprinting_codeless_project (push)
```

Next we inform git of where to find the upstream repository (the repo that your fork was forked from) using the following command:

```bash
$ git remote add upstream https://github.com/chalmerlowe/intro_to_sprinting_codeless_project.git
```

Confirm that git has stored the correct upstream repository with this command:

```bash
$ git remote -v
origin   https://github.com/myusername/intro_to_sprinting_codeless_project (fetch)
origin   https://github.com/myusername/intro_to_sprinting_codeless_project (push)
upstream https://github.com/chalmerlowe/intro_to_sprinting_codeless_project (fetch)
```

**Note:** You'll do this **one time for each project** you want to work on.


## Resources

* [<resource name>](<resource url>)
* [<resource name>](<resource url>)


| Previous | Up | Next |
|:---------|:---:|-----:|
| [Git Concepts](./git_concepts.md) | [Using Git](./git_overview.md) | [Git Primary Workflow: Add, Commit, Push](./git_main_lifecycle.md) |
