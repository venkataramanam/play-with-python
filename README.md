<style>
H1{color:Blue !important;}
H2{color:DarkOrange !important;}
p{color:Black !important;}
</style>

# play-with-python
My tryst with Python

## Recommended Git development workflow

We prefer the developers to use the [Git Forking Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow)

See the concise set of instructions below to adopt the workflow.

```
1. Fork repository from browser

2. Clone fork on your desktop
git clone fork_git_url

3. Add upstream repository
git remote add upstream original_git_url

4. Create a branch
git checkout -b new feature branch

See which branch you are on
git branch

Switch branch
git checkout new feature branch

5. Start making changes and commits into new feature branch
git add -A
git commit -m commit message

** If the official upstream master has moved forward, pull those changes
into local master and merge in your branch
git pull upstream master

Merge with these steps..

A)
git checkout new feature branch
git merge master

Merge the conflicts and again commit

6. Push the changes in local branch to remote fork
git push origin new feature branch

7. Raise a PR from browser from your new feature branch

Synching Remote Fork

git pull upstream master
git push origin master

Note that in forking workflow, you will never push directly to remote fork.
The status on the remote fork should always read _'The branch is even with dataconnect:master'_

8. After the feature branch work is done, delete the feature branch

Delete local branch
git branch -D new feature branch

Delete remote branch
git push -d origin new feature branch

NOTE -
'origin' stands for remote forked repo
'upstream' stands for remote original repo
git push and pull accept REMOTE and BRANCH like...
git pull upstream branch_name
git push origin branch_name

```
