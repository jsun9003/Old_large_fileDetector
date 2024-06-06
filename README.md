# Old_large_fileDetector

chmod +x old_large_files.py

usage: old_large_files.py [-h] folder_path output_file

Filter files in a folder that are larger than 10GB and older than two years, and output sorted by size

positional arguments:
  folder_path  Path to the folder to be scanned
  output_file  Output file name

optional arguments:
  -h, --help   show this help message and exit

Example:
  python old_large_files.py /path/to/your/folder output.txt
