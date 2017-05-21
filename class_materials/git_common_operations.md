# Git Common Operation(s): diff


## Time-box

<XX> Minutes


## Overview

<add overview to intro diff>

## What to do

This portion of the workshop presumes the following:
<add some steps>


## The big picture

In this section, we covered a number of commands that break down into several key concepts:

* Determine the **status** of your local directory
* **Add** a file to the staging area
* **Commit** that file for the historical record
* **Push** the file to your Github repo

With your own projects, for 95% of what you do, this is sufficient to regularly track your progress and get your changes onto the Internet. You will use these commands more than any others. 

**NOTE:** We will cover several more advanced concepts both in the Deep Dive and in later discussions.


## Deep dive

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

If you need to add more than one file to the staging area, simply separate the filenames with a space:

```bash
$ git add <file1> <file2> ...
```

... or you can add groups of files using standard [globbing](https://en.wikipedia.org/wiki/Glob_(programming)):
    
```bash
$ git add *.txt
```

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


## Resources

* [<resource name>](<resource url>)
* [<resource name>](<resource url>)


| Previous | Up | Next |
|:---------|:---:|-----:|
| [Cloning a Repository](./git_cloning.md) | [Using Git](./git_overview.md) | [Branching and Merging](./git_branch_merge.md) |


