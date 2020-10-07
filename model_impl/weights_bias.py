
### Chi Tran: Master of Science - Software Engineering - SJSU - CMPE 295B - Fall 2020
### Common functions to extract weights and bias of all layers.

def extract_weights_bias(input_model):
    # Extract weights and bias on each layer
    for layer in input_model.layers:

        # Get layer name
        print("Layer name: ", layer.name, "\n")

        # Get layer configuration
        print("Layer configuration: ", layer.get_config(), "\n")

        # Get layer weights and bias
        w = layer.get_weights()
        if w != []:
            weights = layer.get_weights()[0]
            bias = layer.get_weights()[1]
            print("Layer weights: ", weights, "\n")
            print("Layer bias: ", bias, "\n")
        else:
            print("Layer weights and bias: ", w)