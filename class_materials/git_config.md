# Setting up Git

## Time-box

5 Minutes


## Overview

When you contribute to a project, you'll want your name associated with your contributions. Git will automatically attach your name and email address to every commit you make, if you tell it how.


## What to do

Run the following commands on the commandline to set two global configurations: your name and your email address. Since you are not Johnny Appleseed, please change the commands accordingly.

```bash
$ git config --global user.name "Johnny Appleseed"
$ git config --global user.email "johnny.appleseed@example.com"
```

## Done with commands for now!

If you (if you're working in pairs, you and your partner) are done, then now you can put your green sticky up! This is how we know you're done with the commands.

![green sticky note](images/Sticky-Note-02-Green-300px.png)

If you like reading, you can also keep reading this page.

## The big picture

These are the two fundamental configurations needed to use `git`. 

**Note:** The "--global" option applies these settings to all git projects on your machine  
* You only need to run this **once per computer**.  
* Re-run the command to change a setting.  
* To override these settings for a specific project (i.e. a work project versus a personal project), simply run the command while in that project directory, and leave out the `"--global"` option.

Later sections of the workshop will go into greater depth on `git`.

## Deep dive

`git` is a command-line tool, and as such you will be doing a lot of typing when you work with it. There are many configurations that can be set for `git` but they are outside the scope of this workshop. 

Because git is a commandline tool, if you need a primer for the command line, check out the [free course on Codecademy](https://www.codecademy.com/learn/learn-the-command-line). If you just need a quick reference, check out the [Linux commands cheat sheet on It's Foss](https://itsfoss.com/linux-commands-cheat-sheets/).


## Resources

See the lesson [Git Concepts](./git_concepts.md) for a more comprehensive list of resources...

| Previous | Up | Next |
|:---------|:---:|-----:|
| [Using the Command Line](./command_line.md) | [Environment Set-up](./environment_overview.md) | [Using Git](./git_overview.md) |
