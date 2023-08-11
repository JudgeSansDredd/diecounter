import os

d4_dirpath = "./training-data/train/d4"

for fname in os.listdir(d4_dirpath):
    if "_" not in fname:
        new_name = f"{fname[:2]}_{fname[2:]}"
        os.rename(f"{d4_dirpath}/{fname}", f"{d4_dirpath}/{new_name}")
