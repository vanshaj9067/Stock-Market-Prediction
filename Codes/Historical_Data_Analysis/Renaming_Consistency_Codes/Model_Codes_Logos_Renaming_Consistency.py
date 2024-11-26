"""

Libraries Used:

1. os (Standard Library):
   - Provides functions for interacting with the operating system, including file and directory manipulation.
   - Used for:
     - `os.path.abspath()`: To get the absolute path of the directories.
     - `os.makedirs()`: To create directories if they don't already exist.
     - `os.path.exists()`: To check if a path exists.
     - `os.listdir()`: To list the files in a directory.
     - `os.path.join()`: To join paths in a way that is safe across different operating systems.

2. shutil (Standard Library):
   - Provides a higher-level interface for file operations such as copying, moving, and removing files and directories.
   - Used for:
     - `shutil.move()`: To move files from one location to another. In this script, it is used to move and rename files based on the logic.

This script processes files from a source directory, renames them based on stock abbreviations, and moves them to respective destination folders.

The script assumes the following structure:
- The source directory contains model files (e.g., `.ipynb`) and logo files (e.g., `.jpg`, `.png`, `.gif`).
- The stock names are mapped to their abbreviations via `abbreviation_mapping` dictionary (e.g., "Amazon" is mapped to "AMZN").
- The files are renamed based on the stock abbreviation and moved into specific folders:
  - Model files are moved to "Model Codes" folder.
  - Logo files are moved to "Logos" folder.
- If logo files have duplicate names, they are renamed by appending a count to ensure uniqueness.

The script does the following:
1. Defines the source and destination directories.
2. Creates the necessary destination directories if they don't exist.
3. Maps stock names to abbreviations using a dictionary.
4. Processes each file in the source directory:
    - If the file is a notebook, it renames it using the stock abbreviation and moves it to the "Model Codes" folder.
    - If the file is a logo, it renames it and ensures uniqueness before moving it to the "Logos" folder.
    - Skips files that don't match the supported formats (notebooks or image files).

Usage:
- Make sure the source directory path is correctly defined.
- This script will rename and move files automatically based on the mappings and logic defined.
"""

# Importing Required Libraries
import os
import shutil

# Define source and destination directories
source_dir = os.path.abspath("source_directory")  # Actual source directory
renamed_models_dir = os.path.abspath("Output_directory")
model_codes_dir = os.path.abspath("Output_directory")
logos_dir = os.path.join(renamed_models_dir, "Output_directory_Logos")

# Create destination directories if they don't exist
os.makedirs(model_codes_dir, exist_ok=True)
os.makedirs(logos_dir, exist_ok=True)

# Abbreviation mapping for stock names
abbreviation_mapping = {
    "Amazon": "AMZN",
    "Apple": "AAPL",
    "Google": "GOOG",
    "Meta": "META",
    "Microsoft": "MSFT",
    "Netflix": "NFLX",
    "Nvidia": "NVDA",
    "TCS": "TCS",
}

# Track file counts for naming duplicates
logo_counts = {}


def get_abbreviation(stock_name):
    """Return the abbreviation for the given stock name."""
    for full_name, abbr in abbreviation_mapping.items():
        if stock_name.lower() in full_name.lower():
            return abbr
    return stock_name  # Return original if no match found


def rename_and_move_stock_files(file_name, source_folder):
    """
    Rename and move stock-related files to the appropriate folders:
    - Model files are moved to 'Model Codes' folder.
    - Logo files are moved to 'Logos' folder.

    Parameters:
        file_name (str): Name of the file to be processed.
        source_folder (str): The source folder where the file is located.
    """
    # Identify stock name by first part of file name
    stock_name = file_name.split()[0]
    stock_abbreviation = get_abbreviation(stock_name)

    # For `.ipynb` files (notebooks)
    if file_name.endswith(".ipynb"):
        new_name = f"{stock_abbreviation} Stock Price Model.ipynb"
        dest_path = os.path.join(model_codes_dir, new_name)

    # For logo files (.jpg, .png, .gif)
    elif file_name.lower().endswith((".jpg", ".png", ".gif")):
        # Scrape the name and convert to Title Case, then append "_Logo"
        logo_base_name = os.path.splitext(file_name)[0].title()  # Capitalize the name
        logo_new_name = f"{logo_base_name}_Logo{os.path.splitext(file_name)[1]}"
        dest_path = os.path.join(logos_dir, logo_new_name)

        # Ensure unique file names if needed
        count = logo_counts.get(logo_base_name, 0)
        while os.path.exists(dest_path):  # Check for existing file
            count += 1
            logo_new_name = (
                f"{logo_base_name}_Logo_{count}{os.path.splitext(file_name)[1]}"
            )
            dest_path = os.path.join(logos_dir, logo_new_name)

        logo_counts[logo_base_name] = count

    else:
        # Skip files that don't match the required formats
        print(f"Skipped file: {file_name} (not a model or logo file)")
        return

    # Move and rename the file
    shutil.move(os.path.join(source_folder, file_name), dest_path)
    print(
        f"Renamed and moved: {file_name} -> {logo_new_name if file_name.lower().endswith(('.jpg', '.png', '.gif')) else new_name}"
    )


# Process all files in the source directory
for file_name in os.listdir(source_dir):
    rename_and_move_stock_files(file_name, source_dir)
