


# Git Cheatsheet

## When starting a project

|Command|Comment|Reference
|:---|:---|:---|
|<code><nobr>git clone [url]</nobr></code>|downloads a copy of the repository from the given url (typically **your** GitHub repo)||
|<code><nobr>git remote add [alias] [url]</nobr></code><br><code><nobr>git remote add upstream [url]</nobr></code>|adds an alias (often 'upstream') for a remote repository (repo) located at the `url` (the `upstream` repo will generally be the main project repo on GitHub)||

## When editing a project

|Command|Comment|Reference|
|:---|:---|:---|
|<nobr>`git status`|shows files and the status of the local git repo (i.e. staged for next commit, modified, etc. Also shows frequently used commands to take you to the next step) ||
|<nobr>`git add [file]`</nobr><br><nobr>`git add [file] [file] [file]`</nobr>|add a file to the staging area in preparation for commit||
|<nobr>`git commit -m "[descriptive msg]"`</nobr>|commit your staged content||
|<nobr>`git checkout -b [branchname]`</nobr>|create a new branch||
|<nobr>`git checkout master`</nobr>|checkout the `master` branch||
|<nobr>`git merge [branchname]`</nobr>|merge the specified branch into the current branch (often `master`)||
|<nobr>`git push [alias] [branch]`</nobr><br><nobr>`git push origin master`</nobr>|push the committed changes in the branch (often `master`) to the matching branch on the repo represented by the alias (often `origin` ||
|<nobr>`git branch -d [branchname]`</nobr>|delete a branch after it has been successfully merged||
||||
