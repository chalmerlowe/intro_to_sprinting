<!-- begin auto-generated title section --><!-- end auto-generated section -->

## Time-box

<XX> Minutes

## Overview

THIS FILE IS A WORK IN PROGRESS...

When working on open source projects, it is customary to work with others on a project, which means that we will need to incorporate their changes into our local repositories. 

If their changes are completely different from any changes we have made (i.e. if they modify File A, while we modify File B), then there should be no conflicts and it should be fairly trivial to merge the changes.  

If their changes are in the same file that we changed, but are in completely separate portions of the file, we can often merge without conflict.

But if our changes are in the same file and are too similar to each other or overlap, it becomes difficult for git to automagically merge our changes. In those cases, git will turn over the merge process to us, to do manually.

## What to do

<steps to execute go here, no details, just raw steps>

* create and switch to a new branch
* choose a text file that is both present in your fork and on your local repo
* edit that file on GitHub (click the pencil button, make changes, and save)
* edit that same file in your local repo. Change the same line(s) in both files to say something different in each case.
* in your local repo, git add, commit.
* switch to master
* git pull from master
* git merge your branch
* You will see an error message.
* Open the file with 

## The big picture

<high-level concepts that can be described in a few mintues>

## Deep dive

<detailed explanations go here, with h3/h4 subsecitons if necessary>

## Resources

* [Git Branching - Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)


<!-- begin auto-generated nav-links section --><!-- end auto-generated section -->
