import os
import sys
import argparse

def process_file(file_path):
    try:
        TableOfContents = "## Table of Contents\n\n"

        with open(file_path, 'r', encoding='utf-8') as f:
            contents = f.read()
            lines = contents.split('\n')

            for line in lines:
                if line.startswith('# '):
                    heading = line.strip('# ')
                    anchor = heading.lower().replace(' ', '\\')
                    TableOfContents += f"- [{heading}](#{anchor})\n"
                elif line.startswith('## '):
                    heading = line.strip('## ')
                    anchor = heading.replace(' ', '\\')
                    TableOfContents += f"  - [{heading}](#{anchor})\n"
                elif line.startswith('### '):
                    heading = line.strip('### ')
                    anchor = heading.replace(' ', '\\')
                    TableOfContents += f"    - [{heading}](#{anchor})\n"
                elif line.startswith('#### '):
                    heading = line.strip('#### ')
                    anchor = heading.replace(' ', '\\')
                    TableOfContents += f"      - [{heading}](#{anchor})\n"
                elif line.startswith('##### '):
                    heading = line.strip('##### ')
                    anchor = heading.replace(' ', '\\')
                    TableOfContents += f"        - [{heading}](#{anchor})\n"
                elif line.startswith('###### '):
                    heading = line.strip('###### ')
                    anchor = heading.replace(' ', '\\')
                    TableOfContents += f"          - [{heading}](#{anchor})\n"
    except UnicodeDecodeError:
        print(f"Skipping file {file_path} due to encoding issues")
        with open(file_path, 'r+', encoding='utf-8') as f:
            original_contents = f.read()
            f.seek(0)
            f.write(TableOfContents + "\n" + original_contents)

    print(f"Table of Contents appended successfully to {file_path}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_file(file_path)

def main():
    if args.dir:
        directory = args.dir
        if not os.path.isdir(directory):
            print(f"{directory} is not a valid directory.")
            sys.exit(1)
        process_directory(directory)
    else:
        print("Please provide the directory path using the --dir argument.")
        sys.exit(1)
    
    if args.file:
        file = args.file
        if not os.path.isfile(file):
            print(f"{file} is not a valid file path.")
            sys.exit(1)
        process_file(file)
    else:
        print("Please provide the correct file path using the --file argument.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Append Table of Contents to Markdown files.')
    parser.add_argument('--dir', type=str, help='Directory containing Markdown files')
    parser.add_argument('--file', type=str, help='File to process and append Table of Contents')
    args = parser.parse_args()
    main()

    if args.file and args.dir is True:
        print("Please use either --file or --dir, but not both at the same time.")
        sys.exit(1)
