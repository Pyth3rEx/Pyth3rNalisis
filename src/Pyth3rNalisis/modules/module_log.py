import logging
import os
from colorama import init, Fore, Style, Back

# Initialize colorama
init(autoreset=True)

# Basic configuration for logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Pyth3rNalisis')

# Stop propagating to the root logger
logger.propagate = False

# Create a file handler
directory = "logs"
os.makedirs(directory, exist_ok=True)  # Create the directory if it does not exist
file_handler = logging.FileHandler('logs/Pyth3rNalisis.log')
file_handler.setLevel(logging.DEBUG)  # Set the logging level for the file handler

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Set the logging level for the console handler

# Create a custom formatter that includes colors for the log level names
class CustomFormatter(logging.Formatter):
    def format(self, record):
        # Define color codes based on the log level
        if record.levelno == logging.DEBUG:
            levelname_color = f"{Fore.BLUE}{record.levelname}{Style.RESET_ALL}"
        elif record.levelno == logging.INFO:
            levelname_color = f"{Fore.GREEN}{record.levelname}{Style.RESET_ALL}"
        elif record.levelno == logging.WARNING:
            levelname_color = f"{Fore.YELLOW}{record.levelname}{Style.RESET_ALL}"
        elif record.levelno == logging.ERROR:
            levelname_color = f"{Fore.RED}{record.levelname}{Style.RESET_ALL}"
        elif record.levelno == logging.CRITICAL:
            levelname_color = f"{Back.RED}{Fore.WHITE}{record.levelname}{Style.RESET_ALL}"
        else:
            levelname_color = record.levelname
        
        # Replace the original levelname with the colored one
        record.levelname = levelname_color
        return super().format(record)

# Use the custom formatter for the console handler
console_formatter = CustomFormatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# Set the standard formatter for the file handler
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Defining functions for public use
def debug(stringToPrint):
    logger.debug(str(stringToPrint))

def info(stringToPrint):
    logger.info(str(stringToPrint))

def warning(stringToPrint):
    logger.warning(str(stringToPrint))

def error(stringToPrint):
    logger.error(str(stringToPrint))

def critical(stringToPrint):
    logger.critical(str(stringToPrint))

# # Usage:
# import modules.module_log as module_log
# module_log.debug('text')
# module_log.info('text')
# module_log.warning('text')
# module_log.error('text')
# module_log.critical('text')