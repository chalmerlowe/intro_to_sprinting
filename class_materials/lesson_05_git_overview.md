# Using Git

## What is git?
Git is a version control system - it enables you to control the various versions of projects, such as open source projects.

Version control systems, along with managing changes to projects, help ensure every contributor is working on the same codebase.

Git is a tool that makes it easy to contribute to projects that other people are
working on. The project code lives in a central **remote repository**, traditionally called
`origin`. Programmers copy the project into their own **local repository**,
where they can work on adding features and squashing bugs. When finished, they
push the code back into `origin`, for other contributers to see and pull from.

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

# Lecture and Demos

## How do you get started?

### Introduce yourself to git

When you contribute to a project, you'll want your name associated with your contributions. The following commands allow git to get to know you:

```bash
git config --global user.name "<Your Name here>"
git config --global user.email "<your_email@domainname.com>"
```

**Note:** You'll only need to do this once on your computer.

### Clone a project
We're presuming you've already read the [github\_overview](./lesson_04_github_overview.md), and have forked Chalmer's Intro to Sprinting repo @ [https://github.com/chalmerlowe/intro_to_sprinting/](https://github.com/chalmerlowe/intro_to_sprinting/) into your own Github repository. IF NOT, go do that now.

Now, you're ready to contribute. It's time to clone the project, so you have a copy on your machine to do work on.

Enter the following on the command line:

```bash
git clone https://github.com/<your_username>/<the_project> <destination/directory/path>
```

This command creates a folder, which should be full of project files. Git will automatically set up `origin` as a **remote** repository, which points to **your** fork of the repository.

Next we inform git of where to find the upstream repository (the repo that your fork was forked from) using the following command:

```bash
git remote add upstream <main repo>
```

Confirm that git has stored the correct upstream repository with this command:

```bash
git remote -v
```

**Note:** You'll do this **one time for each project** you want to work on.

### Contribute to the project

#### How git handles files

Git repositories are very sophisticated, but at the lowest level, they are fairly simple. Git tracks changes to files in a database AND categorizes files in the following ways:

1. Local directory (warehouse)
2. Staging area (pallet)
3. Commit (truck)
4. Origin

As we look at each of these, we will imagine that we are processing materials in a warehouse and shipping them to another location.

#### Local directory

The **local directory** is simply the directory on your machine and it contains all your files, drafts, completed work, incomplete work, tools, etc. This material is uniquely yours. We can consider this to be the warehouse in our example. There are plenty of materials, some that are necessary to run the warehouse, but not part of what is typically stored in the warehouse, some things that have been ordered and some things that are not quite ready to ship. Any new files you create in your local directory will only be visible to you.

#### Staging area

The **staging area** holds all the files that are ready to added to the project and shared with others. The staging area can be compared to the pallet in our example. Everything that is 'done' and ready to be loaded on the truck gets placed on the pallet. To put a file into the staging area (i.e. add  it to the pallet), you will use the `add` command (described below). Just like a pallet, you can continue to add files to the pallet, essentially indefinitely. When you are done making all the changes you want to, you move the pallet into the truck. While things are still in the staging area (on the pallet), it is fairly easy to add more files, remove files, change files, etc. **NOTE**: if you add a file to the staging area and **THEN** make additional changes to the file, you will need to add the file a second time to capture the newest changes.

#### Commit

The **commit area** holds all the changes that you are going to release to the original author. The commit area can be compared to the truck in our example. Once your pallet is full, you load it onto the truck for delivery. Everything that is ready to be shipped goes into the commit area (gets loaded on the truck). To commit a file, you will use the `commit` command (described below). **NOTE**: much like we saw above...if you edit something that has been committed, then the new changes will not be released to the original author. Any new changes will have to be added to the staging area and then committed.

#### Origin

The **origin** is your Github repository or **remote repository**. Nothing gets moved off your local system until you `push` it to your origin repository. Only items that have been committed are pushed to Origin. Pushing to origin can be compared to the truck driving away to deliver the pallet. Once changes have been pushed, they are published and others can see those changes in your Github repository.

Below, we will see how you move files from category to category.

### Making changes to files

After cloning the code from your fork you are free to create and expand upon the
project. Once you have completed something sizeable, be it a feature, function,
or documentation, it is time to commit.

For now, let's edit the `class_materials/student_names.txt` file, by adding your name to the line with your student number. (The instructor will provide you with a student number).

1. Change directories in your **local directory** until you are in the `class_materials` folder.
2. Edit the `student_names.txt` file, adding your name, as described above.
3. **Add** the `student_names.txt` file to the git **staging area**.

    ```bash
    git add student_names.txt
    ```

    If you need to add more than one file to the staging area, simply separate the filenames with a space:

    ```bash
    git add <file1> <file2> ...
    ```

4. After adding the files you changed it is time to **commit** them. It is customary to add a description message (using the `-m` option) describing your changes, when you commit.

    ```bash
    git commit -m "Description of changes"
    ```
    **NOTE**: commit messages should be short (typically 50 characters or less). See the Resources below for more details on commit messages.

5. Lastly, you are going to have to send the commit to Github or another Source Code Manager with:

    ```bash
    git push origin master
    ```

    In this case, you are pushing your master branch to **origin** (the **remote repository**). We'll discuss branching in more depth later.

After pushing to origin you will have to go and create a pull request, which is explained in the [github\_overview](./lesson_04_github_overview.md).

## Common Operations

### Adding

There are couple tricks that makes adding files to a commit a little bit easier if you pay attention to what you are doing. For instance you can add all of the changed files to your staging area with:

```bash
git add *
```

You can add all changed files from the current directory using:

```bash
git add .
```

**NOTE**: This can lead to problems if you add files that aren't related to the commit. To protect against this you can view which files have pending changes before you add them with:

```bash
git status
```

### Committing

The method taught above works fine, but there are additional flags and parameters that can make for a better commit. First of all, if you would like to add a more in depth description you can use:

```bash
git commit
```

This command will bring you into a command line text editor like **vi/vim** or **emacs** where the
first line serves as the title of the commit, followed by a blank line and then you can add a paragraph-style description.

Another feature related to that, which ties in with open source sprinting is if you enter

```bash
git commit -s
```

It will bring of the same command line text editor as before but with a `Signed off by:` section
listing your name, giving the rights to your code to whomever you committed it to.


### Pushing

The `commit` command notes your changes locally, but they are not yet changed on the **origin (remote repository)**. To push your changes up to GitHub, you use the `git push` command:

```bash
git push <repository_name> <branch_name>
```

The repository will generally be `origin` (the conventional name for your primary repository), but does not have to be. In this case we worked on the main branch which is by default, called `master`.

This command can be condensed to simply  `git push` if you are pushing to `origin` on the branch that is currently active in Git (in this case `master`).

### Branching and Merging

With larger projects, it is very common to create **branches** and then **merge** the branch into the main project when you make changes. You've seen references to `master` above, the default branch. A typical enhancement would be done by:

1. creating a branch (so you have a separate workspace to work in) using `git checkout`
1. doing your work as a series of `git add`, `git commit` cycles to the branch, as described above
1. merging your changes back into master

By following this pattern, you keep your work isolated from the rest of the project until it is ready to be released. Examples include:
* creating new features
* experimenting with changes to the code
* fixing bugs

Branches should be small and self-contained so that they can be merged. Sprawling and convoluted changes to code can make it nearly impossible to merge. In addition, it is customary for branches to be focused on specific problems: i.e. one bug fix per branch OR one new feature per branch.

A typical iteration of creating a feature (sometimes called a `feature branch`) would look like this:

```bash
git checkout -b my-feature-name         # "-b" creates a new branch named "my-feature-branch"
# <do some work in my editor or IDE>

git add .
git commit -m 'my first bit of work'
# <do more work in my editor or IDE>

git add .
git commit -m 'my second bit of work'

git checkout master                      # this checks out the master branch              
git merge my-feature-name
git push origin master
```

Let's imagine that you are working on a project with multiple commits to the master branch and a single bug fix branch to fix Issue #53 called `iss53`. Commits `C3` and `C5` are the changes that were committed on the branch, and `C4` is a change made by someone else to the master branch during that same timeframe.

The history created by the above steps would look something like this:

<img src="http://sentheon.com/images/27052016_branches.png">
**Source**: http://sentheon.com/images/27052016_branches.png

# Hands-on

Here you will create a repo locally and make some changes.

##### Create a repo locally

    cd ~
    mkdir my-project-name
    cd my-project-name
    git init

##### Make a branch for your changes

**Note:** replace "my_change_name" with the name of the feature you are adding.

    git checkout -b feature/my_change_name

##### Make your changes

Open your favorite editor or IDE and make the changes desired. When you are finished making changes, proceed with the remaining steps.

##### Commit your changes

    git add .
    git commit -m 'added my new feature'

##### Merge your changes into the master branch

    git checkout master
    git merge feature/my_change_name

##### Delete your feature branch

    git branch -d feature/my_change_name


# Resources
To learn more about git, try these resources:

## Documentation and Books:

[Pro-Git](https://git-scm.com/book/en/v2), a free online resource (and in [PDF](https://progit2.s3.amazonaws.com/en/2016-03-22-f3531/progit-en.1084.pdf) form to save to your computer) with comprehensive documentation about using git well by Scott Chacon and Ben Straub

[User Manual](https://git-scm.com/docs/user-manual.html)

## Tutorials and videos:
[Interactive Tutorial](https://try.github.io/levels/1/challenges/1)

[A Successful Git Branching Model](http://nvie.com/posts/a-successful-git-branching-model/), which describes the branching model used by a variety of large and small projects; some projects do this differently, but the basic ideas are common with all of them

[Written Tutorial](https://git-scm.com/docs/gittutorial)

[Videos](https://git-scm.com/videos)

[50/72 rule for git commit messages](http://stackoverflow.com/questions/2290016/git-commit-messages-50-72-formatting) How to format git commit messages efficiently

## Reference Manuals:
[Official Reference Manual](https://git-scm.com/docs)

[Git cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)

|[<<< Previous Lesson: GitHub Overview](./lesson_04_github_overview.md)|[Next Lesson: Intro to the Project >>>](./lesson_06_github_part_deux.md)|
|:--|--:|
