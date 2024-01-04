# Get all py files from this folder

import os

def get_all_code():
    code = ""
    for file in os.listdir():
        if file.endswith(".py") and file != "get_all_code.py":
            code += "\n\n# " + file + "\n"
            with open(file, "r") as f:
                code += f.read()
    return code

# Copy in clipboard
import pyperclip
code = get_all_code()
pyperclip.copy(code)