<!-- begin auto-generated title section -->
# Submitting a Pull Request
<!-- end auto-generated section -->


## Time-box

5 Minutes


## Overview

Once you have a change OR changes pushed to your GitHub repo, you will want to share those changes with the owner of the upstream project repository.


<div style="background-color: #eaea8d; border: 2px solid #0e0e0e; padding: 5px; color:#0e0e0e">
  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px;">
    <path d="M4 2v20h16V2H4zm16 2l-8 5-8-5M4 6l8 5 8-5" />
  </svg>
 <b>NOTE:</b> This lesson presumes that your changes have been pushed to <b>your own</b> GitHub repo (instructions on how to do this were covered in a previous lesson.

</div>
<br>


## What to do

1. Navigate to **your** GitHub repo in your browser.
1. Click on the Branch Dropdown button.
1. Select the branch you want to examine: in this case, the `conflict-merge` branch
1. Click the **Pull Request** link to issue a pull request
![New Pull Request Button](images/new-pull-request-icon.png)
1. GitHub will allow you to confirm which changes in your repo you want to share with the original author, as shown in the following image.
   * You will **no longer** be on your own GitHub account page.
<div style="background-color: #eaea8d; border: 2px solid #0e0e0e; padding: 5px; color:#0e0e0e">
  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px;">
    <path d="M4 2v20h16V2H4zm16 2l-8 5-8-5M4 6l8 5 8-5" />
  </svg>
 <b>NOTE:</b> GitHub transfers you to the repo of the original author

</div>
<br>
1. Before proceeding, you should check for the following items.
  * Confirm that the **base branch** is the original author's branch
  * Confirm that the **compare branch** is your branch
  * Confirm that GitHub says: **Able to merge** (IF there are conflicts, refer to the [Git Overview](./lesson_05_git_overview.md) for instructions on how to fix this problem.<br>
![Create Pull Request One](images/create-pull-request-one.png)
1. Follow these steps to prep the Pull Request for creation:
    * Write a Summary Title describing your changes (~50 characters or so)
    * Write a brief Description of what you're changing in this pull request. Your description should be clear and concise and should help the upstream developers understand your submission. They are often busy and may get a lots of pull requests. Help them understand why your work should be included in their project.
1. Click on the **Create pull request** button

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

* [GitHub - Contributing to a Project](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project)

<!-- begin auto-generated nav-links section -->
| Previous | Up | Next |
|:---------|:---:|-----:|
| [GitHub Concepts](./github_concepts.md) | [Using GitHub](./github_overview.md) | [Working with Real Projects](./projects_with_code.md) |
<!-- end auto-generated section -->
