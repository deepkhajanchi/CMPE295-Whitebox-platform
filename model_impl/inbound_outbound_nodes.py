### Chi Tran: Master of Science - Software Engineering - SJSU - CMPE 295B - Fall 2020
### Common function to get all inbound and outbound nodes.

def get_inbound_nodes(input_model):
    count = 0
    for layer in input_model.layers:
        layer_name = layer.name
        #print('Layer name: ' + layer_name)
        for node in layer._inbound_nodes:
             for i in range(len(node.inbound_layers)):
                    count = count + 1
                    inbound_node_index = node.node_indices
                    strings = [str(integer) for integer in inbound_node_index]
                    a_string = "". join(strings)
                    an_integer = int(a_string)
                    #print(an_integer)
                    print("Inbound nodes of layer " + str(count) + " - layer name: " + layer_name)
                    print(layer.get_input_at(an_integer))
                    print(layer.get_output_at(an_integer))
                    print(layer.get_input_shape_at(an_integer))
                    print(layer.get_output_shape_at(an_integer))
                    print("================================================================================")


def get_outbound_nodes(input_model):
    count = 0
    for layer in input_model.layers:
        layer_name = layer.name
        for node in layer._outbound_nodes:
            if (node.outbound_layer != None):
                count = count + 1
            #for i in range(count):
                outbound_node_index = node.node_indices
                strings = [str(integer) for integer in outbound_node_index]
                a_string = "". join(strings)
                an_integer = int(a_string)
                #print(an_integer)
                print("Outbound nodes of layer " + str(count) + " - layer name: " + layer_name)
                print(layer.get_input_at(an_integer))
                print(layer.get_output_at(an_integer))
                print(layer.get_input_shape_at(an_integer))
                print(layer.get_output_shape_at(an_integer))
                print("================================================================================")
    print('Total outbound layer:%s' % count)