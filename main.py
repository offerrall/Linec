import os

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

files_by_type = get_files_by_type("./", valid_extensions=valid_extensions)
total_lines_count = 0

for ext, files in files_by_type.items():
    if len(files) == 0:
        continue

    ext_lines_count = 0
    for file in files:
        lines_count = count_lines(file)
        ext_lines_count += lines_count
    
    print(f"Total lines count for {ext}: {ext_lines_count}")
    total_lines_count += ext_lines_count

print(f"Total lines count for all files: {total_lines_count}")