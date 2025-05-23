import os

# Set the Download folder path
folder_path = r"C:\Users\saota\Downloads"

# Size threshold in megabytes
size_threshold_mb = 50
size_threshold_bytes = size_threshold_mb * 1024 * 1024

# Counter
count = 0

print(f"Files in '{folder_path}' larger than {size_threshold_mb} MB:\n")

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