import psutil
from PIL import Image

from db.connection import Connection
from dialogs.dialogs import Dialogs


def kill_open_images():
    for proc in psutil.process_iter():
        name = proc.name()
        if name == "display" or name == "Preview":
            proc.kill()


def get_input():
    strSides, return_code = Dialogs.input_box("How many sides?")
    print(strSides)
    if return_code == 1:
        exit()
    sides = int(strSides)
    strValue, return_code = Dialogs.input_box("What value is showing?")
    print(strValue)
    if return_code == 1:
        exit()
    value = int(strValue)
    return sides, value


def main():
    conn = Connection()
    conn.init_db()
    img = Image.open("./training-data/train/d4/d4_angle_color000.jpg")
    img.show()
    sides, value = get_input()
    kill_open_images()
    conn.add_image_classification(
        sides, value, "./training-data/train/d4/d4_angle_color000.jpg"
    )


if __name__ == "__main__":
    main()
