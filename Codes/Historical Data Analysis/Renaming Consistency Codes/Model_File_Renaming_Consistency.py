"""
This script processes and renames model files based on a ticker symbol mapping, then moves them into
specific directories for .pkl and .joblib model files.

It performs the following tasks:
1. Renames model files according to predefined ticker symbols from a mapping.
2. Moves the renamed files to designated directories based on their file extensions.
3. Creates the required directories for .pkl and .joblib models if they don't exist.
4. Logs the operations performed on each file.

Libraries Used:
1. os (Standard Library):
   - Provides functions for interacting with the operating system, including file and directory manipulation.
   - Used for:
     - `os.path.abspath()`: To get the absolute path of directories.
     - `os.makedirs()`: To create directories if they don't exist.
     - `os.path.exists()`: To check if a path exists.
     - `os.listdir()`: To list files in a directory.
     - `os.path.join()`: To join paths in a way that is safe across different operating systems.
     - `os.path.splitext()`: To split a file name into its name and extension.
     
2. shutil (Standard Library):
   - Provides a higher-level interface for file operations such as copying, moving, and removing files and directories.
   - Used for:
     - `shutil.move()`: To move and rename files. In this script, it moves files from the source folder to the destination folder with new names based on the ticker symbol.
"""

import os
import shutil

# Define input and output directories
input_dir = os.path.abspath(
    "New_code_&_Model\Models"
)  # Directory containing the model files
output_dir = os.path.abspath(
    "Renamed Models"
)  # Destination directory for renamed files

# Define separate folders for .pkl and .joblib files within the output directory
pkl_dir = os.path.join(output_dir, "pkl_models")
joblib_dir = os.path.join(output_dir, "joblib_models")

# Create destination folders if they don't already exist
os.makedirs(pkl_dir, exist_ok=True)
os.makedirs(joblib_dir, exist_ok=True)

# Define mapping of file prefixes to standardized ticker symbols
# Each key represents part of the prefix in the original file name, and the value is the standardized ticker symbol
ticker_mapping = {
    "META": "META",
    "Google": "GOOG",
    "MSFT": "MSFT",
    "Netflix": "NFLX",
    "Nvidia": "NVDA",
    "TCS": "TCS",
    "Apple": "AAPL",
    "Amazon": "AMZN",
}


def rename_and_move(file_name, source_folder, dest_folder, ticker_mapping):
    """
    Renames a file based on a ticker mapping and moves it to the specified destination folder.

    Parameters:
        file_name (str): The original name of the file.
        source_folder (str): The directory where the original file is located.
        dest_folder (str): The directory to move the renamed file to.
        ticker_mapping (dict): A dictionary mapping name prefixes to standardized ticker symbols.

    Returns:
        bool: True if the file was renamed and moved, False if no matching prefix was found.

    Functionality:
        - Iterates over each name prefix and corresponding ticker symbol in the mapping.
        - If a file name contains a prefix (e.g., "Google" or "Netflix"), the function renames the file to include the corresponding ticker symbol.
        - Moves the file to the appropriate destination folder (either pkl_models or joblib_models) and prints the operation performed.
        - If no match is found, returns False, indicating the file wasn't renamed and moved.
    """
    # Iterate over each name prefix and corresponding ticker symbol in the mapping
    for name_prefix, ticker in ticker_mapping.items():
        # Check if the file name contains the prefix (e.g., "Google" or "Netflix")
        if name_prefix.lower() in file_name.lower():
            # Create the new standardized file name based on the ticker and file extension
            new_name = f"{ticker}_Ensemble_Model{os.path.splitext(file_name)[1]}"
            # Move the file to the destination folder with the new name
            shutil.move(
                os.path.join(source_folder, file_name),
                os.path.join(dest_folder, new_name),
            )
            print(f"Renamed and moved: {file_name} -> {new_name}")
            return True  # File successfully renamed and moved
    return False  # No matching prefix was found


# Process files in the input directory
for file_name in os.listdir(input_dir):
    # Process .pkl files: rename and move them to the pkl_dir if they match the expected format
    if file_name.endswith(".pkl"):
        if not rename_and_move(file_name, input_dir, pkl_dir, ticker_mapping):
            print(f"Skipped file: {file_name} (does not match expected format)")

    # Process .joblib files: rename and move them to the joblib_dir if they match the expected format
    elif file_name.endswith(".joblib"):
        if not rename_and_move(file_name, input_dir, joblib_dir, ticker_mapping):
            print(f"Skipped file: {file_name} (does not match expected format)")

    # Skip any files that are not .pkl or .joblib models
    else:
        print(f"Skipped file: {file_name} (not a model file)")
