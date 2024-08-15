from setuptools import setup, find_packages
import os

def parse_requirements(filename):
    with open(filename, 'r') as file:
        return [line for line in file.read().splitlines() if line and not line.startswith('#')]

current_dir = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(current_dir, 'README.md')

with open(readme_path, 'r') as fh:
    long_description = fh.read()

setup(
    name='Pyth3rNalisis',
    version='0.0.1',
    description='Pyth3rNalisis is a malware analysis tool that searches for red flags in any file.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Pyth3rEx',
    author_email='',
    url='https://github.com/Pyth3rEx/Pyth3rNalisis',
    packages=find_packages(),
    install_requires=parse_requirements(os.path.join(current_dir, 'requirements.txt')),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)
