# downloads_folder_cleanup
This project contains Python scripts designed to help you manage and clean up your local file system — especially the **Downloads folder**, where duplicates, large files, and old clutter often accumulate.

These scripts are practical tools that:
- Free up storage
- Organize files by type or age
- Remove duplicates
- Help you understand what’s taking up space

## Motivation
This repo was created as a practical Python scripting exercise and a personal productivity tool to manage the growing clutter in the Downloads folder. It's a great project to improve scripting, automation, and system organization.

## Features and Scripts

| Script Name                | Description |
|---------------------------|-------------|
| `count_large_files.py`    | Lists and counts all files larger than a given size (in MB) |
| `delete_old_files.py`     | Deletes files not modified in the last _N_ days |
| `find_duplicate_files.py` | Detects files with the same name and size (optionally deletes them) |
| `organize_by_extension.py`| Sorts files into folders by extension (e.g., `.pdf`, `.jpg`) |
| `rename_files_with_date.py`| Renames files by appending their last modified date |
| `delete_empty_folders.py` | Removes all empty folders inside the target directory |
| `move_to_archive.py`      | Moves old files to an `Archive/` folder instead of deleting them |
| `file_type_summary.py`    | Prints a summary of file counts by type (e.g., PDF: 30, JPG: 50) |

## Default Target Folder

Most scripts are configured by default to target:
You can modify the path inside each script to fit your needs.

## Requirements

These scripts use only **Python standard libraries** such as:
- `os`
- `shutil`
- `datetime`
- `hashlib`

No external dependencies required.

## How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/downloads-folder-cleanup.git