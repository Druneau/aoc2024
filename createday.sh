#!/bin/bash

# Use the current day of the month if no argument is provided
if [ "$#" -eq 0 ]; then
    ARG=$(date +'%d')
else
    ARG=$1
fi

# Remove leading zero for single-digit days (optional, if you don't want "day01" but "day1")
ARG=$(echo "$ARG" | sed 's/^0*//')

# Create a folder with prefix "day" followed by the argument
FOLDER="day$ARG"
mkdir -p "$FOLDER"

# Create the files in the folder
touch "$FOLDER/day${ARG}.py"
touch "$FOLDER/test_day${ARG}.py"
touch "$FOLDER/input.txt"
touch "$FOLDER/input_example.txt"

# Confirmation message
echo "Created $FOLDER/ with files"