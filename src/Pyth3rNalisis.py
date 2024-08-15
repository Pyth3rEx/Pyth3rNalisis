#imports
import sys
import os
import argparse
from tabulate import tabulate
import modules.module_log as module_log
import modules.module_banner as module_banner
import modules.worker_metadata as worker_metadata
import modules.worker_extension as worker_extension

#constants
version = '0.0.2'

# Custom ArgumentParser class
class CustomArgumentParser(argparse.ArgumentParser):
    def print_help(self, file=None):
        module_banner.printBanner(version)  # Print the banner
        super().print_help(file)  # Call the default print_help()

# Argument parsing with custom parser
parser = CustomArgumentParser(
    prog='Pyth3rNalisis',
    description='Pyth3rNalisis is a malware analysis tool that searches for red flags in any file. [NOT A REPLACEMENT FOR AV!!!!]'
)
parser.add_argument("-f", "--file", help="File to check")
parser.add_argument("-e", "--extension", action='store_true', help="Check for extension anomaly")
parser.add_argument("-m", "--metadata", action='store_true', help="Check for metadata anomaly")
args = parser.parse_args()

module_banner.printBanner(version)  # Print the banner

# Check if a file path argument is provided
if not args.file:
    module_log.critical('No file specified, quitting')
    sys.exit(1) # Exit the program with a non-zero status to indicate an error
elif not os.path.isfile(args.file):
    module_log.critical(f"File '{args.file}' specified does not exist, quitting")
    sys.exit(1) # Exit the program with a non-zero status to indicate an error
else:
    # Recursively check if any flags are specified
    flags_provided = any(value for key, value in vars(args).items() if key != 'file')
    
    if not flags_provided:
        module_log.critical('No analysis flags specified, quitting')
        sys.exit(1)  # Exit the program with a non-zero status to indicate an error

# Handle extension analysis
if args.extension:
    declared_file_extension, magic_file_type, detected_file_type = worker_extension.check_file_type(args.file)

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
    print('==================')
    print('EXTENSION ANALISIS:')
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

# Handle metadata analysis
if args.metadata:
    metadata_results = worker_metadata.check_metadata(args.file)

    # Printing the table
    print('==================')
    print('METADATA ANALISIS:')
    if metadata_results:
        headers = ["Metadata Attribute", "Value"]
        print(tabulate(metadata_results, headers=headers, tablefmt="fancy_grid"))
    else:
        module_log.critical('No data returned')