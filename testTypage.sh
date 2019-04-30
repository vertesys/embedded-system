#!/bin/bash

# Install mypy
# pip install mypy --upgrade --user

# Git branch
git checkout devpy

# Workdir is temp directory
mkdir tmpopo
cd tmpopo

# List all py files recursively in target directory
target_dir=/home/pi/robot
echo '--- Test typage du dossier' $target_dir '---'
target_files=$(find $target_dir -type f -name "*.py*" > tmplist)

# html report can be generated only with files in the current directory
# copy all .py files in temp directory
while IFS='' read -r line || [[ -n "$line" ]]; do
	targ=$(echo $line)
	targ2=$(echo $targ | tr '/' ':')
	targ2="${targ2:1}"
	cp $targ ./$targ2
done < "tmplist"
find . -type f -name "*.py" > myfiles

# Generate report
report_folder=$(date +"%d-%m-%Y_%H:%M:%S")
mypy $(cat myfiles) --ignore-missing-imports --html-report ../$report_folder
scp -r -p -o StrictHostKeyChecking=no ../$report_folder ansibleuser@vps646618.ovh.net:/var/www/html/robot

cd ..
rm -r ./tmpopo
rm -r ./$report_folder
