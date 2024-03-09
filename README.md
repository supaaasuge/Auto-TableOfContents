# Auto-TableOfContents
Python script to read a markdown file/directory of markdown files and automatically create a working Table of Contents of all headers.
```
python3 createToC.py --file <file_path.md>
```
- Process a single markdown file.
```
python3 createToC.py --dir </path/to/mdNotes/dir>
```
- Process a directory + all sub directories of markdown files
```
python3 createToC.py --file <file_path.md> --git
```
- Process file using Github compatible format (`-` instead of `\` for spaces)
  - If you want Obsidian compatible anchor links leave it as is.
```
python3 createToC.py --dir </path/to/mdNotes/dir> --git
```
- Process a directory + all sub-directories using Github compatible format. 

Examples:


```bash
python3 createToC.py --file /path/to/notes.md

---
Table of Contents generated successfully at {/path/to/notes.md}
```

```bash
python3 createToC.py --dir /path/to/dir/of/mdNotes

---
Table of contents generated successfully at {mdNotes/....}
Table of contents generated successfully at {mdNotes/1....}
.
.
.
```
![image](https://github.com/supaaasuge/Auto-TableOfContents/assets/158092262/a05f9a9c-a924-465f-80b0-bf6411485a63)
