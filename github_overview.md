####################################################################################################
# Using GitHub
GitHub is a Git repository (repo) hosting service - it provides a Web-based graphical interface
which offers collaboration features for projects.

# Objectives
Through participating in this session, attendees will be able to:
* Understand why GitHub is used in an open source project
* Use some basic features of GitHub to contribute to a project

# What is GitHub?
GitHub is used to host Git repositories or repos.  It's a `cloud` or hosted service making it
easy for people from all over the world to easily collaborate on and contribute to projects
such as Open Source.  GitHub is used in tandem with Git to make changes, share the changes,
deal with conflicting changes and keep all project participants synchronized.

# How do you get started?
## Create a GitHub account
* Open your browser and navigate to [The GitHub Home Page](https://github.com/)
* Fill out the forms and click "Sign up for GitHub"

## Clone a project
Navigate to [Chalmer Lowe's intro_to_sprinting repo](https://github.com/chalmerlowe/intro_to_sprinting/) and clone it
* In the upper right hand corner, you'll see a "Fork" Icon:
  * ![Fork a Repo Button](images/fork-repo-icon.png)
* Click on it to create a fork (a copy linked to the original) of this repo in your account
* Note:  The fork refers back to the original - if you look under your repo name, you'll see
it's "forked from chalmerlowe/intro_to_sprinting:"
  * ![Fork link to original repo](images/fork-repo-link.png)
* From your working system you'll need to clone this repo to create a local copy and make
changes - refer to the Git section
* If you make changes you want to share with the original author, Chalmer Lowe, you'll need to
submit a Pull Request:
  * Using git on your local repo on your working system you'll need to push the changes to your
GitHub repo - refer to the Git section on how to do this
  * Once you have the changes in your GitHub Repo, above the file list on the left hand side,
click on "New Pull Request:"
    * ![New Pull Request Button](images/new-pull-request-icon.png)
  * Next
    1. Make sure the base fork is chalmerlowe/intro_to_sprinting and the head fork is your repo
    2. Make sure you get a green check mark and "Able to merge" - if there are conflicts, you
should pull all changes from chalmerlowe's upstream repo - see the Git section for how to do this
    3. Click on "Create pull request:"
      * ![Create Pull Request One](images/create-pull-request-one.png)
  * Next
    1. Write a summary title describing the changes
    2. Write a brief description of what you're changing in this pull request
    3. Click on "Create pull request:"
      * ![Create Pull Request Two](images/create-pull-request-two.png)
  * Note:  This leaves you in author's repo (Chalmer Lowe in this case) and not your own!

