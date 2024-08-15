
# Pyth3rNalisis

<div align="center">

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-GNU-green)
![Contributions](https://img.shields.io/badge/contributions-welcome-orange)

</div>

Pyth3rNalisis is a powerful and modular Python-based analysis tool aimed at file analysis with a focus on malware detection. It is designed to be easily extensible, allowing users to add custom functionality through additional modules.
<div align="center">

![image](https://raw.githubusercontent.com/Pyth3rEx/Pyth3rNalisis/main/examples/test.png)
</div>

## Features

- **Automated Malware Detection**: Automatically detect potential malware based on file signatures and patterns.
- **Metadata Extraction**: Extract and analyze metadata from various file formats.
- **Comprehensive Logging**: Keep detailed logs of all analysis processes for audit and review purposes.
- **Modular Design**: Custom modules can be integrated into the tool to extend its functionality.
- **Cross-Platform**: Works on both Windows and Unix-based systems.

## Directory Structure

The project is organized as follows:

```
Pyth3rNalisis/
│
├── docs/                        # Documentation files
│
├── examples/                    # Example scripts and files demonstrating the tool’s usage
│
├── src/                         # Source code of the project
│   ├── Pyth3rNalisis.py         # Main script to run the analysis tool
│   └── modules/                 # Directory for additional modules
│
└── tests/                       # Test files for validating the tool’s functionality
    ├── malware/                 # Test files containing malware-like signatures
    └── not_malware/             # Test files that do not contain malware
```

## Installation

### Via PyPI

   ```bash
   pip install Pyth3rNalisis
   ```

### Via Git [For Developers]

1. Clone the repository:
   ```bash
   git clone https://github.com/Pyth3rEx/Pyth3rNalisis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Pyth3rNalisis
   ```
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use \`env\Scripts\activate\`
   ```
4. Install dependencies:
   ```bash
   pip install -r src/requirements.txt
   ```

## Usage

To run the analysis tool and display it's options, execute the main script:

```bash
Pyth3rNalisis -h
```

```
  -h, --help              Show the help message for the app
  -f FILE, --file FILE    File to perform analisis on
  -e, --extension         Check for extension anomaly            | Will perform both a magic number analisis and a filetype analisis and present the results against the declared filetype
  -E, --entropy           Check for unusal entropy in file       | High entropy can indicate obfuscation or encryption of data in the file
  -H, --hashing           Perform hashing analisis on the file   | Will check the file's hash against publicly known malware hashes on online databases
  -m, --metadata          Check for metadata anomaly             | will return data dependent on the file type provided, will overline anomalies such as incoherent dates, author names and such
```

For more detailed usage, refer to the documentation in the \`docs/\` directory.

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING](CONTRIBUTING.md) for details.

## License

This project is licensed under the GNU V3 License - see the [LICENSE](LICENSE) file for details.
