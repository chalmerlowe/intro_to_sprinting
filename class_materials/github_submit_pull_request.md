<!-- begin auto-generated title section -->
# Submitting a Pull Request
<!-- end auto-generated section -->


## Time-box

5 Minutes


## Overview

Once you have a change OR changes pushed to your GitHub repo, you will want to share those changes with the owner of the upstream project repository.

**NOTE**: This lesson presumes that your changes have been pushed to **your own** GitHub repo (instructions on how to do this were covered in a previous lesson: [Git Overview](./git_overview.md).


## What to do

1. Navigate to **your** GitHub repo in your browser.
1. Above the file list on the left hand side, click on the **New Pull Request** button:<br>
![New Pull Request Button](images/new-pull-request-icon.png)
1. GitHub will allow you to confirm which changes in your repo you want to share with the original author, as shown in the following image.
   * **NOTE**: GitHub transfers you to the repo of the original author
   * You will **no longer** be on your own GitHub account page.
1. Before proceeding, you should check for the following items.
  * Confirm that the **base fork** is the original author's fork
  * Confirm that the **head fork** is your fork
  * Confirm that GitHub says: **Able to merge** (IF there are conflicts, refer to the [Git Overview](./lesson_05_git_overview.md) for instructions on how to fix this problem.<br>
![Create Pull Request One](images/create-pull-request-one.png)
1. Click on the **Create pull request** button
1. Follow these steps to prep the Pull Request for creation:
    * Write a Summary Title describing your changes (~50 characters or so)
    * Write a brief Description of what you're changing in this pull request. Your description should be clear and concise and should help the upstream developers understand your submission. They are often busy and may get a lots of pull requests. Help them understand why your work should be included in their project.
    * Click on the **Create pull request** button<br>
![Create Pull Request Two](images/create-pull-request-two.png)

**REMINDER**:  Once you do these steps, GitHub leaves you on the upstream GitHub repo (Chalmer Lowe's in this case) and not your own!

![green sticky note](images/Sticky-Note-02-Green-300px.png)


## The big picture

As shown here, your repo has changes that need to be advertised to the upstream owner. GitHub uses the concept of a Pull Request to do this.

![Pull Request](images/git_pull_request.png)

When you submit a Pull Request, the upstream owner will get a notification in GitHub and can then review all your suggested changes.

If they agree with and approve your **suggested changes** they will merge the changes into their project. We emphasize suggested changes, because that is what they are... you are providing a suggestion. Upstream authors:

* are under no obligation to accept your suggestions
* may reject your suggestions outright
* may take their sweet old time in incorporating those changes
* may ask you to go back and make further revisions before accepting your changes
* may accept them immediately
* may not do anything at all

When a pull request is incorporated, your changes get included in the upstream repo, as shown below and are now available for others to see!

Congratulations!

![Merge](images/github_merge.png)

## Deep dive

N/A


## Resources

* [<resource name>](<resource url>)
* [<resource name>](<resource url>)

<!-- begin auto-generated nav-links section -->
| Previous | Up | Next |
|:---------|:---:|-----:|
| [GitHub Concepts](./github_concepts.md) | [Using GitHub](./github_overview.md) | [Table of Contents](./README.md) |
<!-- end auto-generated section -->
