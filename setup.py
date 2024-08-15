from setuptools import setup, find_packages
import os

# Function to read the requirements.txt file
def parse_requirements(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        # Filter out comments and empty lines
        requirements = [line for line in lines if line and not line.startswith('#')]
    return requirements

# Get the absolute path to the current directory (where setup.py is located)
current_dir = os.path.abspath(os.path.dirname(__file__))

# Compute the absolute path to the README.md file (located one directory above the current one)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
readme_path = os.path.join(parent_dir, 'README.md')

# Read the long description from the README.md file
with open(readme_path, 'r') as fh:
    long_description = fh.read()

setup(
    name='Pyth3rNalisis',
    version='0.0.1',
    description='Pyth3rNalisis is a malware analysis tool that searches for red flags in any file.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Pyth3rEx',
    author_email='',  # Replace with a real email if necessary
    url='https://github.com/Pyth3rEx/Pyth3rNalisis',
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=parse_requirements(os.path.join(current_dir, 'src/requirements.txt')),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)
