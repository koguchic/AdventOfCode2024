#!/bin/bash

# Rename directories from 1-9 to 01-09 for all subdirectories
for parent_dir in */; do
    for sub_dir in "$parent_dir"[1-9]/; do
        # Remove trailing slash for renaming
        old_name="${sub_dir%/}"
        # Extract the parent directory and the current subdirectory name
        base_name=$(basename "$old_name")
        parent_path=$(dirname "$old_name")
        
        # Rename to add leading zero
        if [[ "$base_name" =~ ^[1-9]$ ]]; then
            new_name=$(printf "%02d" "$base_name")
            mv "$old_name" "$parent_path/$new_name"
            echo "Renamed $old_name to $parent_path/$new_name"
        fi
    done
done

echo "Renaming completed!"

