# Using Git
Git is a version control system - it let's you keep track of changes to an open
source project, and helps ensure every contributor is working on the same
codebase.

# Objectives
Through participating in this session, attendees will be able to:
* Understand why git is used in an open source project
* Use basic git commands to contribute to a project

# What is git?
Git is a tool that makes it easy to contribute to projects that other people are
working on. The project code lives in a central _remote repository_, called the 
`origin`. Programmers pull the project into their own _local repository_,
where they can work on adding features and squashing bugs. When finished, they
push the code back into `origin`, for other contributers to see and pull from.

# How do you get started?
## Introduce yourself to git
When you contribute to a project, you'll want your name on it. The following
let's git get to know you:
```bash
git config --global user.name "<Your Name here>"
git config --global user.email "<your_email@domainname.com>"
```

## Clone a project
There's a project hosted on github, and you're ready to contribute. It's time to
clone the project, so you have a copy on your machine to do work on. We're
assuming you've already read the github\_overview, and have forked your project
into your own repository. First, use:
```bash
git clone git@github.com:<your_username>/<the_project>
<destination/directory/path>
```
A folder was created, and should be full of project files. Git will
automatically set up `origin` as a _remote_, which points to your fork of the
repository. Inform git where to find the upstream repository (the repo that your
fork was forked from) with:
```bash
git remote add upstream <main repo>
```
See that everything is in order with:
```bash
git remote -v
```

## Contribute to a project
After cloning the code from your fork you are free to create and expand upon the
project. Once you have completed something sizeable, be it a feature, function,
or documentation, it is time to commit. First off we are going to have to add all
the files that you chanegd with:
```bash
git add <file1> <file2>...
```
After adding the files you chnaged it is time to add a description to what you
changed in these files with:
```bash
git commit -m "Description of changes"
```
Lastly, you are going to have to send the commit to Github or another Source Code
Manager with:
```bash
git push origin master
```
After pushing to your fork you will have to go and create a pull request, which is
explained in the github\_overview.

## Addtional Information
# Links
For more interesting information about git check out the [docs](https://git-scm.com/)
