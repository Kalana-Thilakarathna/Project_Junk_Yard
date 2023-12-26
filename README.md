# JunkYard Organizer

**JunkYard Organizer** is a Python script that helps you organize your desktop by categorizing files into specific folders based on their types. It runs automatically and organizes files into subfolders under the "JunkYard" directory on your desktop.

## Table of Contents

- [Features](#features)
- [Installation and Usage](#installation-and-usage)
- [File Types Supported](#file-types-supported)
- [Customization](#customization)
- [Issues](#issues)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automatic organization of files on your desktop into categories such as Video, Audio, Images, Documents, Compressed, and Others.
- Creation of subfolders based on the current date under the "JunkYard" directory.
- Supports a variety of file types for categorization.

## Installation and Usage

1. Clone the repository to your local machine:
   [https://github.com/Kalana-Thilakarathna/Project_Junk_Yard](https://github.com/Kalana-Thilakarathna/Project_junk_Yard.git)
   
3. Install the required dependencies:
   pip install -r requirements.txt

4. Run the script:
   python main.py


The script automatically runs on system startup. It checks for files on the desktop and organizes them into subfolders under the "JunkYard" directory.

## File Types Supported

The script supports the following file types:

- **Documents:** .pdf, .docx, .xlsx, .pptx, .txt, .csv, ...
- **Video:** .mp4, .avi, .mkv, .mov, .wmv, .flv, ...
- **Audio:** .mp3, .wav, .flac, .aac, .ogg, .wma, ...
- **Images:** .jpg, .jpeg, .png, .gif, .bmp, .tiff, ...
- **Compressed:** .zip, .rar, .tar, .gz, .bz2, .7z, ...

## Customization

You can customize the script by modifying the `file_extensions_dict` dictionary in the `organizer.py` file to add or remove file types.
Also, you can customize the target directory that you want to organize by changing this `desktop_path` variably by adding your desired path.

## Issues

If you encounter any issues or have suggestions, please open an [issue](link-to-issues).

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License.



