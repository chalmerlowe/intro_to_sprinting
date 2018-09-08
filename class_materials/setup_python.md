<!-- begin auto-generated title section -->
# Setting up Virtual Environments
<!-- end auto-generated section -->


## Time-box

15 Minutes


## Overview

TBD

### Objectives

Through participating in this session, attendees will be able to:

* Identify what a virtual environment is AND when using a virtual environment is a suitable solution to a task
* Create a virtual environment
* Populate a virtual environment with the software necessary to complete a programming/development task


## What to do

TBD


## Done with commands for now!

If you (if you're working in pairs, you and your partner) are done, then now you can put your green sticky up! This is how we know you're done with the commands.

![green sticky note](images/Sticky-Note-02-Green-300px.png)

If you like reading, you can also keep reading this page.


## The big picture

TBD

## Deep dive

### What is a virtual environment?

As mentioned above, virtual environments (also called virtualenvs) are tools used to keep projects separate, especially in terms of keeping different software versions separate and different library versions separate. For example, virtualenvs prevent Python's site packages folder from getting filled with potentially conflicting versions of software AND thus prevents problems that arise when one project needs **version x.x** of a library but another project needs **version y.y** of the same library. At their core, virtualenvs are glorified directories that use scripts and metadata to organize and control the environment. You are allowed to have an essentially unlimited number of virtualenvs. And as you saw above, they are very easy to create using various command line tools, such as `conda`.

### When should we use a virtual environment?

Anytime you have more than one project and there is a possibility of conflicts between your libraries, it is a good time to use a virtualenv. Having said that, many programmers use virtual environments for **all but the most trivial** programming tasks. Especially for beginners, using virtualenvs early on in your learning career will build a valuable skill AND help prevent sneaky bugs related to version discrepancies. Bugs that can be hard to diagnose.

### How do you create a virtual environment?

TBD

## Resources

* [Installing packages using pip and virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/): A getting started guide on how to use Python's built-in `virtualenv` tool
* [pip instructions](https://docs.python.org/3/installing/): An overview of a Python-oriented package manager: Pip


## Footnotes

[1]: the maintainers of conda put together resources for the most recent versions of Python libraries as they get released, but sometimes there may be a short lag.

<!-- begin auto-generated nav-links section -->
| Previous | Up | Next |
|:---------|:---:|-----:|
| [Installing the Software You'll Need](./installing_tools.md) | [Environment Set-up](./environment_overview.md) | [Setting up GitHub and Forking a Repository](./github_setup.md) |
<!-- end auto-generated section -->
