
import matplotlib.pyplot as plt
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from PIL import Image
from mpl_toolkits.axes_grid1 import ImageGrid
from utilities import data_observation as do


def display_misclassified_images(paths, rows, columns):
    from mpl_toolkits.axes_grid1 import ImageGrid
    fig = plt.figure(figsize=(50,50))

    grid = ImageGrid(fig, 111,
                     nrows_ncols=(rows,columns),
                     axes_pad=0.5,
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
    for i, file in enumerate(path):   
        plt.imshow(Image.open(file))
        plt.title(file.rsplit('\\')[-1])
        f=plt.figure(figsize=(8,7))
        plt.show()