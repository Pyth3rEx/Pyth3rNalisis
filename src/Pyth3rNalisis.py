#imports
import sys
import os
import argparse
import modules.module_log as module_log
import modules.module_banner as module_banner
import modules.worker_metadata as worker_metadata
import modules.worker_extension as worker_extension
import modules.worker_hashingAnalisis as worker_hashingAnalisis
import modules.worker_entropy as worker_entropy

#constants
version = '0.0.4'

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
parser.add_argument("-E", "--entropy", action='store_true', help="Check for unusal entropy in file")
parser.add_argument("-H", "--hashing", action='store_true', help="Perform hashing analisis on the file")
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
    print('\033[91m==================\033[0m')
    print('\033[92mEXTENSION ANALISIS:\033[0m')
    worker_extension.check_file_type(args.file)

# Handle hashing analysis
if args.hashing:
    print('\033[91m==================\033[0m')
    print('\033[92mHASHING ANALISIS:\033[0m')
    worker_hashingAnalisis.perform_hashing_analisis(args.file)

# Handle metadata analysis
if args.metadata:
    print('\033[91m==================\033[0m')
    print('\033[92mMETADATA ANALISIS:\033[0m')
    worker_metadata.check_metadata(args.file)

#Handle entropy analysis
if args.entropy:
    print('\033[91m==================\033[0m')
    print('\033[92mENTROPY ANALISIS:\033[0m')
    worker_entropy.check_entropy(args.file)