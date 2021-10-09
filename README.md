# Translates .Xmodmap file lines to bash lines

> Useful for executing a .Xmodmap file on i3 windows manager.

Use example: ```bash
	python3 xmodmap-to-sh.py<br>
		Save a new file? (y/N): y<br>
		Source file path: source/file/path<br>
		Destination file path: destination/file/path
```

To save the traslation in a new file without executing, add `-s` as the first argument and `destination/file/path` to the end of the command.

To only translate and execute the commands, just add `source/file/path` as unique argument.

Command use example: `python3 xmodmap-to-sh.py -s source/file/path destination/file/path`

