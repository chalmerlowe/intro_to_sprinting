# Using Git

## TODOS:
[ ] decide on an overall format for each lesson and ensure that each lesson matches that format:  

* [ ] intro to the lessons  
* [ ] objectives  
* [ ] lecture/demos  
* [ ] hands-on  
* [ ] resources 

# What is git?
Git is a version control system - it enables you to control the various versions of projects, such as open source projects.


it let's you keep track of changes to an open
source project, and helps ensure every contributor is working on the same
codebase.
Git is a tool that makes it easy to contribute to projects that other people are
working on. The project code lives in a central _remote repository_, called the 
`origin`. Programmers pull the project into their own _local repository_,
where they can work on adding features and squashing bugs. When finished, they
push the code back into `origin`, for other contributers to see and pull from.


# Objectives
Through participating in this session, attendees will be able to:

* Understand why git is used in an open source project
* Use basic git commands to:
    * configure git for use
    * get a copy of an open source project
    * save modifications/additions/deletions to the project
    * submit those changes to the project
    * incorporate other's changes to the project 
    * verify the status of the project repository
    * basic troubleshooting

NOTE: this will be a hands-on overview of git. It is incredibly powerful with many options and capabilities. The goal is to get you started with git, not make you into an expert.



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
# Adding
There are couple tricks that makes adding files to a commit a little bit easier
if you pay attention to what you are doing. For instance you can add all of the
changed files to your commit with:
```bash
git add *
```
This can lead to problems if you add files that aren't related to the commit at
to protect against this you can view which files have pending changes before you
add them with:
```bash
git status
```

# Committing
The method taugt above works fine, but there are additional flags and paramters
that can make for a better commit. First of all if you would like to add a more
in depth description you can use:
```bash
git commit
```
It will bring you into a command line text editor like vim or emacs where the
first line serves as the title and if you add a blank line and begin typeing more
you can add the mentioned details.

Another feature related to that, which ties in with open source spriting is if you
enter
```bash
git commit -s
```
It will bring of the same prompt as before but with a `Signed off by:` section 
with your name after it giving the rights to your code to whomever you committed
it to.


# Links
For more interesting information about git check out the [docs](https://git-scm.com/)
