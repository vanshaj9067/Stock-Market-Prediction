"""
This script traverses a specified directory and its subdirectories to find files with spaces 
in their filenames and replaces those spaces with underscores. The script is particularly 
useful for ensuring filenames are compatible with systems or tools that do not handle spaces 
well in file paths.

Modules used:
--------------
- os: 
  The `os` module is part of Python's standard library and is used here for:
  1. Navigating the file system with `os.walk`, which generates file and directory names 
     in a directory tree.
  2. Manipulating file paths using `os.path.join`.
  3. Renaming files using `os.rename`.

Code functionality:
--------------------
1. A directory path is provided as the `directory` variable. 
2. The `os.walk` function iterates through all subdirectories and files in the specified 
   directory tree.
3. For each file, the script checks if its name contains spaces.
4. If spaces are found, the script constructs the old and new file paths using `os.path.join`.
5. It then renames the file, replacing spaces with underscores using `str.replace`.
6. A message is printed for each renamed file, indicating the old and new filenames.
7. After processing all files, the script outputs a final message: "All files processed."

Usage:
------
1. Replace the `directory` variable with the desired directory path to be processed.
2. Run the script. It will handle renaming all applicable files and provide a log of changes made.
"""

# Importing Required Libraries
import os

# Directory to traverse
directory = "source_directory"

# Traverse through all files and subdirectories
for root, _, files in os.walk(directory):
    for filename in files:
        if " " in filename:  # Check if there's a space in the filename
            old_path = os.path.join(root, filename)
            new_filename = filename.replace(" ", "_")
            new_path = os.path.join(root, new_filename)

            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed '{filename}' to '{new_filename}'")

print("All files processed.")
