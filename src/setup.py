from setuptools import setup, find_packages
import os

# Function to read the requirements.txt file
def parse_requirements(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        # Filter out comments and empty lines
        requirements = [line for line in lines if line and not line.startswith('#')]
    return requirements

# Specify the path to requirements.txt
requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')

setup(
    name='Pyth3rNalisis',
    version='0.0.1',
    description='Pyth3rNalisis is a malware analisis tool that search for red flags in any file.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Pyth3rEx',
    author_email='',
    url='https://github.com/Pyth3rEx/Pyth3rNalisis',
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=parse_requirements(requirements_path),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)
