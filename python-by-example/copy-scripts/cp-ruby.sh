#!/bin/bash

echo "Enter the file you want to copy: "
read oldFile

echo "Enter the new file name: "
read newFile

cp $oldFile ../../ruby/ruby-by-example/$newFile
