# Translates .Xmodmap file lines to bash lines

> Useful for running a .Xmodmap file on i3 windows manager.

Usage example:

	$ python3 xmodmap-to-sh.py
	Save in a new file? (y/N): y
	Source file path: source/file/path
	Destination file path: destination/file/path

### It can also be used without user's input

To just translate and run the commands, add `source/file/path` as single argument.

To save the traslation in a new file without executing, add `destination/file/path` to the end of the command as the second argument.

Command usage example: `python3 xmodmap-to-sh.py source/file/path destination/file/path`

