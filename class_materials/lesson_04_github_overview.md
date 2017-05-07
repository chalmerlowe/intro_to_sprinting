# Using GitHub

GitHub is a web-based version control repository. It also serves as an Internet hosting service. Github provides the functionality of `Git` (like distributed version control and source code management). It also offers bug tracking, task management, wikis, gists, feature requests and more. Github is the world's largest repository for source code. Github is used in tandem with `Git` to make changes, share changes, deal with conflicts and enable project participants to synchronize their work.

# Objectives
Through participating in this session, attendees will be able to:

* Understand why GitHub is used in an open source project
* Use some basic features of GitHub to contribute to a project, including creating a copy of the project

A later session will show additional steps in the process such as issuing a **pull request**, etc.


# Lecture/Demos

## How do you get started?

### Create OR login to a GitHub account

If you **DO NOT** have a Github account, you will need to make one:

1. Open your browser and navigate to the [GitHub Home Page](https://github.com/)
2. Fill out the form on the home page:
   * Pick a username (you will need a unique username)
   * Enter your email address
   * Create a password   
3. Click "Sign up for GitHub"

If you **ALREADY** have a Github account, log into your regular account.

## The big picture

Projects files on Github are often called repositories or **repo/repos** for short. For every project you contribute to, you will interact with two different repos:

* One repo will be the original project repository
* The other repo will be your personal copy of the original repo

![Remote Repo](images/github_part_1_remote.png)

When you want to work on a project, Github will enable you to **fork** the project so that you can have a copy of the project under your account.

![Personal Repo](images/github_part_1_personal.png)

## Fork a repository

A **fork** of a repository is a copy, hosted under your account, of a repository created by someone else. You then have complete control to modify and change the code to suit your needs (within the limits of copyright/the license on the project). The fork is tied to the original repository (repo) and you can issue requests to the original owner to incorporate your changes into the original project. This process is called a **pull request**.

To practice these steps, we will have you fork fork a sample project to your github account. Navigate to the [Codeless Project](https://github.com/chalmerlowe/intro_to_sprinting_codeless_project/).

1. In the upper right hand corner, you'll see a **Fork** button:<br>
![Fork a Repo Button](images/fork-repo-icon.png)
2. Click the Fork button to to create a fork under your account
3. **NOTE**:  As mentioned, the fork refers back to the original repo - if you look under your repo name, you'll see it's "forked from chalmerlowe/intro\_to\_sprinting\_codeless\_project:"<br>
![Fork link to original repo](images/fork-repo-link.png)
4. The next step will be to clone the repo from your online Github account to your local computer. That step will be covered in depth in the next lesson: [Git Overview](./lesson_05_git_overview.md)

# Resources

Curious about the difference between a Fork and a Clone? See the StackOverflow discussion of: ["Are git forks actually git clones?"](http://stackoverflow.com/questions/6286571/are-git-forks-actually-git-clones)


|[<<< Previous Lesson: Virtual Environments](./lesson_03_venv_overview.md)|[Next Lesson: Git Overview >>>](./lesson_05_git_overview.md)|
|:--|--:|
