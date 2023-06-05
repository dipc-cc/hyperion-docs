# Hyperion Technical Documentation

## Making changes in the repository 

First of all ownload the Git repository

```
git clone git@github.com:dipc-cc/hyperion-docs.git
```

To make changes in the repositoy. First create a new branch inside the `hyperion-docs` directory:

```
git checkout -b new_branch

```

After making all needed changes run the following command to apply the changes:

```
git add -A
git commit -m "Description about the modifications"
git push origin new_branch
git checkout main
git pull origin main
git merge new_branch
git push origin main
```

Delete the branch used to make changes

```
git branch -d new_branch
git push origin --delete new_branch
```


## Deploy Webpage


Change to `hyperion-docs` directory and run the `build.sh` script

