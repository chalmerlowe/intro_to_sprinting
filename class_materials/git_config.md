<!-- begin auto-generated title section -->
# Setting up Git
<!-- end auto-generated section -->


## Time-box

5 Minutes


## Overview

When you contribute to a project, you'll want your name associated with your contributions. Git will automatically attach your name and email address to every commit you make, if you tell it how.


## What to do

Run the following commands on the command-line to set two global configurations: your name and your email address. Since you are not Johnny Appleseed, please change the commands accordingly.

```bash
$ git config --global user.name "Johnny Appleseed"
$ git config --global user.email "johnny.appleseed@example.com"
```

## Done with commands for now!

If you (and your partner, if you're working in pairs) are done, then you can put your green sticky up! This is how we know you're done.

![green sticky note](images/Sticky-Note-02-Green-300px.png)

## The big picture

These are the two fundamental configurations needed to use `git`. 

**Note:** The `--global` option applies these settings to all `git` projects on your machine  
* You only need to run this **once per computer**.  
* To change a setting, simply re-run the command.  
* To override these settings for a specific project (e.g., a work project versus a personal project), simply run the command while in that project directory, and leave out the `--global` option.

Later sections of the workshop will go into greater depth on using `git`.

## Deep dive

`git` is a command-line tool, and as such you will be doing a lot of typing when you work with it. There are many configurations that can be set for `git` but they are outside the scope of this workshop. 

Because `git` is a command-line tool, if you need a primer for the command line, check out the . If you just need a quick reference, check out the .


## Resources

* [Getting Started - First-Time Git Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
* See the lesson [Git Concepts](./git_concepts.md) for a more comprehensive list of resources related to `git`.
* Free [Learn the command-line](https://www.codecademy.com/learn/learn-the-command-line) course on Codecademy
* Cheatsheet for [Linux command-line commands](https://itsfoss.com/linux-commands-cheat-sheets/)
* Cheatsheet for Windows command-line commands: 
* Cheatsheet for Mac command-line commands:

<!-- begin auto-generated nav-links section -->
| Previous | Up | Next |
|:---------|:---:|-----:|
| [Setting up GitHub and Forking a Repository](./github_setup.md) | [Environment Set-up](./environment_overview.md) | [Using Git](./git_overview.md) |
<!-- end auto-generated section -->
