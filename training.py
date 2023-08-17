from pathlib import Path

from fastai.vision.all import *

from db.connection import Connection

root_dir = Path("./").resolve()
training_data_path = root_dir.joinpath("training-data/train")
validation_data_path = root_dir.joinpath("training-data/valid")

conn = Connection()


def label_func(fname):
    image_classification = conn.get_image_classification(str(fname))
    return image_classification.die_value if image_classification else 0


dblock = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=get_image_files,
    get_y=label_func,
    splitter=RandomSplitter(),
    item_tfms=Resize(300),
)
dls = dblock.dataloaders(training_data_path)

learn = Learner(
    dls,
    xresnet50(n_out=dls.c),
    opt_func=ranger,
    loss_func=LabelSmoothingCrossEntropyFlat(),
    metrics=accuracy,
)

learn.fit_flat_cos(5, 8e-3)

learn.path = root_dir

learn.save("5epoch")
