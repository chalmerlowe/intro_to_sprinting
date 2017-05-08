# Branching and Merging

## Time-box

<XX> Minutes

## Overview

<put single paragraph here>

## What to do

<steps to execute go here, no details, just raw steps>

## The big picture

<high-level concepts that can be described in a few mintues>

## Deep dive

<detailed explanations go here, with h3/h4 subsecitons if necessary>

## Resources

* [<resource name>](<resource url>)
* [<resource name>](<resource url>)

| Previous | Up | Next |
|:---------|:---:|-----:|
| [Git Primary Workflow: Add, Commit, Push](./git_main_lifecycle.md) | [Using Git](./git_overview.md) | [Dealing with Merge Conflicts](./git_merge_conflicts.md) |




### Branching and Merging

With larger projects, it is very common to create **branches** and then **merge** the branch into the main project when you make changes. You've seen references to `master` above, the default branch. A typical enhancement would be done by:

1. creating a branch (so you have a separate workspace to work in) using `git checkout -b <branch name>`
1. doing your work as a series of `git add`, `git commit` cycles to the branch, as described above
1. merging your changes back into `master`

By following this pattern, you keep your work isolated from the rest of the project until it is ready to be released. Examples include:

* creating new features
* experimenting with changes to the code
* fixing bugs

Branches should be small and self-contained so that they can be merged. Sprawling and convoluted changes to code can make it nearly impossible to merge. In addition, it is customary for branches to be focused on specific problems: i.e. one bug fix per branch OR one new feature per branch.

A typical iteration of creating a feature (sometimes called a `feature branch`) would look like this:

```bash
$ git checkout -b my-feature-name     # "-b" creates a new branch named "my-feature-branch"
```

... do some work in my editor or IDE ...

```
$ git add .
$ git commit -m 'my first bit of work'
```

... do more work in my editor or IDE ...

```
$ git add .
$ git commit -m 'my second bit of work'
```

Once we are done, let's merge the feature branch back into the master branch

```
$ git checkout master     # this checks out the master branch   
$ git pull                # this pulls any remote changes into master           
$ git merge my-feature-name
$ git push origin master
```

Let's imagine that you are working on a project with multiple commits to the master branch and a single bug fix branch to fix Issue #53 called `iss53`. Commits `C3` and `C5` are the changes that were committed on the branch, and `C4` is a change made by someone else to the master branch during that same timeframe.

The history created by the above steps would look something like this:

<img src="http://sentheon.com/images/27052016_branches.png">
**Source**: http://sentheon.com/images/27052016_branches.png





## Make a change in a branch

As you get used to the above steps, the next step is to grow familiar with using the branch-work-merge flow to isolate your work from changes made by others.

### Create a branch

**Note:** replace "my\_change\_name" with the name of the feature you are adding.

```bash
$ git checkout -b feature/my_change_name
```

### Make your changes



When you are finished making changes, proceed with the remaining steps.

### Commit your changes

```bash
$ git add .
$ git commit -m 'added my new feature'
```

### Merge changes from master into your branch

Sometimes other people will make changes that impact the thing you were working on. It's easiest to catch this early by trying to merge **master** into your feature branch:

```bash
$ git merge master
```

If you have any conflicts, you will need to address them. GitHub has a simple resource for [resolving conflicts](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/). A full discussion of conflict resolution is beyond the scope of this lesson.

### Merge your changes into the master branch

```bash
$ git checkout master
$ git pull
$ git merge feature/my_change_name
```

### Delete your feature branch

When you are finished using a branch (i.e. all the pertinent changes have been merged into master), you can simply delete it:

```bash
$ git branch -d feature/my_change_name
```
