<!-- begin auto-generated title section --><!-- end auto-generated section -->

Now that you have been through the demo and seen, heard and in some cases, tried each of the steps, let's put it all together and get you set up to work on the RPN Calculator project.

The details of the Project will be described in the next lesson. This lesson is more about getting your working environment set up, AND giving you a summary of the major commands, etc.

These steps purposely limit the explanation to highlight the major commands and steps. If you need some review on a given command, feel free to ask the mentors in the room OR to refer back to the main lecture/demo materials.

# Objectives

Through participating in this session, attendees will be able to:

* Prep their environment:  do all the preliminary steps necessary to:
    * setup a virtual environment specific to this project
    * activate the virtualenv
    * install the software required for the project in the virtualenv
    * fork the project to your GitHub repo
    * clone the project to your local directory
* Review the major steps performed when making changes
* Review the major steps when issuing a Pull Request

# Hands-on

## Make your virtual environment

The following steps will set up your system in preparation for the remaining lessons:

Follow the directions below, depending on your operating system.

### <img src = "images/linux_icon.jpg" width="24" height="24"><img src = "images/mac_icon.png" width="24" height="24">  Linux\Mac OSX version

1. `conda create -n rpncalc python=3`
1. `source activate rpncalc`
1. `conda install ipython`

### <img src="images/windows_icon.jpg" width="24" height="24"> Windows version

1. `conda create -n rpncalc python=3`
1. `activate rpncalc`
1. `conda install ipython`

## Fork the RPN Calculator project on GitHub

You will need to fork the calculator repo.

1. Navigate to this GitHub repo: [RPN Calculator](https://github.com/chalmerlowe/python-rpncalc-20170506)
2. Click on the **Fork** button to fork the repo to your GitHub account

## Clone the repo to your desktop

Clone a copy of your repo to your desktop:

```bash
$ git clone https://github.com/<your_username>/python-rpncalc-20170506.git
$ cd python-rpncalc-20170506
```

Add the upstream repo:

```bash
$ git remote add upstream https://github.com/chalmerlowe/python-rpncalc-20170506.git
```

Confirm that Git has stored the correct upstream repository with this command:

```bash
$ git remote -v
```

## Stage, Commit, Push

```bash
$ git checkout -b mybranch
```

Make wonderful, glorious changes to the project.

```bash
$ git add <file>
$ git commit -m "supremely concise, but explanatory message "
```

Continue the process of saving the world through code!

```bash
$ git add <file>
$ git commit -m "awesomely short, but descriptive message"
```

```bash
$ git checkout master
```

```bash
$ git merge
```

```bash
$ git push
```

## Pull Requests

Navigate via your browser to your GitHub account:

1. Click on "**New Pull Request**" button

You will be transferred to the original project GitHub Repo:

1. Click on "**Create pull request**" button
1. Add summary notes
1. Click on "**Create pull request**" button


<!-- begin auto-generated nav-links section --><!-- end auto-generated section -->
