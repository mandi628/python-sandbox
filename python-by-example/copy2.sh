#!/bin/bash

echo "Enter the file you want to copy: "
read oldFile

chmod -x $oldFile

echo "Enter the new file name (with no filetype): "
read newFile

cp $oldFile ../../my_sandbox/bash/bash-by-example/$newFile.sh
cp $oldFile ../../my_sandbox/ruby/ruby-by-example/$newFile.rb
cp $oldFile ../../js-sandbox/js-by-example/$newFile.js

chmod +x $oldFile

# This new version requires less typing. It still copies the file to the required folders,
# but it automatically adds the filetype. Not sure how to automatically remove the ".py"
# from the original filename yet.
