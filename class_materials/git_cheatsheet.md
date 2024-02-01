


# Git Cheatsheet

## When starting a project

|Command|Comment|Reference
|:---|:---|:---|
|<code>git&nbsp;clone&nbsp;[url]</code>|downloads a copy of the repository from the given url (typically **your** GitHub repo)|[Cloning a Repository](./git_cloning.md)|
|<code>git&nbsp;remote&nbsp;add&nbsp;[alias]&nbsp;[url]</code><br><code>git&nbsp;remote&nbsp;add&nbsp;upstream&nbsp;[url]</code>|adds an alias (often 'upstream') for a remote repository (repo) located at the `url` (the `upstream` repo will generally be the main project repo on GitHub)|[Cloning a Repository](./git_cloning.md)|

## When editing a project

| Command                                                                                                   | Comment                                                                                                                                                         |Reference|
|:----------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|:---|
| <code>git&nbsp;status</code>                                                                              | shows files and the status of the local git repo (i.e. staged for next commit, modified, etc. Also shows frequently used commands to take you to the next step) |[Git Primary Workflow: Add, Commit, Push](./git_main_lifecycle.md)|
| <code>git&nbsp;add&nbsp;[file]</code><br><code>git&nbsp;add&nbsp;[file]&nbsp;[file]&nbsp;[file]</code>    | add a file to the staging area in preparation for commit                                                                                                        |[Git Primary Workflow: Add, Commit, Push](./git_main_lifecycle.md)|
| <code>git commit&nbsp;-m&nbsp;"[msg]"</code>                                                              | commit your staged content                                                                                                                                      |[Git Primary Workflow: Add, Commit, Push](./git_main_lifecycle.md)|
| <code>git&nbsp;checkout&nbsp;-b&nbsp;[branchname]</code>                                                  | create a new branch                                                                                                                                             |[Branching and Merging](./git_branch_merge.md)|
| <code>git&nbsp;checkout&nbsp;main</code>                                                                  | checkout the `main` branch                                                                                                                                      |[Branching and Merging](./git_branch_merge.md)|
| <code>git&nbsp;merge&nbsp;[branchname]</code>                                                             | merge the specified branch into the current branch (often `main`)                                                                                               |[Branching and Merging](./git_branch_merge.md)|
| <code>git&nbsp;push&nbsp;[alias]&nbsp;[branch]</code><br><code>git&nbsp;push&nbsp;origin&nbsp;main</code> | push the committed changes in the branch (often `main`) to the matching branch on the repo represented by the alias (often `origin`)                            |[Git Primary Workflow: Add, Commit, Push](./git_main_lifecycle.md)|
| <code>git&nbsp;branch&nbsp;-d&nbsp;[branchname]</code>                                                    | delete a branch after it has been successfully merged                                                                                                           ||
|                                                                                                           |                                                                                                                                                                 ||
