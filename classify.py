import os
from pathlib import Path
from platform import system

import psutil
from PIL import Image

from db.connection import Connection
from dialogs.dialogs import Dialogs

DIE_TYPES = [4, 6, 8, 10, 12, 20]


def focus_on_terminal():
    if system() == "Darwin":
        os.system(
            """/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "iTerm2" to true' """
        )


def kill_open_images():
    for proc in psutil.process_iter():
        name = proc.name()
        if name == "display" or name == "Preview":
            proc.kill()


def get_input():
    focus_on_terminal()
    strValue, return_code = Dialogs.input_box("What value is showing?")
    if return_code == 1:
        exit()
    value = int(strValue)
    return value


def main():
    # Create db connection and init db
    conn = Connection()
    conn.init_db()

    for die_type in DIE_TYPES:
        dir_path = f"./training-data/train/d{die_type}"
        for image_path in os.listdir(dir_path):
            fpath = str(Path(f"{dir_path}/{image_path}").resolve())
            image_classification = conn.get_image_classification(fpath)
            if image_classification:
                continue
            with Image.open(fpath) as img:
                img.show()
                value = get_input()
                kill_open_images()
                conn.add_image_classification(die_type, value, fpath)


if __name__ == "__main__":
    main()
