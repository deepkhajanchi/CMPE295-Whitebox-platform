import tensorflow as tf

### Chi Tran: Master of Science - Software Engineering - SJSU - CMPE 295B - Fall 2020
### Common function to get all hidden layers and layer information.

def print_hidden_layers(input_model):
    tf.compat.v1.disable_eager_execution()
    for layer in input_model.layers:
        hidden_layer = layer.output

        print(hidden_layer)
        
def print_layer_info(input_model):
    from tensorflow.keras.applications.vgg16 import VGG16
    from keras_sequential_ascii import keras2ascii

    #conv_base1 = VGG16(include_top=False,
     #                 weights='imagenet',
      #                input_shape=(image_height, image_width, 3))
    keras2ascii(input_model)