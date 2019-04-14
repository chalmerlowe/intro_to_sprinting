<!-- begin auto-generated title section -->
# Git Concepts
<!-- end auto-generated section -->


## Time-box

15 Minutes


## Overview

Git repositories can seem sophisticated, but at the lowest level, they are fairly simple: Git tracks changes to files in a special database AND categorizes those files. For our purposes, we will compare each categorization to an analogy in the following ways:

||Category|Analogy|
|:---|:----|:----|
|1.|Local directory|Local warehouse (typically cloned from a remote warehouse)|
|2.|Staging area|Pallet|
|3.|Commit|Truck|
|4.|Remote|Remote warehouse shared by all (typically called "origin")|

As we look at each of these, we will imagine that we are processing materials in a warehouse and shipping them to another warehouse location.

## What to do

Take a break, listen, enjoy the show

: )


## The big picture

[Jessica Kerr](https://github.com/jessitron) gave a great talk using this analogy, you can watch it here:

[![Git Happens Thumbnail](https://i.imgur.com/K38FXnG.png)](https://www.youtube.com/watch?v=yCh6TSLIQBQ)

You can reach this video, here: [Git Happens](https://www.youtube.com/watch?v=yCh6TSLIQBQ).

## Deep dive

As noted above, Git tracks changes to files in a database AND categorizes files in the following ways:

||Category|Analogy|
|:---|:----|:----|
|1.|Local directory|Local warehouse (typically cloned from a remote warehouse)|
|2.|Staging area|Pallet|
|3.|Commit|Truck|
|4.|Remote|Remote warehouse shared by all (typically called "origin")|

### Local directory

The **local directory** is simply the directory on your computer and it contains all your files, drafts, completed work, incomplete work, tools, etc. This material is uniquely yours. We can consider this to be the local warehouse in our example.

Just like in a real warehouse, there are a wide variety of materials:

* the products that you are storing/selling (this would be your project files)
* some items that are needed to run the warehouse, but aren't part of what you sell (this might be utilities and tools you created to help clean up your work, autogenerate content, configure your compilation environment, etc)
* there might be some items that still need to processed before you can sell them (files that are a work in progress, currently being edited, etc)

NOTE: Any new files you create in your local directory will only be visible to you, until you process them (more on that as we go).

NOTE: Local directories are often produced via a `git clone` command and based on a remote repository.

![staging](images/basic_dir.png)

### Staging area

The **staging area** holds all the files that are ready to be added to the project and eventually shared with others. The staging area can be compared to the pallet in our example. Everything that is 'done' and ready to be loaded on the truck gets placed on the pallet. To put a file into the staging area (i.e. add it to the pallet), you will use the `git add` command. Just like a pallet, you can continue to add files to the staging area, essentially indefinitely. While things are still in the staging area (on the pallet), it is fairly easy to add more files, remove files, change files, etc.

![staging](images/git_staging.png)

**NOTE**: if you add a file to the staging area and **THEN** make additional changes to the file, the newest changes will **not** be staged. Staging takes a snapshot in time. You will need to `git add` the file a second time to capture the newest changes.

### Commit

The **commit area** holds all the changes that you are going to release to the remote warehouse. The commit area can be compared to the truck in our example. Once your pallet is full and ready to go, you load it onto the truck for delivery. Everything that is ready to be shipped goes into the commit area (i.e. gets loaded on the truck). To commit a file, you will use the `git commit` command.

![commiting](images/git_commit.png)

**NOTE**: much like we saw above... if you add a file to the commit area and **THEN** make additional changes to the file, the newest changes will **not** be staged OR committed. Committing also takes a snapshot in time. You will need to `git add` the file a second time to stage it and then `git commmit` it to capture the newest changes.

### Remote

A **remote** is a repository other than the local copy on your computer; this is typically stored somewhere like GitHub but can be just about anywhere (i.e. on a server within your company OR an alternative to GitHub, like BitBucket OR GitLab).

Remotes are named, and the default name for the remote you `git clone` from is typically **origin**.

Another remote name you will hear often if you're submitting code to other people's projects is **upstream**, which usually refers to the original project you `fork` from.

Nothing gets copied from your local system until you `git push` it to a remote repository. Only items that have been committed are pushed to the remote. Pushing to `origin` (the default remote when you clone from GitHub, for example) can be compared to the truck driving away to deliver the pallet. Once changes have been pushed, they are published and others can see those changes in **your Github** repository.

![git push](images/git_push.png)

**NOTE:** we're not yet thinking about how to get your changes back to the original project; that will be covered later. At this point, all these efforts have been focused on repos that you control.

## Resources

### Documentation and Books:

[Pro-Git](https://git-scm.com/book/en/v2), a free online resource (available in [PDF format](https://progit2.s3.amazonaws.com/en/2016-03-22-f3531/progit-en.1084.pdf).) with comprehensive documentation about using Git efficiently by Scott Chacon and Ben Straub

[User Manual](https://git-scm.com/docs/user-manual.html)

### Tutorials and videos:

[Interactive Tutorial](https://try.github.io/levels/1/challenges/1)

[A Successful Git Branching Model](http://nvie.com/posts/a-successful-git-branching-model/), which describes the branching model used by a variety of large and small projects; some projects do this differently, but the basic ideas are common with all of them

[Written Tutorial](https://git-scm.com/docs/gittutorial)

[Git Happens](https://youtu.be/yCh6TSLIQBQ) video by Jessitron (Jessica Kerr) that uses the warehouse analogy to help clarify directory, staging, commit

[Video collection](https://git-scm.com/videos)

[50/72 rule for git commit messages](http://stackoverflow.com/questions/2290016/git-commit-messages-50-72-formatting) How to format git commit messages efficiently

### Reference Manuals:

[Official Reference Manual](https://git-scm.com/docs)

[Git cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)

<!-- begin auto-generated nav-links section -->
| Previous | Up | Next |
|:---------|:---:|-----:|
| [Using Git](./git_overview.md) | [Using Git](./git_overview.md) | [Cloning a Repository](./git_cloning.md) |
<!-- end auto-generated section -->
