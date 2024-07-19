# File Organizer

## Overview

File Organizer is a Python-based utility designed to help you organize files in a specified directory by categorizing them into folders based on their file extensions. This application is especially useful for cleaning up and organizing your Downloads folder or any other directory containing a mix of different file types.

## Features

- Organizes files into specific directories based on their file extensions.
- Supports a wide range of file types, including images, videos, audios, documents, compressed files, and program files.
- Logs all file movements and any errors encountered during the process.

## Installation

### Prerequisites

- Python 3.x installed on your machine.

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/file-organizer.git
    cd file-organizer
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required packages (if any):
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Script

1. Navigate to the directory where the script is located.
2. Run the script:
    ```bash
    python file_organizer.py
    ```

3. When prompted, enter the path to the directory you want to organize (e.g., `C:\Users\PC\Downloads`).

### Creating an Executable

To create a standalone executable (Windows):

1. Install PyInstaller:
    ```bash
    pip install pyinstaller
    ```

2. Create the executable:
    ```bash
    pyinstaller --onefile file_organizer.py
    ```

3. The executable will be located in the `dist` directory.

### Example Usage

```bash
python file_organizer.py 
```
### Log File
The script generates a log file (file_organiser.log) in the same directory as the script, which records:

1. Directory creation events.
2. Files moved and their destinations.
3. Any errors encountered during file movements.

## File Categories
The following file categories and extensions are supported:
```
1. Images: .jpeg, .jpg, .png, .gif, .bmp, .tiff, .svg, .webp, .jfif, .ico, .heif
2. Videos: .avi, .mp4, .mov, .mkv, .webm, .flv, .wmv, .mpg, .mpeg, .3gp, .ts
3. Audios: .mp3, .ogg, .wav, .amr, .flac, .aac, .m4a, .wma, .opus
4. Documents: .doc, .docx, .txt, .pdf, .xlsx, .ppt, .pptx, .odt, .ods, .odp, .docm, .dot, .dotx, .dotm, .epub, .mobi, .azw, .xps, .tex, .xml, .rtf, .html, .htm, .csv
5. Compressed: .zip, .rar, .7z, .iso, .tar, .gz, .bz2, .xz, .z, .dmg
6. Programs: .exe, .msi, .app, .bat, .sh, .jar
```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.


