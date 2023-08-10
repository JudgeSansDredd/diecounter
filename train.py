import psutil
from PIL import Image

from dialogs.dialogs import Dialogs


def kill_open_images():
    for proc in psutil.process_iter():
        name = proc.name()
        if name == "display" or name == "Preview":
            proc.kill()


def get_input():
    res, strSides = Dialogs.input_box("How many sides?")
    if res == 1:
        exit()
    sides = int(strSides)
    res, strValue = Dialogs.input_box("What value is showing?")
    if res == 1:
        exit()
    value = int(strValue)
    return sides, value


def main():
    img = Image.open("./training-data/train/d4/d4_angle_color000.jpg")
    img.show()
    sides, value = get_input()
    kill_open_images()


if __name__ == "__main__":
    main()
