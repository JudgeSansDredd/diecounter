import time

import psutil
from PIL import Image


def kill_open_images():
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()

def main():
    img = Image.open("./training-data/train/d4/d4_angle_color000.jpg")
    img.show()
    time.sleep(3)
    kill_open_images()

if __name__ == '__main__':
    main()
