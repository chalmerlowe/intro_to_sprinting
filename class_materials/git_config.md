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

If you (and your partner, if you're working in pairs) are done, then you can put your green sticky up! This is how we know you're done. Feel free to read the following sections to learn more about some of steps you just completed.

![green sticky note](images/Sticky-Note-02-Green-300px.png)

## The big picture

These are the two fundamental configurations needed to use `git`.


<div style="background-color: #eaea8d; border: 2px solid #0e0e0e; padding: 5px; color:#0e0e0e">
  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px;">
    <path d="M4 2v20h16V2H4zm16 2l-8 5-8-5M4 6l8 5 8-5" />
  </svg>
 <b>NOTE:</b> The `--global` option applies these settings to all `git` projects on your machine<br>

- You only need to run this <b>once per computer</b><br>
- To change a setting, simply re-run the command<br>
- To override these settings for a specific project (e.g., a work project versus a personal project), simply run the command while in that project directory, and leave out the "--global" option

</div>
<br>

Later sections of the workshop will go into greater depth on using `git`.

## Deep dive

`git` is a command-line tool, and as such you will be doing a lot of typing when you work with it. There are many configurations that can be set for `git` but they are outside the scope of this workshop.

Because `git` is a command-line tool, if you need a primer for the command line, check out the [Learn the command-line](https://www.codecademy.com/learn/learn-the-command-line) course on Codecademy. If you just need a quick reference, check out the cheatsheets in **Resources** section below.


## Resources

* [Getting Started - First-Time Git Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
* See the lesson [Git Concepts](./git_concepts.md) for a more comprehensive list of resources related to `git`
* Free [Learn the command-line](https://www.codecademy.com/learn/learn-the-command-line) course on Codecademy
* [Windows command-line cheatsheet](http://www.cs.columbia.edu/~sedwards/classes/2017/1102-spring/Command%20Prompt%20Cheatsheet.pdf) Windows commandline commands
* [Linux/Mac command-line cheatsheet](https://files.fosswire.com/2007/08/fwunixref.pdf) Linux commandline commands

<!-- begin auto-generated nav-links section -->
| Previous | Up | Next |
|:---------|:---:|-----:|
| [Setting up GitHub and Forking a Repository](./github_setup.md) | [Environment Set-up](./environment_overview.md) | [Using Git](./git_overview.md) |
<!-- end auto-generated section -->
