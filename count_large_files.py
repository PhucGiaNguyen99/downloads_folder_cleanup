import argparse
import os

# Setup command-line arguments
parser = argparse.ArgumentParser(description="Count files larger than a given size in MB.")
parser.add_argument("size", type=int, help="Size threshold in MB")
parser.add_argument("--path", type=str, default=r"C:\Users\saota\Downloads", help="Folder to scan (default: Downloads)")
args = parser.parse_args()

# Size threshold in megabytes
size_threshold_bytes = args.size * 1024 * 1024
folder_path = args.path

# Counter
count = 0

print(f"Files in '{folder_path}' larger than {args.size} MB:\n")

# Walk through the folder and subfolders
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            size = os.path.getsize(file_path)
            if size > size_threshold_bytes:
                size_mb = size / (1024 * 1024)
                print(f"{file_path} - {size_mb:.2f} MB")
                count += 1
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

print(f"\nTotal large files: {count}")