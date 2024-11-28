# PDF Attachment Extractor

PDF Attachment Extractor is a Python application that extracts attachments from PDF files.

## Features

- Extract attachments from PDF files.
- Single executable file using PyInstaller.

## Installation

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Build

To build the application into a single executable using PyInstaller:

```bash
pyinstaller --distpath ../ --workpath build pdf_attachment_extractor.spec
```

The executable will be located in the `pdf_attachment_extractor` directory.

`Note:` To automate the build process on Windows, you can use the start_build.bat file. Click on start_build.bat to execute the build process.


## Usage

### Running the Application

To run the application, simply double-click on the executable file `PDF Attachment Extractor.exe` on windows.

## Acknowledgments

- [PyInstaller](https://www.pyinstaller.org/) - For bundling Python applications into standalone executables.
- [PyPDF2](https://pythonhosted.org/PyPDF2/) - For PDF manipulation.
