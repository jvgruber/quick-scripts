#!/bin/bash

# Check if the directory argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 directory"
    exit 1
fi

directory="$1"

# Check if the directory exists
if [ ! -d "$directory" ]; then
    echo "Directory '$directory' not found."
    exit 1
fi

# Loop through files in the directory
for file in "$directory"/*; do
    if [ -f "$file" ]; then
        # Extract file name and extension
        filename=$(basename "$file")
        extension="${filename##*.}"
        filename="${filename%.*}"

        # Replace whitespaces with dashes and convert to lowercase
        new_filename=$(echo "$filename" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')."$extension"

        # Rename the file
        if [ "$filename" != "$new_filename" ]; then
            mv "$file" "$directory/$new_filename"
            echo "Renamed '$filename.$extension' to '$new_filename'"
        fi
    fi
done
