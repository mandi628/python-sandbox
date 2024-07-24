#!/bin/bash

echo "Enter the file you want to copy: "
read oldFile

chmod -x $oldFile

echo "Enter the new bash file name: "
read newBash

cp $oldFile ../../bash/bash-by-example/$newBash

echo "Enter the new ruby file name: "
read newRuby

cp $oldFile ../../ruby/ruby-by-example/$newRuby

echo "Enter the new JS file name: "
read newJS

cp $oldFile ../../js/js-by-example/$newJS

chmod +x $oldFile
