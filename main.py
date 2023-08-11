from fastai.data.block import CategoryBlock, DataBlock, get_image_files
from fastai.vision.augment import ImageBlock


def d4_func(fname):
    print(fname.name[:2])

    return "cat" if fname.name[0].isupper() else "dog"


def main():
    dblock = DataBlock(
        blocks=(ImageBlock, CategoryBlock), get_items=get_image_files, get_y=d4_func
    )
    dsets = dblock.datasets("./training-data/train")
    dsets.train[0]


if __name__ == "__main__":
    main()
