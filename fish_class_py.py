# %%
import pandas as pd
import numpy as np
from tensorflow.keras import layers, optimizers, Model

# for image handling
import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path


# %%
# Lets check out some of the data
pictures_dir = Path('/Users/aaron.stjohn/Documents/tf_projects/NA_Fish_Dataset')

# %%
for i in pictures_dir.glob('**/*'):
    # make sure the image is an image; png or jpg
    if not i.name.endswith('png') and not i.name.endswith('JPG'):
        continue
    # convert image to gray scale. Reduces the # of params without losing
    # information
    img = Image.open(i).convert('L')
    try:
        # create the type of fish dirs
        Path.mkdir(Path(f'{pictures_dir.as_posix()}/gray_fish/{i.parent.name}'))
    except FileExistsError:
        continue
    img.save(
        f'{pictures_dir.as_posix()}/gray_fish/{i.parent.name}/{i.stem}_gray{i.suffix}'
    )
    # print(f'{pictures_dir.as_posix()}/{i.parent.name}/{i.stem}_gray{i.suffix}')

# %%
# Path.mkdir(Path(f'{pictures_dir.as_posix()}/gray_fish/{i.parent.name}'))


