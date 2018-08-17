<!-- begin auto-generated title section -->
# Git Common Operations
<!-- end auto-generated section -->


## Time-box

10 Minutes


## Overview

Git has a number of capabilities to simplify your life, help you understand the status of your directory and improve your ability to communicate about your changes.

When using `git`, sometimes you want to know more about the changes you are committing ... this is where `git diff` comes in. 

## What to do

For this next exercise, we will change a single file and use the `git diff` tool to examine those specific changes in detail.

1. Use your text editor to open the `beowulf.txt` file in the your local Codeless Project repo.
2. Change the letter `B` in the first line `The Project Getenberg EBook of Beowulf ...` to a lowercase `b`.
1. Execute the following command:

```bash
git diff
```

This will show you, in detail, the differences between the last version of the file that was committed via `git` and any changes you have since created. For details on how this is broken out, see the **Deep Dive** section.

Once you are done, you can restore the modified file to it's original state by typing `git checkout -- beowolf.txt`. This essentialy tells Git to "undo" any changes to that file that are not yet staged or committed.

## Done with commands for now!

If you (and your partner, if you're working in pairs) are done, then you can put your green sticky up! This is how we know you're done.

![green sticky note](images/Sticky-Note-02-Green-300px.png)

## The big picture

With your own projects, for 95% of what you do, `git status` and `git diff` should be sufficient to regularly track your progress and confirm the changes you have made. You will use these commands, along with `git add`, `git commit`, `git push` more than any others. 

**NOTE:** We will cover several more advanced concepts in later discussions.

## Deep dive

It can be very helpful to see what's different between the file you are working on and the last-committed version. To do this, use the `git diff` command.

`git diff` represents changes in a manner referred to generally as "diff format". This format most basically represents all changes as the addition or removal of lines from files.

**Note:** the examples below are in black/white, but in most command-line environments (`bash`, for example) they will also be color-coded to help make them easier to read.

If I add a line to a file, I'll see something like this:

```bash
$ git diff
diff --git a/test.txt b/test.txt
index 624b469..f8b6f0a 100644
--- a/test.txt
+++ b/test.txt
@@ -10,3 +10,4 @@ line 9
 line 10
 line 11
 line 12
+line 13
```

The first part of the output shows the filenames for the files being compared. This is important, because the output from `git diff` might display many files if you have changed numerous files in your repo. You can also specify individual files or groups of files by providing the file name(s) as arguments to the `git diff` command like so: `git diff <file1> <file2> ...`. Even with a single file specified, the output will always show you which file(s) are being compared with each change.

The line that starts with a single `+` indicates that this line is new compared to what's currently staged OR committed. Also note that the tool shows me a few lines before and/or after the change to help me see the context of the change.

Also you can see which line number(s) are involved in the change. The `@@` line tells you that the displayed content starts at line 10 and includes 3 lines (`10,3`) from the original file and then tells you that the displayed content also starts at line 10 and includes 4 lines (`10,4`) from the new file.

Similarly, if I remove a line:

```bash
$ git diff
diff --git a/test.txt b/test.txt
index f8b6f0a..abe1f83 100644
--- a/test.txt
+++ b/test.txt
@@ -9,5 +9,4 @@ line 8
 line 9
 line 10
 line 11
-line 12
 line 13
```

Here, the `-` shows me the line that was removed, i.e. line 12. Notice that the value displayed for the starting line and the number of lines displayed may change: the `@@` line tells you that the displayed content starts at line 9 and includes 5 lines (`9,5`) from the original file and then tells you that the displayed content also starts at line 9 and includes only 4 lines (`9,4`) from the new file.

If I *change* a line, the change actually appears as a removed line AND an added line:

```bash
$ git diff
diff --git a/test.txt b/test.txt
index abe1f83..6276304 100644
--- a/test.txt
+++ b/test.txt
@@ -8,5 +8,5 @@ line 7
 line 8
 line 9
 line 10
-line 11
+line eleven
 line 13
```
The `@@` line tells you that the displayed content starts at line 8 and includes 5 lines (`8,5`) from the original file and then tells you that the displayed content also starts at line 8 and includes 5 lines (`8,4`) from the new file.

A file with multiple changes would look like this:

```bash
$ git diff
diff --git a/test.txt b/test.txt
index abe1f83..a3fc0c5 100644
--- a/test.txt
+++ b/test.txt
@@ -2,11 +2,11 @@ line 1
 line 2
 line 3
 line 4
-line 5
+line five
 line 6
 line 7
 line 8
 line 9
 line 10
-line 11
+line eleven
 line 13
```

Here I can see that I changed line 5 and line 11.

Many GUI-based tools will show you more information, such as highlighting the individual characters in a line that were changed. Since this varies from tool to tool, it won't be covered in detail here.

## Resources

* [Git Basics - Recording Changes to the Repository](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)

<!-- begin auto-generated nav-links section -->
| Previous | Up | Next |
|:---------|:---:|-----:|
| [Git Primary Workflow: Add, Commit, Push](./git_main_lifecycle.md) | [Using Git](./git_overview.md) | [Branching and Merging](./git_branch_merge.md) |
<!-- end auto-generated section -->
