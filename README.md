# TreeCopier

TreeCopier is a Python utility that generates a directory tree of your current working directory while respecting `.gitignore` rules, copies all non-ignored files into a single directory, and renames them to reflect their original paths. Additionally, the tool copies the generated directory tree to your clipboard for easy sharing and documentation.

## Features

- **Directory Tree Generation:** Prints a visual directory tree that respects the rules defined in your `.gitignore` file.
- **File Export:** Copies all non-ignored files to a designated directory (`AI_file_export`) while renaming them to reflect their original paths.
- **Clipboard Support:** Automatically copies the generated directory tree to your clipboard.
- **Automatic Cleanup:** Cleans out the export directory before copying new files to ensure a fresh set of files every time.

## Installation

To use TreeCopier, you'll need Python installed on your system. Additionally, the tool relies on the following Python packages:

- `pathspec`: For parsing and matching `.gitignore` patterns.
- `pyperclip`: For copying the directory tree to the clipboard.

You can install these dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/TreeCopier.git
   cd TreeCopier
   ```

2. **Run the Script:**

   Simply run the script in your terminal:

   ```bash
   python export_and_tree_with_cleanup_and_clipboard.py
   ```

   The script will:
   - Generate and print the directory tree of your current directory.
   - Copy the directory tree to your clipboard.
   - Clear the `AI_file_export` directory (or create it if it doesn't exist).
   - Copy all non-ignored files to the `AI_file_export` directory, renaming them to reflect their original paths.

3. **Paste the Directory Tree:**

   After running the script, the directory tree is copied to your clipboard. You can paste it into any text editor, document, or chat.

## Example

Here’s an example of what the output might look like:

```plaintext
Directory Tree:
├── README.md
├── src
│   ├── main.py
│   ├── utils.py
└── tests
    ├── test_main.py
    └── test_utils.py
```

Files will be copied to `AI_file_export`, renamed to reflect their original paths, like so:

```plaintext
Copied: README.md to AI_file_export/README.md
Copied: src/main.py to AI_file_export/src_main.py
Copied: src/utils.py to AI_file_export/src_utils.py
Copied: tests/test_main.py to AI_file_export/tests_test_main.py
Copied: tests/test_utils.py to AI_file_export/tests_test_utils.py
```

## Requirements

- Python 3.x
- `pathspec` package
- `pyperclip` package

Install the required packages using:

```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or run into issues, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.