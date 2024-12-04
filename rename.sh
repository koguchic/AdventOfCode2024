#!/bin/bash

# Fix intermediate directories and move contents up one level
for parent_dir in */; do
    for intermediate_dir in "$parent_dir"[0-9][0-9]/[1-9]/; do
        # Remove trailing slash for processing
        intermediate_path="${intermediate_dir%/}"
        parent_path=$(dirname "$intermediate_path")
        
        # Move contents of intermediate_dir to its parent
        mv "$intermediate_path"/* "$parent_path/"
        
        # Remove the now-empty intermediate directory
        rmdir "$intermediate_path"
        echo "Fixed intermediate directory: $intermediate_path"
    done
done

echo "Intermediate directories fixed!"

