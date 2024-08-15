
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
│   ├── requirements.txt         # Python dependencies for the project
│   ├── __init__.py              # Package initializer
│   └── modules/                 # Directory for additional modules
│       ├── module_banner.py     # Module for displaying banners
│       ├── module_log.py        # Module for enhanced logging
│       ├── worker_extension.py  # Worker module for file extensions
│       ├── worker_metadata.py   # Worker module for metadata extraction
│       └── __init__.py          # Package initializer for the modules directory
│
└── tests/                       # Test files for validating the tool’s functionality
    ├── malware/                 # Test files containing malware-like signatures
    │   ├── corrupted_magic.gif
    │   ├── corrupted_magic.jpg
    │   ├── corrupted_magic.pdf
    │   ├── corrupted_magic.png
    └── not_malware/             # Test files that do not contain malware
        ├── legitimate_GIF.gif
        ├── legitimate_JPG.jpg
        ├── legitimate_PDF.pdf
        ├── legitimate_PNG.png
```

## Installation

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
python src/Pyth3rNalisis.py -h
```

For more detailed usage, refer to the documentation in the \`docs/\` directory.

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING](CONTRIBUTING.md) for details.

## License

This project is licensed under the GNU V3 License - see the [LICENSE](LICENSE) file for details.
