# Using Git


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
    * perform basic troubleshooting

**NOTE**: this will be a **hands-on** overview of git. It is incredibly powerful with many options and capabilities. The goal is to get you **started** with git, but it will take time and practice on your own to make you into an expert.





Below, we will show you how to move files from category to category and track your progress, status and changes as you go.



# Lesson Practice

## Making changes to files

This practice presumes that:

* you are in your `mytest` directory
* your `mytest` virtualenv is active
* you have forked the [Codeless Project](https://github.com/chalmerlowe/intro_to_sprinting_codeless_project/) to your repo
* you have cloned that material into your local directory

With a freshly cloned repo, we can make some edits and revisions to the Codeless Project, which is full of files with poems.


**Ensure** you are in the top-level folder for the repository. 
   
   * If you type `ls` (or `dir` in Windows) you should see multiple files.

Pick a file and edit it.
 
   * Open your favorite editor or IDE and make some desired changes. 
     * Perhaps you want to add a new file with your favorite poems
     * Add a joke to a Nerd Jokes file
     * But any change to a line, a word, a phrase will be sufficient
     * **NOTE**: this workshop is intended for all audiences, so please avoid anything inappropriate OR not safe for work (NSFW). **Play like a champion**.
   * Save the file. 
  

**Check** the current status of all files in the repository:

```bash
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   <file you edited>
```
**Add** the file you edited, to the git **staging area**.

```bash
$ git add <file you edited>
```

If you need to add more than one file to the staging area, simply separate the filenames with a space:

```bash
$ git add <file1> <file2> ...
```
    
... or you can add groups of files using standard [globbing](https://en.wikipedia.org/wiki/Glob_(programming)):
    
```bash
$ git add *.txt
```

**Commit** your changes when you are ready to make a permanent record of them. It is customary to add a description message (using the `-m` option) describing your changes, when you commit.

```bash
$ git commit -m "Description of changes"
```

**NOTE**: commit messages should be short (typically 50 characters or less). See the Resources below for more details on commit messages.

**Push** the commit to Github with:

```bash
$ git push origin master
```

In this case, you are pushing your master branch to **origin** (the **remote repository**). We'll discuss branching in more depth later.

After pushing to origin you will have to go and create a pull request, which is explained in the [Github\_overview](./lesson_04_github_overview.md).

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
