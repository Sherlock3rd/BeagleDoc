@echo off
git --no-pager status > git_output.txt
git add .
git commit -m "docs: publish - update cp2/cp3 scope and cp2 timeline curve" >> git_output.txt
git push >> git_output.txt
git --no-pager status >> git_output.txt
