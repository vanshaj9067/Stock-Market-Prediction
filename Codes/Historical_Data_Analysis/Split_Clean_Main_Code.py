"""
Author: Madhurima Rawat

Script to clean a Streamlit app by removing all top-level functions except 'main'.
Preserves:
- All import statements
- Global variables
- Top-level code (outside functions)
- The 'main' function (if present)

Removes both the function and the comment immediately above it.

Saves the result as 'app_cleaned.py'.
"""

import ast
import black  # Import black for automatic Python code formatting

# For Local
# INPUT_FILE = "Streamlit_app_local_combined.py"
# CLEANED_FILE = "Streamlit_app_local.py"

# For Deployed
INPUT_FILE = "Streamlit_app_combined.py"
CLEANED_FILE = "Streamlit_app.py"

# Read source
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    source = f.read()

lines = source.splitlines()
tree = ast.parse(source)

# Identify non-main function lines to remove, including function header comments
lines_to_remove = set()
for node in tree.body:
    if isinstance(node, ast.FunctionDef) and node.name != "main":
        # Add the function comment above it and the function itself to the removal list
        comment_line = node.lineno - 2
        if 0 <= comment_line < len(lines):
            lines_to_remove.add(comment_line)
        for i in range(node.lineno - 1, node.end_lineno):
            lines_to_remove.add(i)

# Generate cleaned lines by excluding the lines marked for removal
cleaned_lines = [line for i, line in enumerate(lines) if i not in lines_to_remove]

# Join cleaned lines into a single string and format it with black
cleaned_code = "".join(line + "\n" for line in cleaned_lines)
formatted_code = black.format_str(cleaned_code, mode=black.FileMode())

# Write the formatted code to the cleaned file
with open(CLEANED_FILE, "w", encoding="utf-8") as f:
    f.write(formatted_code)

print(
    f"✅ Cleaned and formatted file saved as '{CLEANED_FILE}' (only 'main' retained, function comments removed)."
)
