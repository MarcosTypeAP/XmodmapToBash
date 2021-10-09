import sys
import os


def run():

    try:
        save = sys.argv[1] == "-s"
        if save:
            dest_file_path = sys.argv[len(sys.argv) - 1]
            file_path = sys.argv[len(sys.argv) - 2]
        else:
            file_path = sys.argv[len(sys.argv) - 1]
    except IndexError:
        save = input("Save in a new file? (y/N): ")
        if "y" in save or "Y" in save:
            save = True
        else:
            save = False

        file_path = input("Source file path: ")
        if save:
            dest_file_path = input("Destination file path: ")

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
    except (FileNotFoundError, NotADirectoryError):
        print("Source file not found")
        return

    for i, line in enumerate(lines):
        if line.startswith("keycode"):
            lines[i] = 'xmodmap -e "{}"\n'.format(line.rstrip())
            if not save:
                os.system(lines[i])
        elif line.startswith("!") and save:
            lines[i] = "#" + line[1:]

    if save:
        try:
            os.remove(dest_file_path)
        except FileNotFoundError:
            pass
        except NotADirectoryError:
            print("Invalid destination path")
            return
        except PermissionError:
            print("Permission denied")
            return

        try:
            with open(dest_file_path, "w") as file:
                lines.insert(0, "#!/bin/bash\n")
                lines.insert(1, "\n")
                file.writelines(lines)
        except PermissionError:
            print("Permission denied")
            return


if __name__ == "__main__":
    run()
