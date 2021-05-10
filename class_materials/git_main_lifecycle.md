<!-- begin auto-generated title section -->
# Git Primary Workflow: Add, Commit, Push
<!-- end auto-generated section -->


## Time-box

10 Minutes


## Overview

In this section, we will cover a number of commands, but the principles are fairly straightforward:

* Determine the **status** of your local directory
* **Add** a file to the staging area
* **Commit** that file for the historical record
* **Push** the file to **your** GitHub repo

## What to do

This portion of the workshop presumes the following:

1. you have **forked** the Codeless Project to your repo (NOTE: either our version if you are doing self study via the [Codeless Project](https://github.com/chalmerlowe/intro_to_sprinting_codeless_project/) or a copy identified for you by your workshop instructor.
1. you have **cloned** the Codeless Project repo into your local `mytest` directory
1. you are in the `intro_to_sprinting_codeless_project` directory on your commandline

With a freshly cloned repo, we can make some edits and revisions to the Codeless Project, which is full of poetry files.

If you type `ls` (or `dir` if you are using Windows) you should see multiple files, such as:

* annabel_lee.txt
* beowulf.txt
* do_not_go_gentle.txt
* the raven.txt
* jabberwocky.txt
* etc


### Status check
At any time, we can check the status of our `git` repository. Before we change any files, let's check to see what the status of our repo is, by using `git status`

```bash
$ git status
```

**NOTE**: Full details on the messages that appear are spelled out below in the **Big Picture/Deep Dive** discussion.

**NOTE**: Using `git status` is completely **optional**, but strongly recommended. As you learn how each of the `git` commands change the state of your repository it can provide feedback and better understanding.


### Pick a file and edit it.

1. Open your favorite text editor or integrated development environment (IDE).
1. Select a file to edit and open the file in your editor/IDE.
    * **NOTE**: this workshop is intended for all audiences (and may include youth), so in making the following changes, please avoid anything inappropriate OR not safe for work (NSFW). **Play like a champion**.

1. Make a simple change, such as:
    * Change any line, word or phrase
    * Add a new line
    * Delete a line

1. Save the file.

### Status Check
Before we go further, it is often useful to again check the status using `git status`. We should notice that a line in the output identifies that a text file has been modified, but has not been staged.

```bash
$ git status
# abbreviated for clarity
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   johnny_appleseed.txt
```

### Add the file to the staging area
We now add the file **you** edited to the git staging area using the `git add` command. **ENSURE** you replace `johnny_appleseed.txt` with the actual name of the file.

```bash
$ git add johnny_appleseed.txt
```

If you need to add more than one file to the staging area, simply separate the filenames with a space:

```bash
$ git add <file1> <file2> ...
```

### Status check
Take a look at things now that the file has been staged, again using `git status`... We should notice that the output identifies that a text file has been modified AND is now ready to be committed.

```bash
$ git status
# abbreviated for clarity
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   johnny_appleseed.txt
```

### Commit your changes


We use `git commit` to commit your changes when you are ready to make a permanent record of them. It is customary to add a short descriptive message (using the `-m` option) describing your changes, whenever you commit.

```bash
$ git commit -m "Description of changes"
```

> **NOTE**: Commit messages should be short (typically 50 characters or less). See the **Resources** below for more details on commit messages.

### Status check
Take a look at things now that the file has been committed, again using `git status`... We should notice a line in the output identifies that your files are ahead of/or no longer in sync with the files in **your GitHub repo**.

```bash
$ git status
# abbreviated for clarity
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)
```

### Push your changes to your GitHub repo:

> **NOTE**: historically, git repositories used the term `master` to indicate the main branch OR the latest branch of a repository. This term comes with some negative connotations and as such, many open source development teams have changed the name of the main branch in their repository to be `main`. Both the **Intro to Sprinting** and the **Intro to Sprinting Codeless Project** have set our primary branch name to be main. Having said that, in other tutorials, in other repos, etc you may still find references to `master`.

Push the commit to **your** GitHub repo with `git push`:

```bash
$ git push origin main
```

In this case, you are pushing your `main` branch (i.e., the main branch you have been working on) to **origin**, your GitHub repository. We will discuss branching in more depth later.

### Status check, local
Take a look at things now that the file has been pushed, again using `git status`... We should notice a line in the output identifies that your `main` branch is up-to-date/or in sync with **your GitHub repo** (`origin`).

```bash
$ git status
On branch main
Your branch is up-to-date with 'origin/main'.
```

### Status check, remote
Now go to **your GitHub Repo** and confirm that the changes you made on your local computer are actually present in the files on GitHub. You should be able to surf to the file you edited and see the changes!

## Done with commands for now!

If you (and your partner, if you're working in pairs) are done, then you can put your green sticky up! This is how we know you're done. Feel free to read the following sections to learn more about some of steps you just completed.

![green sticky note](images/Sticky-Note-02-Green-300px.png)

## The big picture

In this section, we covered a number of commands that break down into several key concepts:

* Determine the **status** of your local directory
* **Add** a file to the staging area
* **Commit** that file for the historical record
* **Push** the file to your GitHub repo

With your own projects, for 95% of what you do, this is sufficient to regularly track your progress and get your changes onto the internet. You will use these commands more than any others.

**NOTE:** We will cover several more advanced concepts both in the **Deep Dive** and in later discussions.


## Deep dive

Especially for beginners, understanding the state of your local directory is critical to growing your skills. And luckily, for 95% of what you do, only a handful of commands will get you most of the way.

### Status checking

Since some of our messages above were abbreviated for clarity, let's look more deeply into what we really get from `git status`. Get into the habit of reading the status messages after every command you type and you will quickly hone in on the feedback you need. The following command tells you that right now, your local copy matches what your computer last heard is in your GitHub server... everything is **clean**.

> **NOTE**: git does not check the remote repository every time you do this. It simply compares the state of your files since the last time it checked in with that remote repository.


```bash
$ git status
On branch main
Your branch is up-to-date with 'origin/main'.
nothing to commit, working tree clean
```

If you have locally changed files that are in a **working** state (not yet **staged**), you will see something like this:

```bash
$ git status
On branch main
Your branch is up-to-date with 'origin/main'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

This says the file called "README.md" is changed locally but not yet staged. 

> **NOTE**: There are several helper messages in the above status report that tell us how to:

* **add** the README.md file to the staging area
* **revert** the README.md (i.e. get it back to the way it was before I made my change)

These helper messages show up regularly in `git status` (and elsewhere, to point you in the right direction for the most common use cases).

### Staging files

Next I want to move the file to the staging area (i.e. `git add` to the pallet):

```bash
$ git add README.md
```

This time, the status message is slightly different. The hints are different and the status announcements are new. Again, reading these status messages will help you get familiar with the commands AND hints AND will drive home the concepts related to local changes, staged changes, committed changes, etc.

```bash
$ git status
On branch main
Your branch is up-to-date with 'origin/main'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   README.md
```

Now we can see that the file is **staged**, but not yet **committed**. We can also see the hint `git reset HEAD` for what to type if we need to move a given file back to an unstaged state.

### Committing files

Next I want to commit the file (i.e. load it on the truck) using `git commit -m "a short description"`, where `-m` is a flag for my commit message. Good commit messages should be short, sweet and descriptive.

```bash
$ git commit -m "my short description of the work"
[main 206546b] my short description of the work
 1 file changed, 1 insertion(+), 1 deletion(-)
```

In this case, the immediate output from the `git commit` command tells me several things:

* it repeats my commit message
* lets me know what types of changes occurred: 1 file changed, 1 line was inserted, 1 line was deleted (i.e., I swapped out a line)

In a later discussion, we will discuss how to see exactly what content changed.

`git status` again comes to the rescue to help us confirm and understand the changes we have committed.

```bash
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)
nothing to commit, working tree clean
```

Here, like earlier, my working tree is again **clean** (all changes are committed). However, unlike before, I have some changes in my local repository that are not yet on the remote server. Like all other status messages, I can see the hint message that provides guidance on how to proceed: i.e. type `git push` to send the file up to **my GitHub repo** (`origin`).

### Pushing files

When pushing your commits to GitHub, the `git push` command will give you a summary of all the changes that it attempted to make. In the following case, we see that `git push`:

* sent several objects (NOTE: it is normal for multiple objects to be sent up even if you only changed one file. Those other items are internal to `git` and not critical for you to worry about now)
* compressed the data
* wrote the data
* reported back on where the data was sent
* displayed several hash values showing the commits

```bash
$ git push
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 284 bytes | 0 bytes/s, done.
Total 3 (delta 2), reused 0 (delta 0)
To github:myusername/my_repo.git
   98b2f3f..206546b  main -> main
```

> **About Hashes**: without going into the computer science behind it, `git` creates a unique value called a `hash` for every change that gets committed. Because hashes are unique values, they allow you to:
> * pick specific commits to examine OR
> * specific commits to revert back to, if you find you need to undo a change to your repository
>
> The seven digit numbers you see in `git` and on GitHub (e.g., `206546b`) identify a specific change and are a short form for a longer hash number. Generally, about seven or eight digits are sufficient to uniquely identify a specific hash number within a git repository. A sample of the longer form of a hash might look like this: `206546b828dd2e0e34bb20041dec0a029348133f`

Let's again use `git status` to look at the results of our work:

```bash
$ git status
On branch main
Your branch is up-to-date with 'origin/main'.
nothing to commit, working tree clean
```

... and everything is clean again, but now with our local change has been pushed to GitHub and available to the world. **IF** you go to **your GitHub repository**, you can see your changes via your web browser.

Get in the habit of using `git status` regularly, it is probably the most informative and helpful command for understanding exactly what's going on.

## Resources

* [Git Basics - Recording Changes to the Repository](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)

<!-- begin auto-generated nav-links section -->
| Previous | Up | Next |
|:---------|:---:|-----:|
| [Cloning a Repository](./git_cloning.md) | [Using Git](./git_overview.md) | [Git Common Operations](./git_common_operations.md) |
<!-- end auto-generated section -->
