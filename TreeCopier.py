import os
import shutil
import pathspec
import pyperclip
from io import StringIO

def load_gitignore_patterns():
    with open('.gitignore', 'r') as gitignore_file:
        lines = gitignore_file.read().splitlines()
    spec = pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, lines)
    return spec

def should_ignore(path, spec):
    return spec.match_file(path)

def print_tree(start_path, spec, prefix='', output=None):
    entries = sorted(os.listdir(start_path))
    entries = [e for e in entries if not should_ignore(os.path.relpath(os.path.join(start_path, e)), spec)]

    for index, entry in enumerate(entries):
        full_path = os.path.join(start_path, entry)
        connector = '└── ' if index == len(entries) - 1 else '├── '
        line = prefix + connector + entry
        if output is not None:
            output.write(line + '\n')
        print(line)

        if os.path.isdir(full_path):
            next_prefix = '    ' if index == len(entries) - 1 else '│   '
            print_tree(full_path, spec, prefix + next_prefix, output)

def clear_export_directory(export_dir):
    if os.path.exists(export_dir):
        for root, dirs, files in os.walk(export_dir):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                shutil.rmtree(os.path.join(root, dir))
        print(f"Cleared existing files in {export_dir}.")

def copy_files_to_export(start_path, export_dir, spec):
    for root, dirs, files in os.walk(start_path):
        dirs[:] = [d for d in dirs if not should_ignore(os.path.relpath(os.path.join(root, d)), spec)]
        for file in files:
            if should_ignore(os.path.relpath(os.path.join(root, file)), spec):
                continue
            
            relative_path = os.path.relpath(os.path.join(root, file), start_path)
            dest_file_name = relative_path.replace(os.sep, '_')
            dest_file_path = os.path.join(export_dir, dest_file_name)
            
            shutil.copyfile(os.path.join(root, file), dest_file_path)
            print(f"Copied: {relative_path} to {dest_file_path}")

def main():
    spec = load_gitignore_patterns()
    
    # Capture the directory tree output
    output = StringIO()
    
    # Print the directory tree
    print("Directory Tree:")
    print_tree('.', spec, output=output)
    
    # Copy the directory tree to clipboard
    tree_output = output.getvalue()
    pyperclip.copy(tree_output)
    print("\nDirectory tree has been copied to clipboard.")
    
    # Create or clear the export directory
    export_dir = 'AI_file_export'
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)
    else:
        clear_export_directory(export_dir)
    
    # Start copying files
    print("\nCopying Files:")
    copy_files_to_export('.', export_dir, spec)

if __name__ == '__main__':
    main()
