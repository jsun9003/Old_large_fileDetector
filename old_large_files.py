#!/data1/juns/software/mambaforge/bin/python
import os
import time
import argparse
from datetime import datetime, timedelta

def main(folder_path, output_file):
    # Define size and time thresholds
    size_threshold = 10 * 1024 * 1024 * 1024  # 10GB
    time_threshold = datetime.now() - timedelta(days=365*2)  # Two years

    # List to store information about files that meet the criteria
    files_info = []

    # Traverse the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            try:
                # Get file size and last modification time
                file_size = os.path.getsize(file_path)
                file_mtime = os.path.getmtime(file_path)
                file_mtime_dt = datetime.fromtimestamp(file_mtime)
                
                # Check if the file meets the criteria
                if file_size > size_threshold and file_mtime_dt < time_threshold:
                    files_info.append((file_path, file_size, file_mtime_dt))
            except FileNotFoundError:
                # Skip files that do not exist
                print(f"File not found: {file_path}")
                continue

    # Sort files by size in descending order
    files_info.sort(key=lambda x: x[1], reverse=True)

    # Output the information of files that meet the criteria to the specified file
    with open(output_file, 'w') as f:
        for file_info in files_info:
            f.write(f"File path: {file_info[0]}\n")
            f.write(f"File size: {file_info[1] / (1024 * 1024 * 1024):.2f} GB\n")
            f.write(f"Last modification time: {file_info[2]}\n")
            f.write('-----------------------------------\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Filter files in a folder that are larger than 10GB and older than two years, and output sorted by size')
    parser.add_argument('folder_path', type=str, help='Path to the folder to be scanned')
    parser.add_argument('output_file', type=str, help='Output file name')

    args = parser.parse_args()
    main(args.folder_path, args.output_file)
