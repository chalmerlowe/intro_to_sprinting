<!-- begin auto-generated title section -->
# Using Git
<!-- end auto-generated section -->


## Overview

`git` is a version control system -- it enables you to control the various versions of your projects, such as open source projects.

While `git` is great for helping you manage versions for **your own** projects, it also makes it easy to contribute to projects that **other people** are working on. If you are collaborating on a project with others OR if you have a copy of your project hosted somewhere, such as GitHub, the project code will live in a central **remote repository**, traditionally called `upstream`. Programmers copy a fork of the project into their own remote repository and then clone the fork to a **local repository**, where they can work on adding features and squashing bugs. When finished, they push the code to their fork and issue a pull request to `upstream`, for other contributors to see and/or incorporate. Version control systems, along with managing changes to projects, also help ensure each contributor is working on the same codebase.

## Objectives

Through participating in this session, attendees will be able to:

* Understand why `git` is used in an open source project
* Use basic `git` commands to:
    * get a copy of an open source project
    * save modifications/additions/deletions to the project
    * submit those changes to the project
    * incorporate other's changes to the project
    * verify the status of the project repository
    * perform basic troubleshooting

<div style="background-color: #eaea8d; border: 2px solid #0e0e0e; padding: 5px; color:#0e0e0e">
  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px;">
    <path d="M4 2v20h16V2H4zm16 2l-8 5-8-5M4 6l8 5 8-5" />
  </svg>
 <b>NOTE:</b> this will be a <b>hands-on</b> overview of `git`. The `git` software is incredibly powerful with many options and capabilities. The goal is to get you <b>started</b> with `git`, but it will take time and practice on your own to make you into an expert.


</div>
<br>

### Command-line interface

We will be using `git` from the command line in this course. There are a lot of commands, and they can be kind of confusing. That's OK... it will start to make sense once you do it a few times. And that's why you're here!

### Graphical User Interface (GUI)-based `git` tools

There are Graphical User Interface (GUI) tools available as well, but they are beyond the scope of this workshop. Some examples include:

* [gitk](https://lostechies.com/joshuaflanagan/2010/09/03/use-gitk-to-understand-git/)
* [SourceTree](https://www.sourcetreeapp.com/)
* [GitHub Desktop](https://desktop.github.com/)

... and there are many others.


## Lessons

* [Git Concepts](./git_concepts.md): <objective of lesson>
* [Cloning a Repository](./git_cloning.md): <objective of lesson>
* [Git Primary Workflow: Add, Commit, Push](./git_main_lifecycle.md): <objective of lesson>
* [Git Common Operations](./git_common_operations.md): <objective of lesson>
* [Branching and Merging](./git_branch_merge.md): <objective of lesson>


## Resources

* [Getting Started - Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)

<!-- begin auto-generated nav-links section -->
| Previous                          |                Up                |                              Next |
| :-------------------------------- | :------------------------------: | --------------------------------: |
| [Setting up Git](./git_config.md) | [Table of Contents](./README.md) | [Git Concepts](./git_concepts.md) |
<!-- end auto-generated section -->
