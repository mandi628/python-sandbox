#!/bin/bash

cd ~/repos/my_sandbox

git status

git add .

echo "Please enter commit message: "
read msg

git commit -m "$msg"

git push
