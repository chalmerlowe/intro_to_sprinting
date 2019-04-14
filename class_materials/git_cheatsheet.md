


# Git Cheatsheet

## When starting a project

|Command|Comment|Reference
|:---|:---|:---|
|`git clone [url]`|downloads a copy of the repository from the given url (typically **your** GitHub repo)||
|<code>git&nbsp;remote&nbsp;add&nbsp;[alias]&nbsp;[url]</code><br>`git remote add upstream [url]`|adds an alias (often 'upstream') for a remote repository (repo) located at the `url` (the `upstream` repo will generally be the main project repo on GitHub)||

## When editing a project

|Command|Comment|Reference|
|:---|:---|:---|
|`git status`|shows files and the status of the local git repo (i.e. staged for next commit, modified, etc. Also shows frequently used commands to take you to the next step) ||
|`git add [file]`<br>`git add [file] [file] [file]`|add a file to the staging area in preparation for commit||
|`git commit -m "[descriptive msg]"`|commit your staged content||
|`git checkout -b [branchname]`|create a new branch||
|`git checkout master`|checkout the `master` branch||
|`git merge [branchname]`|merge the specified branch into the current branch (often `master`)||
|`git push [alias] [branch]`<br>`git push origin master`|push the committed changes in the branch (often `master`) to the matching branch on the repo represented by the alias (often `origin` ||
|`git branch -d [branchname]`|delete a branch after it has been successfully merged||
||||
