<h1>Translates .Xmodmap file lines to bash lines</h1>

<p>Useful for executing a .Xmodmap file on i3 windows manager.</p>

<p>Use example:<br>
<tab><code>Save a new file? (y/N): y</code><br>
<tab><code>Source file path: source/file/path</code><br>
<tab><code>Destination file path: destination/file/path</code>
</p>

<p>To save the traslation in a new file without executing, add <code>-s</code> and <code>destination/file/path</code> to the end of the command.</p>

<p>To only translate and execute the commands, just add <code>source/file/path</code> as unique argument.</p>

<p>Command use example: <code>python3 xmodmap-to-sh.py -s source/file/path destination/file/path</code></p>

