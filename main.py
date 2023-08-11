from fastai.vision.augment import (
    CategoryBlock,
    DataBlock,
    ImageBlock,
    RandomSplitter,
    Resize,
    get_image_files,
)
from fastai.vision.learner import Learner
from fastai.vision.models import resnet18


def label_func(fname):
    return fname.name.split("_")[0]


dblock = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=get_image_files,
    get_y=label_func,
    splitter=RandomSplitter(),
    item_tfms=Resize(300),
)
dls = dblock.dataloaders("./training-data/train")
learn = Learner(
    dls,
    resnet18,
)
learn.fit(5)
learn.export("foo.pkl")
