from setuptools import setup, find_packages

setup(
    name='Pyth3rNalisis',
    version='0.0.2',
    description='Pyth3rNalisis is a malware analysis tool that searches for red flags in any file.',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    author='Pyth3rEx',
    author_email='',
    url='https://github.com/Pyth3rEx/Pyth3rNalisis',
    packages=find_packages(),
    install_requires=["""
        cffi>=1.17.0
        colorama>=0.4.6
        colorclass>=2.2.2
        cryptography>=43.0.0
        easygui>=0.98.3
        filetype>=1.2.0
        lxml>=5.3.0
        msoffcrypto-tool>=5.4.2
        olefile>=0.47
        oletools>=0.60.2
        pcodedmp>=1.2.6
        pefile>=2023.2.7
        pycparser>=2.22
        pyfiglet>=1.0.2
        pyparsing>=3.1.2
        PyPDF2>=3.0.1
        python-docx>=1.1.2
        python-magic>=0.4.27
        setuptools>=72.2.0
        tabulate>=0.9.0
        typing_extensions>=4.12.2
        win_unicode_console>=0.5
    """],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)
