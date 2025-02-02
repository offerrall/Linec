import os
from time import time

valid_extensions = [".py", ".c", ".cpp", ".h", ".html", ".css", ".js", ".kv"]

def get_files_by_type(folder_path: str, valid_extensions: list) -> dict:
    files_dict = {}
    
    for ext in valid_extensions:
        files_dict[ext] = []
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            ext = os.path.splitext(file)[1]
            if not file.endswith(tuple(valid_extensions)):
                continue
            full_path = os.path.join(root, file)
            
            if ext not in files_dict:
                files_dict[ext] = []
            
            files_dict[ext].append(full_path)
    
    return files_dict

def count_lines(file_path: str) -> int:
    with open(file_path, "r") as file:
        return len(file.readlines())

folder = "./"
full_path = os.path.join(os.getcwd())
start_time = time()

print(f"\nScanning folder: {full_path} \n")

files_by_type = get_files_by_type(folder, valid_extensions=valid_extensions)
total_lines_count = 0

for ext, files in files_by_type.items():
    if len(files) == 0:
        continue

    ext_lines_count = 0
    num_files = len(files)
    print(f"{ext} files: {num_files}")
    for file in files:
        lines_count = count_lines(file)
        ext_lines_count += lines_count
    
    print(f" - Total lines count: {ext_lines_count}\n")
    total_lines_count += ext_lines_count

print(f"\nTotal lines count for all files: {total_lines_count}")
print(f"Time taken: {time() - start_time:.2f} seconds\n")