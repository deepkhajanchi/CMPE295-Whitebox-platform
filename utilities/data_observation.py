from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from PIL import Image
from mpl_toolkits.axes_grid1 import ImageGrid
from keras.applications import imagenet_utils
import matplotlib.pyplot as plt
import os
import numpy as np

### Chi Tran: Master of Science - Software Engineering - SJSU - CMPE 295B - Fall 2020
### Common functions to read and show samples of input data (display data samples in each class).

def read_data(path, size):
    img = image.load_img(path, target_size=size)
    img = image.img_to_array(img)
    return img
  
  
def show_sample(data_source):
    CATE = ['phylloxera', 'mealybug', 'black_measles', 'black_rot', 'leaf_blight', 'healthy']
    NUM_CATE = len(CATE)
    img_height, img_width = 256, 256

    # Create image grid
    figure = plt.figure(num=1, figsize=(8,8))
    grid = ImageGrid(figure, 111, nrows_ncols=(NUM_CATE,NUM_CATE),
                     axes_pad=0.1) 

    # Plot each image into a square
    i = 0
    for cate in CATE:
      for j in range(6):
        ax = grid[i]
        path = os.path.join(data_source, cate)
        pic = cate + str(j) + '.jpg'
        im = read_data(os.path.join(path, pic), size=(img_height, img_width))
        ax.imshow(im/255., interpolation='nearest', aspect='auto')
        ax.axis('off')
        if i % NUM_CATE == NUM_CATE - 1:
          ax.text(x=img_height*1.05, y=img_height//2, s=cate, verticalalignment='center')
        i += 1

    figure.savefig('test.png');
    
def load_img_into_narr(train_label, bin_dir, numpy):
    # Read all images into numpy array
    label_numpy = [read_data(os.path.join(train_label, img),\
               (256, 256)) for img in os.listdir(train_label)]
    
    # Save numpy arrays into a folder
    np.save(os.path.join(bin_dir, numpy), arr=label_numpy)
    return label_numpy