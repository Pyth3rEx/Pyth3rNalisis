from setuptools import setup, find_packages

setup(
    name='Pyth3rNalisis',
    version='0.0.7',
    description='Pyth3rNalisis is a malware analysis tool that searches for red flags in any file.',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    author='Pyth3rEx',
    url='https://github.com/Pyth3rEx/Pyth3rNalisis',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,  # Ensure that all data files are included
    package_data={
        'Pyth3rNalisis': ['*.py', 'modules/*.py'],  # Include all Python files and modules
    },
    install_requires=[
        "certifi>=2024.7.4",
        "cffi>=1.17.0",
        "charset-normalizer>=3.3.2",
        "colorama>=0.4.6",
        "colorclass>=2.2.2",
        "cryptography>=43.0.0",
        "easygui>=0.98.3",
        "filetype>=1.2.0",
        "idna>=3.7",
        "lxml>=5.3.0",
        "msoffcrypto-tool>=5.4.2",
        "olefile>=0.47",
        "oletools>=0.60.2",
        "pcodedmp>=1.2.6",
        "pefile>=2023.2.7",
        "pycparser>=2.22",
        "pyfiglet>=1.0.2",
        "pyparsing>=3.1.2",
        "PyPDF2>=3.0.1",
        "python-docx>=1.1.2",
        "python-magic>=0.4.27",
        "requests>=2.32.3",
        "setuptools>=73.0.1",
        "tabulate>=0.9.0",
        "typing_extensions>=4.12.2",
        "urllib3>=2.2.2",
        "win_unicode_console>=0.5"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Topic :: Security',
        'Natural Language :: English',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'Development Status :: 3 - Alpha'
    ],
    python_requires='>=3.11',
    entry_points={
        'console_scripts': [
            'Pyth3rNalisis = Pyth3rNalisis.__main__:main',
        ],
    },
)
