# Using Git

# Introduction: What is git?
Git is a version control system - it enables you to control the various versions of projects, such as open source projects.


It lets you keep track of changes to an open
source project, and helps ensure every contributor is working on the same
codebase.
Git is a tool that makes it easy to contribute to projects that other people are
working on. The project code lives in a central _remote repository_, traditionally called 
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

# Lecture and Demos

## How do you get started?

### Introduce yourself to git

When you contribute to a project, you'll want your name on it. The following
lets git get to know you:

```bash
git config --global user.name "<Your Name here>"
git config --global user.email "<your_email@domainname.com>"
```

**Note:** You'll only need to do this once on your computer.

### Clone a project
There's a project hosted on github, and you're ready to contribute. It's time to
clone the project, so you have a copy on your machine to do work on. We're
assuming you've already read the github\_overview, and have forked the project
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

**Note:** You'll do this one time for each project you want to work on.

### Contribute to a project
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

## Common Operations

### Adding
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

## Committing
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


### Pushing

The `commit` command saves your changes locally, but they are not yet changed on the server. To push your changes up to GitHub, you use the `git push` command:

```bash
git push origin master
```

This can be condensed to `git push` if you are pushing to `origin` (the conventional name for your primary repo) on the current branch (in this case `master`).


### Branching and Merging

With larger projects, it is very common to *branch* and *merge* when you make changes. You've seen references to `master` above, this is the name used by convention for the default branch. A typical enhancement would be done by:

1. branching from master (so you have a separate workspace to work in)
1. doing your work as a series of `git add`, `git commit` cycles as described above
1. merging your changes back to master

By following this pattern, you keep your work isolated from the work of others until it is ready for others to see.

A typical iteration of creating a feature would look like this:

```bash
git checkout -b my-feature-name  # this creates the branch
# <do some work in my editor or IDE>
git add .
git commit -m 'my first bit of work'
# <do more work in my editor or IDE>
git add .
git commit -m 'my second bit of work'
git checkout master
git merge my-feature-name
git push origin master
```

The history created by the above steps would look something like this:

<img src="http://sentheon.com/images/27052016_branches.png">

`iss53` is the name of the branch being worked on, `C3` and `C5` are the changes that were committed on the branch, and `C4` is a change made by someone else during that same timeframe.

# Hands-on

Here you will create a repo locally and make some changes.

##### Create a repo locally

    cd ~
    mkdir my-project-name
    git init

##### Make a branch for your changes

    git checkout -b feature/my-change-name

**Note:** replace "my-change-name" with the name of the feature you are adding.

##### Make your changes

Open your favorite editor or IDE and make the changes desired.

##### Commit your changes

    git add .
    git commit -m 'added my new feature'

##### Merge your changes into the master branch

    git checkout master
    git merge feature/my-change-name

##### Delete your feature branch

    git branch -d feature/my-change-name


# Resources
To learn more about git, try these resources:

## Documentation and Books:

[Pro-Git](https://git-scm.com/book/en/v2), a free online resource (and in [PDF](https://progit2.s3.amazonaws.com/en/2016-03-22-f3531/progit-en.1084.pdf) form to save to your computer) with comprehensive documentation about using git well by Scott Chacon and Ben Straub

[User Manual](https://git-scm.com/docs/user-manual.html)

## Tutorials and videos:
[Interactive Tutorial](https://try.github.io/levels/1/challenges/1)

[A Successful Git Branching Model](http://nvie.com/posts/a-successful-git-branching-model/), which describes the branching model used by a variety of large and small projects; some projects do this differently, but the basic ideas are common with all of them

[Written Tutorial](https://git-scm.com/docs/gittutorial)

[Videos](https://git-scm.com/videos)

## Reference Manuals:
[Official Reference Manual](https://git-scm.com/docs)

[Git cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)
