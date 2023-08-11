import os

import psutil
from PIL import Image

from db.connection import Connection
from dialogs.dialogs import Dialogs

DIE_TYPES = [4, 6, 8, 10, 12, 20]


def kill_open_images():
    for proc in psutil.process_iter():
        name = proc.name()
        if name == "display" or name == "Preview":
            proc.kill()


def get_input():
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
            fpath = f"{dir_path}/{image_path}"
            if conn.image_classification_exists(fpath):
                continue
            with Image.open(fpath) as img:
                img.show()
                value = get_input()
                kill_open_images()
                conn.add_image_classification(die_type, value, fpath)


if __name__ == "__main__":
    main()
