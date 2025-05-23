import os
import shutil
import argparse

# Set up CLI
parser = argparse.ArgumentParser(description="Organize files in a folder by their extensions.")
parser.add_argument("--path", type=str, default=r"C:\Users\saota\Downloads", help="Target folder (default: Downloads)")
args = parser.parse_args()

folder_path = args.path

# Create subfolder name based on file extension
def get_folder_for_extension(extension):
    return extension[1:].upper() + "_Files" if extension else "No_Extension"

moved_count = 0

for root, dirs, files in os.walk(folder_path):
    # Skip subfolders
    if root != folder_path:
        continue

    for file in files:
        file_path = os.path.join(root, file)
        _, extension = os.path.splitext(file)
        target_folder = os.path.join(folder_path, get_folder_for_extension(extension))

        # Create target folder if it doesn't exist
        os.makedirs(target_folder, exist_ok=True)

        # Move file
        try:
            shutil.move(file_path, os.path.join(target_folder, file))
            print(f"Moved: {file} → {target_folder}")
            moved_count += 1
        except Exception as e:
            print(f"Failed to move {file}: {e}")

print(f"\n✅ Organized {moved_count} files by extension.")