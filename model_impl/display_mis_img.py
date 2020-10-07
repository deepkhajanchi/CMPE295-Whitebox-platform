
import matplotlib.pyplot as plt
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from PIL import Image
from mpl_toolkits.axes_grid1 import ImageGrid
from utilities import data_observation as do

### Chi Tran: Master of Science - Software Engineering - SJSU - CMPE 295B - Fall 2020
### Common functions to display all misclassified images.

def display_misclassified_images(paths, rows, columns):
    """ Display misclassified images using 2x2 matrix """
    from mpl_toolkits.axes_grid1 import ImageGrid
    fig = plt.figure(figsize=(80,80))

    grid = ImageGrid(fig, 111,
                     nrows_ncols=(rows,columns),
                     axes_pad=0.6,
                     )

    for i,file in enumerate(paths):
        subplot_title=plt.title(file.rsplit('\\')[-1]) 
        #grid[i].axes.set_title(subplot_title, fontdict=None, loc='center', color = "k")      
        #grid[i].imshow(PIL.Image.open(file),cmap='gray',interpolation='none')
        ax = grid[i]
        ax.set_title(plt.title(file.rsplit('\\')[-1]), fontdict=None, loc='center', color = "k") 
        im = do.read_data(file, size=(256, 256))
        ax.imshow(im/255., aspect='auto')
        ax.axis('off')

        i += 1

    plt.show();

def display_misclassified_images_1(path):
    """ Display misclassified images one by one  """
    for i, file in enumerate(path):   
        plt.imshow(Image.open(file))
        plt.title(file.rsplit('\\')[-1])
        f=plt.figure(figsize=(8,7))
        plt.show()