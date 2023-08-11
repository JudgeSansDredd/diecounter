from fastai.vision.all import *

root_dir = Path("../../")
training_data_path = root_dir.joinpath("training-data/train")
validation_data_path = root_dir.joinpath("training-data/valid")


def label_func(fname):
    return fname.name.split("_")[0]


dblock = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=get_image_files,
    get_y=label_func,
    splitter=RandomSplitter(),
    item_tfms=Resize(300),
)
dls = dblock.dataloaders(training_data_path)
dls.show_batch()

learn = Learner(
    dls,
    xresnet50(n_out=dls.c),
    opt_func=ranger,
    loss_func=LabelSmoothingCrossEntropyFlat(),
    metrics=accuracy,
)

learn.fit_flat_cos(5, 8e-3)

learn.predict(validation_data_path.joinpath("d20/d20_off-angle_0345.jpg").resolve())

learn.path = root_dir

learn.save("5epoch")
