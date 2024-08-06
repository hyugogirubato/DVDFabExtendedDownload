# DVDFab ExtendedDownload

This script facilitates the extended download service for DVDFab products. It provides an interactive command-line interface that allows users to select a DVDFab product, platform, software, and version to retrieve a download link.

## Features

- **🎮 Interactive CLI**: Uses the `pick` library for an easy selection menu.
- **📦 Product Selection**: Supports a wide range of DVDFab products.
- **🖥️ Platform Support**: Works with both Windows and macOS.
- **🔗 Download Links**: Retrieves download links for the selected software version.

## Requirements

- `requests` library
- `pick` library

You can install the required libraries using pip:

```bash
pip install requests pick
```

## Usage

1. **Run the Script**:
    ```bash
    python dvdfab.py
    ```

2. **Select Product**: Choose a DVDFab product from the interactive list.
3. **Select Platform**: Choose the platform (Windows or macOS).
4. **Select Software**: Choose the specific software version.
5. **Select Version**: Choose the version from the available versions.
6. **Get Download Link**: The script will display the extended download link for the selected version.

## Example

```bash
[*] Extended Download Service
[+] Product: DVDFab
[+] Product: win
[+] Software: DVDFab x64
[+] Version: 13023
[+] Download: https://dl.dvdfab.cn/download/67_13023_63d667c7/dvdfab13_x64_13023.exe
```

## Configuration

The script uses a predefined dictionary (`EDS_PRODUCTS`) containing the product details, platforms, software versions, and their corresponding identifiers.

## Contributing

Contributions to the DVDFab ExtendDownload are welcome! Feel free to fork the repository and submit pull requests. If you encounter any issues or have suggestions for improvement, please [open an issue](https://github.com/hyugogirubato/DVDFabExtendedDownload/issues) on GitHub.

## Licensing

This software is licensed under the terms of [MIT License](https://github.com/hyugogirubato/DVDFabExtendedDownload/blob/main/LICENSE).  
You can find a copy of the license in the LICENSE file in the root folder.