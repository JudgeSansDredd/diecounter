from fastai.vision.all import *


def label_func(fname):
    return fname.name.split("_")[0]


# Datablock
dblock = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=get_image_files,
    get_y=label_func,
    splitter=RandomSplitter(),
    item_tfms=Resize(300),
)

# Loaders
dls = dblock.dataloaders("./training-data/train")

# Learning model
learn = Learner(
    dls,
    xresnet50(n_out=dls.c),
    opt_func=ranger,
    loss_func=LabelSmoothingCrossEntropyFlat(),
    metrics=accuracy,
)

# Do the learning
learn.fit_flat_cos(5, 8e-3)

# Save the learned model
learn.save("./5epoch")
