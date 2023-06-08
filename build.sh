#!/bin/bash

pip install virtualenv
virtualenv mypython
pip install -r requirements.txt

mkdocs build
cd site
git init
git remote add origin git@github.com:dipc-cc/hyperion-docs.git
git checkout -b new_branch
git rm --cached -r *
git add -A
git commit -m "Hyperion docs deploy"
git push origin new_branch
git checkout gh-pages
git pull origin gh-pages
git merge new_branch
git push origin gh-pages

git branch -d new_branch
git push origin --delete new_branch

