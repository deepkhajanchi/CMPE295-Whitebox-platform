import numpy as np

def get_misclassified_images(input_model, gen, step):
    
    # Look for all misclassified images 
    y_pred = input_model.predict_generator(generator=gen, steps=step)
    y_pred = np.argmax(y_pred, axis=1)
    y_real = gen.classes

    # Show indices of these misclassified images
    global index
    index = np.where(np.not_equal(y_pred, y_real))
    
    # Display paths of misclassified images
    global paths
    paths = [gen.filepaths[i] for i in index[0]]
    return paths
