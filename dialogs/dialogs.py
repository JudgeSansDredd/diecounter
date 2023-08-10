import os

from whiptail import Whiptail


class Dialogs:
    @staticmethod
    def get_whiptail():
        settings = {
            "title": "Dice Training",
            "width": os.get_terminal_size().columns - 10,
            "height": os.get_terminal_size().lines - 10,
        }
        return Whiptail(**settings)

    @classmethod
    def input_box(cls, prompt, default=""):
        return cls.get_whiptail().inputbox(prompt, default)
