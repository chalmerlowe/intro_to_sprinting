# Git Primary Workflow: Add, Commit, Push


## Time-box

<XX> Minutes


## Overview

<put single paragraph here>


## What to do

This portion of the workshop presumes the following:

1. your `mytest` virtualenv is **active**
1. you have **forked** the [Codeless Project](https://github.com/chalmerlowe/intro_to_sprinting_codeless_project/) to your repo
1. you have **cloned** that material into your local `mytest` directory
1. you are in the `intro_to_sprinting_codeless_project` directory

With a freshly cloned repo, we can make some edits and revisions to the Codeless Project, which is full of poetry files.
   
* If you type `ls` (or `dir` in Windows) you should see multiple files.

### Status check
Before we change any files, we can check to see what the status of our repo is, by using `git status` 

```bash
$ git status
```
**NOTE**: Full details on the messages that appear are down below in the Big Picture/Deep Dive discussion.

### Pick a file and edit it.
 
Open your favorite text editor or integrated development environment (IDE) and make any one of the following changes. 

* Open any file and change any line, word or phrase
* Create a new file and add your favorite to poem
* **NOTE**: this workshop is intended for all audiences (and may include youth), so please avoid anything inappropriate OR not safe for work (NSFW). **Play like a champion**.
* Save the file. 
  
### Status Check
Before we go further, it is often useful to again check the status. We should notice that a line in the output identifies that a text file has been modified, but has not been staged.

```bash
$ git status
<abbreviated for clarity>
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   <file you edited.txt>

```
### Add the file to the staging area
Add the file **you** edited, to the git staging area using the following command. *ENSURE* you replace `<file you edited>` with the actual name of the file.

```bash
$ git add <file you edited>
```

### Status check
Take a look at things now that the file has been staged, again using `git status`... We should notice that a line in the output identifies that a text file has been modified AND is now ready to be committed.

```bash
$ git status
<abbreviated for clarity>
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   git_main_lifecycle.md
```

### Commit your changes


Commit your changes when you are ready to make a permanent record of them. It is customary to add a short description message (using the `-m` option) describing your changes, whenever you commit.

```bash
$ git commit -m "Description of changes"
```

**NOTE**: commit messages should be short (typically 50 characters or less). See the Resources below for more details on commit messages.

### Status check
Take a look at things now that the file has been committed, again using `git status`... We should notice a line in the output identifies that your files are ahead of/or no longer in sync with the files in **your Github repo**.

```bash
$ git status
<abbreviated for clarity>
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
```

### Push your changes to your Github repo:
Push the commit to **your** Github repo with `git push`:

```bash
$ git push origin master 
```

In this case, you are pushing your `master` branch (i.e. the main branch you have been working on) to **origin**, your Github repository. We will discuss branching in more depth later.


## The big picture

<high-level concepts that can be described in a few mintues>


## Deep dive

<detailed explanations go here, with h3/h4 subsecitons if necessary>


## Resources

* [<resource name>](<resource url>)
* [<resource name>](<resource url>)


| Previous | Up | Next |
|:---------|:---:|-----:|
| [Cloning a Repository](./git_cloning.md) | [Using Git](./git_overview.md) | [Branching and Merging](./git_branch_merge.md) |




### Checking the status of everything

There is a simple way to see what status every file is in: `git status`. Don't try this yet (we'll do it soon), just read the various types of status messages you will encounter regularly and see if you can make sense of them:

```bash
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working tree clean
```

This tells you that right now your local copy matches what your computer last heard is on the server... everything is **clean**.

If you have locally changed files that are in a **working** state (not yet staged), you will see something like this:

```bash
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

This says the file called "README.md" is changed locally but not yet staged. Note particularly that there are several helper messages in there: they tell me how to **add** the README.md file to the staging area and how to **revert** it (get it back to the way it was before I made my change) should I want to do those things.

Next I want to move the file to staging (**add** it):

```bash
$ git add README.md
```
It is especially useful as you learn to check the status regularly. It will help you get familiar with the messages and hints AND drive home the concepts related to local changes, staged changes, committed changes, etc.

```
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   README.md
```

Now we can see that the file is **staged**, but not yet **committed**. We can also see the hint for what to type to if we need to move it back to an unstaged state.

Next I want to commit the file (i.e. load it on the truck) using `git commit -m "a short description"`, where `-m` is a flag for my commit message. Good commit messages should be short, sweet and descriptive.

```bash
$ git commit -m 'my short description of the work'
[master 206546b] my short description of the work
 1 file changed, 1 insertion(+), 1 deletion(-)
```

`git status` again comes to the rescue to help us confirm and understand the changes we have initiated.

```
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
nothing to commit, working tree clean
```

Here, like earlier, my working tree is again **clean** (all changes are committed). However, unlike before, I have some changes in my local repository that are not yet on the remote server. Like all other status messages, I can see what to type to push the file up to Github.

I can push that file:

```bash
$ git push
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 284 bytes | 0 bytes/s, done.
Total 3 (delta 2), reused 0 (delta 0)
To github:myusername/my_repo.git
   98b2f3f..206546b  master -> master
```
Let's take a look at the results of our work:

```
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working tree clean
```

... and everything is clean again, but now with my local change pushed to GitHub and available to the world. **IF** you go to **your** github repository, you can see your changes via your web browser.

Get in the habit of using `git status` regularly, it is probably the most informative and helpful command for understanding exactly what's going on.

## Common Operations


### Seeing what you've changed

It can be very helpful to see what's different between the file you are working on and the last-committed version. To do this, use the `git diff` command.

`git diff` represents changes in a manner referred to generally as "diff format". This format most basically represents all changes as the addition or removal of lines from files.

**Note:** the examples below are in black/white, but in most command-line environments (`bash`, for example) they will also be color-coded to help make them easier to read.

If I add a line to a file, I'll see something like this:

```bash
$ git diff
diff --git a/rpncalculator/parser.py b/rpncalculator/parser.py
index 90cd3cd..e22a262 100644
--- a/rpncalculator/parser.py
+++ b/rpncalculator/parser.py
@@ -39,6 +39,7 @@ class Parser(object):
         """scan input stream and return token generator"""
         if isinstance(stream, str):
             stream = StringIO(stream)
+        print(str(stream))
         for line in stream:
             tokens, remainder = _scanner.scan(line)
             for t in tokens:
```

The first part of the output shows me which file is being displayed. The output from `git diff` can contain many files; you can specify individual files or groups of files by providing the file name(s) to git diff with `git diff <file1> <file2> ...`. Even with a single file specified, the output will always tell you which file(s) are being compared with each change.

The line that starts with `+` indicates that line is new compared to what's currently committed. Also note that the tool shows me a few lines before and after the change to help me see the context of the change.

Also you can see which line number(s) are involved in the change. The `@@` line tells you that line 39 is the affected line. There are two line numbers there because changes to multiple places in a file can mess up your idea of line numbers. Just remember that the first number is the line in the original file and the second number is the line in the modified file.

Similarly, if I remove a line:

```bash
$ git diff
diff --git a/rpncalculator/parser.py b/rpncalculator/parser.py
index e22a262..90cd3cd 100644
--- a/rpncalculator/parser.py
+++ b/rpncalculator/parser.py
@@ -39,7 +39,6 @@ class Parser(object):
         """scan input stream and return token generator"""
         if isinstance(stream, str):
             stream = StringIO(stream)
-        print(str(stream))
         for line in stream:
             tokens, remainder = _scanner.scan(line)
             for t in tokens:
```

Here, the `-` shows me the line that was removed.

If I *change* a line, it will show as a removed line and an added line:

```bash
$ git diff
diff --git a/rpncalculator/parser.py b/rpncalculator/parser.py
index e22a262..b186e9a 100644
--- a/rpncalculator/parser.py
+++ b/rpncalculator/parser.py
@@ -39,7 +39,7 @@ class Parser(object):
         """scan input stream and return token generator"""
         if isinstance(stream, str):
             stream = StringIO(stream)
-        print(str(stream))
+        log.debug(str(stream))
         for line in stream:
             tokens, remainder = _scanner.scan(line)
             for t in tokens:
```

Here you can see that I changed the print() call to a log.debug() call.

A file with multiple changes would look like this:

```bash
$ git diff
diff --git a/rpncalculator/parser.py b/rpncalculator/parser.py
index e22a262..7e8bf4a 100644
--- a/rpncalculator/parser.py
+++ b/rpncalculator/parser.py
@@ -39,7 +39,7 @@ class Parser(object):
         """scan input stream and return token generator"""
         if isinstance(stream, str):
             stream = StringIO(stream)
-        print str(stream)
+        log.debug(str(stream))
         for line in stream:
             tokens, remainder = _scanner.scan(line)
             for t in tokens:
@@ -50,6 +50,7 @@ class Parser(object):
         if not engine:
             engine = Engine()
         result = None
+        log.debug(str(stream))
         for token in self.scan(stream):
             if isinstance(token, float) or isinstance(token, int):
                 result = engine.push(token)
```

Here I can see that I changed line 39 from a `print()` to `log.debug()` and that I also added a new `log.debug()` call at line 50.

Many GUI-based tools will show you more information, such as highlighting the individual characters in a line that were changed. Since this varies from tool to tool, it won't be covered in detail here.

### Adding lots of stuff (at once)

There are couple tricks that make adding files to a commit a little bit easier if you pay attention to what you are doing. For instance you can add **all** of the changed files to your staging area with:

```bash
$ git add *
```

You can add **all** changed files from the current directory using:

```bash
$ git add .
```

**NOTE**: This can lead to problems if you add files that aren't related to the commit. To protect against this you can view which files have pending changes **before** you add them with:

```bash
$ git status
```

### Committing (when you have lots to say)

The method taught above works fine, but there are additional flags and parameters that can make for a better commit. First of all, if you would like to add a more in depth description you can use (without the `-m`):

```bash
$ git commit
```

This command will bring you into a command line text editor like **vi/vim** or **emacs** where the
first line serves as the title of the commit, followed by a blank line and then you can add a paragraph-style description.

Another feature related to that, which ties in with open source sprinting is if you enter

```bash
$ git commit -s
```

It will bring of the same command line text editor as before but with a `Signed off by:` section
listing your name, giving the rights to your code to whomever you committed it to.



# Lesson Practice

## Making changes to files

This practice presumes that:


If you need to add more than one file to the staging area, simply separate the filenames with a space:

```bash
$ git add <file1> <file2> ...
```

... or you can add groups of files using standard [globbing](https://en.wikipedia.org/wiki/Glob_(programming)):
    
```bash
$ git add *.txt
```
