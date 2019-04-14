


# Git Cheatsheet

## When starting a project

|Command|Comment|Reference
|:---|:---|:---|
|<code>git clone [url]</code>|downloads a copy of the repository from the given url (typically **your** GitHub repo)||
|<code>git&nbsp;remote&nbsp;add&nbsp;[alias]&nbsp;[url]</code><br><code>git remote add upstream [url]</code>|adds an alias (often 'upstream') for a remote repository (repo) located at the `url` (the `upstream` repo will generally be the main project repo on GitHub)||

## When editing a project

|Command|Comment|Reference|
|:---|:---|:---|
|<code>git status</code>|shows files and the status of the local git repo (i.e. staged for next commit, modified, etc. Also shows frequently used commands to take you to the next step) ||
|<code>git add [file]</code><br><code>git add [file] [file] [file]</code>|add a file to the staging area in preparation for commit||
|<code>git commit -m "[descriptive msg]"</code>|commit your staged content||
|<code>git checkout -b [branchname]</code>|create a new branch||
|<code>git checkout master</code>|checkout the `master` branch||
|<code>git merge [branchname]</code>|merge the specified branch into the current branch (often `master`)||
|<code>git push [alias] [branch]</code><br><code>git push origin master</code>|push the committed changes in the branch (often `master`) to the matching branch on the repo represented by the alias (often `origin` ||
|<code>git branch -d [branchname]</code>|delete a branch after it has been successfully merged||
||||
