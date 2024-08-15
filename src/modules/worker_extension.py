#imports
import magic
import filetype
import os
import modules.module_log as module_log
from tabulate import tabulate

def get_file_type_via_magic(file_path):
    try:
        # Create a Magic object
        mime = magic.Magic()
        
        # Get the file type
        magic_file_type = mime.from_file(file_path)
        return magic_file_type
    
    except Exception as e:
        module_log.warning(f"Unable to determine the file type via magic number: {e}")
        return None
    
def get_file_type_via_filetype(file_path):
    try:
        # Guess the file type
        kind = filetype.guess(file_path)
        if kind is None:
            module_log.warning(f"Cannot determine the file type for '{file_path}' via filetype")
            return None

        return kind.mime, kind.extension
    
    except Exception as e:
        module_log.warning(f"Unable to determine the file type via filetype: {e}")
        return None

def check_file_type(file_path):
    _, declared_file_extension = os.path.splitext(file_path)
    magic_file_type = get_file_type_via_magic(file_path)
    detected_file_type = get_file_type_via_filetype(file_path)

    # Prepare data for output (assuming you have the previous table display code)
    headers = ["Check", "Result"]
    data = [
        ["Declared Extension", declared_file_extension or "\033[91mNone\033[0m"],  # Overline in red
        ["Magic File Type", magic_file_type or "\033[91mNone\033[0m"],             # Overline in red
        ["Detected File Type", detected_file_type or "\033[91mNone\033[0m"],       # Overline in red
    ]

    if 'data' == str(magic_file_type):
        data[1][1] = f"\033[91m{magic_file_type}\033[0m" # Overline in red

    # Printing the table
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))