#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 2]; then
   echo "Usage: ./script.sh <file> <directory>"
   exit 1
fi 

# Assign the arguments to variables
file=$1
dir=$2

# Validate the directory
if [ ! -d "$dir" ]; then
   echo "Directory $dir does not exist."
   exit 1
fi 

# Read the file line by line and download each URL
while IFS= read -r url
do 
  wget -P "$dir" "$url"
done < "$file"  
