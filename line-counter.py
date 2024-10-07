from os import scandir

IGNORE_DIRS = [
    "obj", "bin", "packages", "properties", ".vs", ".git", ".config",
    ".angular", "node_modules", "target"
    ]
CODE_EXTENSIONS = [
    "cs", "json", "py", "ps1", "xaml", "bat", "html", "ts", "css", "rs"
    ]


def scan_directory(path, exec_name):
    files = []
    for entry in scandir(path):
        if(entry.is_dir() and entry.name.lower() not in IGNORE_DIRS):
            files.extend(scan_directory(entry.path, exec_name))
        elif(entry.is_file() and (entry.name.split(".")[-1]).lower() in CODE_EXTENSIONS):
            if(entry.name != exec_name):
                files.append(entry.path)
    return files

            
code_files = scan_directory(".\\", __file__.split("\\")[-1])
line_count = 0
for path in code_files:
    with open(path) as file:
        line_count += sum(1 for _ in file)
print(str(line_count) + " lines of code in " + str(len(code_files)) + " files")
