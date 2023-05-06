<!-- begin auto-generated title section -->
# Branching and Merging
<!-- end auto-generated section -->


## Time-box

12 Minutes

## Overview

With larger projects, it is very common to create **branches** and then **merge** the branches into the project's main branch when finalize your changes. You've seen references to `main` in earlier lessons. `main` is the default branch (you may also see primary or default branches referred to as `master` in legacy projects). A typical enhancement would be done by:

1. creating a branch (so you have a separate workspace to work in) using `git switch --create <branch name>`
1. doing your work as a series of `git add` and `git commit` cycles to the branch
1. merging your changes with `main`
1. submitting a pull request to the project owner (covered in a separate discussion)

By following this pattern of using branches to develop your changes and then merging into `main`, you can keep your work isolated from the rest of the project until it is ready to be shared or incorporated. Examples include:

* creating new features
* experimenting with changes to the code
* fixing bugs

Branches should be small and self-contained so that they can be merged easily. Sprawling and convoluted changes to code can make it nearly impossible to merge changes. In addition, it is customary for branches to be focused on specific problems, i.e., one bug fix per branch OR one new feature per branch.

## What to do

Do the following steps to get a feel for a typical iteration of creating a feature (sometimes called a `feature branch`):

**Create a new branch** & cause `git` to begin tracking changes in that branch

```bash
$ git switch --create appleseed-feature     # "--create", or "-c", creates a new branch named "appleseed-feature"
```

**Do work/edit files**

In your editor or IDE ... change the 23rd line in the file "jabberwocky.txt".

**`git add`** changes to the staging area ...

```bash
$ git add jabberwocky.txt
$ git commit -m "my first bit of work"
```

**Continue editing if desired** ...

If you want, you can continue to make changes to the same file OR other files...

**`git add`** these new changes to the staging area ...

```bash
$ git add jabberwocky.txt
$ git commit -m "my second bit of work"
```

**Switch to the main branch** and prepare to merge all our changes with any other changes that have been accepted into the upstream codebase...

```bash
$ git switch main            # this switches/checks out the main branch and is the same as "git checkout main"
```

**Update our local copy** ... Before we try to merge our changes to main, let's update our local copy of the repo with any updates that might have occurred in the `upstream` version by using `git pull`.

```bash
$ git pull upstream main       # this pulls any upstream changes into your computer
```

> **NOTE:** This next step generally not necessary, but if *your* GitHub fork also has some changes not reflected in your local copy, you should update the local copy by pulling in those changes as well. How could this happen, you ask? If you directly edit content on your GitHub fork in the browser OR if you (via a separate account) or someone else have applied changes to your GitHub fork directly or via a Pull Request.

```bash
$ git pull origin main         # Generally not necessary, but this pulls
                               # any changes in *your* GitHub fork repo to your computer
```

**Merge local changes from main into our local copy of appleseed-feature** ... With the latest and greatest `upstream` (and/or `origin`) changes on your local machine, attempt to merge `main` with your local copy of `appleseed-feature`. We do this by checking out `appleseed-feature` and then merging it with any changes from `main`.

```bash
$ git switch appleseed-feature # again, the same as "git checkout appleseed-feature"
$ git merge main
```

Then we **`git push`** changes to our **GitHub repo** ... presuming a successful merge (don't worry we'll discuss what to do if the merge is not successful) you can now `git push` your changes to your **GitHub repo** (your changes do NOT go to upstream, yet...)

```bash
$ git push origin appleseed-feature
```

If you (and your partner, if you're working in pairs) are done, then you can put your green sticky up! This is how we know you're done. Feel free to read the following sections to learn more about some of steps you just completed.

![green sticky note](images/Sticky-Note-02-Green-300px.png)

## The big picture

Let's imagine that you are working on a project with multiple commits to the main branch and a single bug fix branch to fix Issue #53 called `iss53`. Commits `C3` and `C5` are the changes that were committed on the branch, and `C4` is a change made by someone else to the main branch during that same timeframe.

The history created by the above steps would look something like this:

<img src="https://git-scm.com/book/en/v2/book/03-git-branching/images/basic-merging-2.png">

**Source:** https://git-scm.com/book/en/v2/book/03-git-branching/images/basic-merging-2.png

Following this workflow allows you to potentially work on multiple features or bugs and yet still maintain a clean, reliable and working set of code at all times.

## Deep dive

### Make a change in a branch

Besides `git add`, `git commit`, `git push`, a next logical step in preparing to contribute to open source projects is to grow familiar with using the **branch-work-merge** workflow to isolate your work from changes made by others.

### Create a branch

**Note:** replace "appleseed-feature" with the name of the feature you are adding. The `git switch` command allows you to change to a new branch. If that branch does not exist yet, it can be created with the `--create` (the same as `-c`) option.

```bash
$ git switch -c appleseed-feature
```

What makes a good branch name? What are the rules for naming branches? This is a short list of rules (for a complete list, see the [git man pages](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/git-check-ref-format.html).

* They cannot have two consecutive dots `..` anywhere
* They cannot contain a `\`
* They cannot be the single character `@`
* They cannot begin or end with a slash `/`
* They cannot have question-mark `?`, asterisk `*`, or open bracket `[` anywhere
* They cannot have ASCII control characters (`\t`, `\n`), `space`, tilde `~`, caret `^`, or colon `:` anywhere

### Make your changes

The whole point of creating a branch is to create a safe place to modify a specific portion of the code. With a `git branch` created, it is safe to edit your files, before proceeding with the remaining steps below.

### Stage and commit your changes

As previously described, once you are satisifed with your changes, they must be staged and then committed.

```bash
$ git add johnny_appleseed.txt
$ git commit -m "added edits to johnny's history"
```

### Merge your changes into the main branch

As noted above, `git switch` allows you to change to an alternate branch. The `main` branch is created by default by `git` and is often used as the primary branch for release. To change back to the `main` branch, use `git switch main`. Often others may be working on the same codebase and some of those changes may impact your codebase, so it is critical to collect all of those changes (i.e. download them from the `upstream` repository) for comparison to your code, using `git pull`.

For now, we will presume that there are no conflicts between your changes and other changes. With that premise in mind, you can merge your code and your local copy of the `upstream` repo.

```bash
$ git switch main
$ git pull
$ git switch appleseed-feature
$ git merge main
```

If you have any conflicts, you will need to address them. GitHub has a simple resource describing how to [resolve conflicts](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/). A full discussion of conflict resolution is beyond the scope of this lesson.

Presuming there are no merge conflicts we next **`git push`** changes to our **GitHub repo** ... 
Remember, the changes go to your **GitHub repo** (your changes do NOT go to upstream, YET...)

```bash
$ git push origin appleseed-feature
```

## Resources

* [Git Branching - Branches in a Nutshell](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
* [Git Branching - Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
* [Advanced Git](https://youtu.be/4EOZvow1mk4) - a great talk about some commands that will make working with multiple branches easier

<!-- begin auto-generated nav-links section -->
| Previous                                            |               Up               |                                        Next |
| :-------------------------------------------------- | :----------------------------: | ------------------------------------------: |
| [Git Common Operations](./git_common_operations.md) | [Using Git](./git_overview.md) | [Merge Conflicts](./git_merge_conflicts.md) |
<!-- end auto-generated section -->
