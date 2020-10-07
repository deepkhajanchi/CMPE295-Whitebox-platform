from keras.preprocessing.image import img_to_array, load_img
import keract
from keract import get_activations
from keract import display_activations
from keract import display_heatmaps
import cv2
import numpy as np

### Chi Tran: Master of Science - Software Engineering - SJSU - CMPE 295B - Fall 2020
### Preprocessing inputted image to get activations and heatmaps.

#### Create a numpy array for an inputted image
def preprocess_image(img_path, input_model=None, rescale=255, resize=(256, 256)):
    """
    Preprocesses a given image for prediction with a trained model, with rescaling and resizing options
    
    Arguments:
            img_path: The path to the image file
            rescale: A float or integer indicating required rescaling. 
                    The image array will be divided (scaled) by this number.
            resize: A tuple indicating desired target size. 
                    This should match the input shape as expected by the model
    Returns:
            img: A processed image.
    """


    assert type(img_path) == str, "Image path must be a string"
    assert (
        type(rescale) == int or type(rescale) == float
    ), "Rescale factor must be either a float or int"
    assert (
        type(resize) == tuple and len(resize) == 2
    ), "Resize target must be a tuple with two elements"

    img = load_img(img_path)
    img = img_to_array(img)
    img = img / float(rescale)
    img = cv2.resize(img, resize)
    if input_model != None:
        if len(input_model.input_shape) == 4:
            img = np.expand_dims(img, axis=0)

    return img

#### Display activations
def display_activations1(path, input_mod):

    x = preprocess_image(img_path=path,input_model=input_mod)
    
    # Get activation of an inputted image on all layers 
    activations = get_activations(input_mod, x)
    
    # Display activation of an inputted image on all layers
    display_activations(activations, save = False)
    
# Display heatmap of activation of an inputted image on all layers    
def display_heatmAps(path, input_mod):

    x = preprocess_image(img_path=path,input_model=input_mod)
    activations = get_activations(input_mod, x)
    
    display_heatmaps(activations, x, save=False)
