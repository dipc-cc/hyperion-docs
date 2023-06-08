# Hyperion Technical Documentation

This repository contains Hyperion HPC technical documentation written in markdown and processed wit hmkdocs static site generator. The documentation pages are found in the top-level folder docs.

# Contributing

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

Provisionally, github pages will be used to serve the web page. To modify it, first download the repository and make the changes.

```
git clone git@github.com:dipc-cc/hyperion-docs.git
```

Go to `hyperion-docs` directory and run the `build.sh` script. 

