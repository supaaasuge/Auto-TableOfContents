# Auto-TableOfContents
Python script to read a markdown file/directory of markdown files and automatically create a working Table of Contents of all headers.


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
