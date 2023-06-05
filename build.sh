#!/bin/bash

pip install virtualenv
virtualenv mypython
pip install -r requirements.txt

mkdocs build
cd site
git init
git remote add origin git@github.com:dipc-cc/hyperion-docs.git
git checkout -b gh-pages
git rm --cached -r * 
git add -A
git commit -m "Hyperion docs deploy"
git push origin gh-pages
