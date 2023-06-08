# Hyperion Technical Documentation

This repository contains Hyperion HPC technical documentation written in markdown and processed wit hmkdocs static site generator. The documentation pages are found in the top-level folder docs.

# Contributing

## Making changes in the repository 

First of all ownload the Git repository

```
git clone git@github.com:dipc-cc/hyperion-docs.git
```

After making all needed changes run the following command to apply the changes:

```
git add -A
git commit -m "Description about the modifications"
git push origin master
```

Every time a push is made to the `master` branch, a github actions process will be activated, which will be in charge of deploying the web page.

If you need to make changes to the GitHub Actions configuration, edit the deploy_webpage.yml file in the `.github/workflows` directory


