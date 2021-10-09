# Translates .Xmodmap file lines to bash lines

> Useful for running a .Xmodmap file on i3 windows manager.

Usage example:

	$ python3 xmodmap-to-sh.py
	Save in a new file? (y/N): y
	Source file path: source/file/path
	Destination file path: destination/file/path

### It can also be used without user's input

To save the traslation in a new file without executing, add `-s` as the first argument and `destination/file/path` to the end of the command.

To just translate and run the commands, add `source/file/path` as single argument.

Command usage example: `python3 xmodmap-to-sh.py -s source/file/path destination/file/path`

