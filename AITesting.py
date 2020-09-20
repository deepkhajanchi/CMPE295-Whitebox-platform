#!/usr/bin/env python
# coding: utf-8

# In[6]:


print('Model-Based AI Testing and Automation library imported ')
import tensorflow as tf
import numpy as np
import io
import psycopg2
from datetime import datetime
from numpy import *


class callback(tf.keras.callbacks.Callback):
    def __init__(self):
        print('init self')
    def on_train_batch_end(self, batch, logs=None):
        print('For batch {}, loss is {:7.2f}.'.format(batch, logs['loss']))
        print('For batch {}, accuracy is {:7.2f}.'.format(batch, logs['accuracy']))
    def on_test_batch_end(self, batch, logs=None):
        print('For batch {}, loss is {:7.2f}.'.format(batch, logs['loss']))
        print('For batch {}, accuracy is {:7.2f}.'.format(batch, logs['accuracy']))
    def MyCustomCallback():
        print('ccc')
    def on_epoch_end(self, epoch, logs=None):
        print('The average loss for epoch {} is {:7.2f} and mean absolute error is {:7.2f}.'.format(epoch, logs['loss'], logs['mae']))
        print('The average loss for epoch {} is {:7.2f} and accuracy is {:7.2f}.'.format(epoch, logs['loss'], logs['accuracy']))
        for i in range(len(self.model.layers)):
            layername = self.model.layers[i].name;
            layerconfig = self.model.layers[i].get_config()
            new_weights = self.model.layers[i].get_weights()
            print('Name of {} layers for epoch{} is {}'.format(i+1, epoch, layername))
            print('Config of {} layers for epoch{} is {}'.format(i+1, epoch, layerconfig))
            print('weights of {} layers for epoch{} is {}'.format(i+1, epoch, new_weights))
        if(logs.get('loss')<0.4):
            self.model.stop_training = True
        
        
def get_model_summary(model, conn):
    stream = io.StringIO()
    
#     model.summary(print_fn=lambda x: stream.write(x + '\n'))

    summary_string = stream.getvalue()
    stream.close()
    
    try:
        cur = conn.cursor()
        dt = datetime.now()
        print('PostgreSQL database version:')
        #cur.execute('INSERT INTO models(id, name, "createdAt", "updatedAt") VALUES (%s, %s, %s, %s)', (2, 'test', dt, dt,))
        #cur.execute('INSERT INTO configurations(id, name, "isOriginal", "layerNum", "activationFunction", regulation, "learningRate", "createdAt", "updatedAt", "modelId") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (1, 'test' , True, 3, 'actFunction', 'regulation', '00.0', dt, dt, '1'))  

        for idx in range(len(model.layers)):
            print(model.get_layer(index = idx).name)
            cur.execute('INSERT INTO layers (name, "createdAt", "updatedAt", "configurationId") VALUES (%s, %s, %s, %s)', ( model.get_layer(index=idx).name , dt, dt, '1', ))
       
        
        conn.commit()
        cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
        
    return summary_string

def get_bias_weight_in_each_layer(model):
    for layerNum, layer in enumerate(model.layers):
        
        name = model.layers[layerNum].name

        if name.startswith( 'flatten' ):
            layerNum = layerNum+1
        
        weights = model.layers[layerNum].get_weights()[0]
        biases = model.layers[layerNum].get_weights()[1]        
        
        for toNeuronNum, bias in enumerate(biases):
            print(f'{layerNum} B -> L{layerNum+1} N{toNeuronNum}: {bias}')

            
        for fromNeuronNum, wgt in enumerate(weights):
            for toNeuronNum, wgt2 in enumerate(wgt):
                print(f'L{layerNum}N{fromNeuronNum} -> L{layerNum+1}N{toNeuronNum}={wgt2}')

                
def insert_model_bias_weight(model, conn):
    try:
        cur = conn.cursor()
        dt = datetime.now()
        nodenum = 0
        
        
        cur.execute('INSERT INTO models(id, name, "createdAt", "updatedAt") VALUES (%s, %s, %s, %s)', (1, 'test', dt, dt,))
        cur.execute('INSERT INTO configurations(id, name, "isOriginal", "layerNum", "activationFunction", regulation, "learningRate", "createdAt", "updatedAt", "modelId") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (1, 'test' , True, len(model.layers), 'actFunction', 'regulation', '00.0', dt, dt, '1'))  
        
        
        for layerNum, layer in enumerate(model.layers):
        
            name = model.layers[layerNum].name
            print("name", name)
            cur.execute('INSERT INTO layers (id, name, "createdAt", "updatedAt", "configurationId") VALUES (%s, %s, %s, %s, %s)', ( layerNum, model.layers[layerNum].name , dt, dt, '1', ))
            
            if name.startswith( 'flatten' ):
                print('Flatten Skip - flatten Layer does not have weights and biases.' )

            else:
                weights = model.layers[layerNum].get_weights()[0]
                biases = model.layers[layerNum].get_weights()[1]        
               
                for toNeuronNum, bias in enumerate(biases):
                    #print(f'{layerNum} B -> L{layerNum+1} N{toNeuronNum}: {bias}')
                    nodenum = nodenum+1
                    neuronid = "L" + str(layerNum+1)+"N"+str(toNeuronNum) 
                    cur.execute('INSERT INTO neurons(id, bias, type, "activationFunction", "createdAt", "updatedAt", "layerId") VALUES (%s, %s, %s, %s, %s, %s, %s)', ( neuronid, double(bias) , name, 'actFunction', dt, dt, layerNum))

                for fromNeuronNum, wgt in enumerate(weights):
                    for toNeuronNum, wgt2 in enumerate(wgt):
                        #print(f'L{layerNum}N{fromNeuronNum} -> L{layerNum+1}N{toNeuronNum}={wgt2}')
                        fromNeuron = "L"+str(layerNum)+"N"+str(fromNeuronNum)
                        toNeuron = "L"+str(layerNum+1)+"N"+str(toNeuronNum)
                        linkid=fromNeuron+toNeuron
                        cur.execute('INSERT INTO links(id, weight, "createdAt", "updatedAt", "sourceId", "destId") VALUES (%s, %s, %s, %s, %s , %s)', ( linkid, double(wgt2) , dt, dt, fromNeuron, toNeuron))

        conn.commit()
        cur.close()
    
    
    #except (Exception, psycopg2.DatabaseError) as error:
        #print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
        
    return "finished"

        

            
class EarlyStoppingAtMinLoss(tf.keras.callbacks.Callback):
    def __init__(self, patience=0):
        super(EarlyStoppingAtMinLoss, self).__init__()
        self.patience = patience
        # best_weights to store the weights at which the minimum loss occurs.
        self.best_weights = None

    def on_train_begin(self, logs=None):
        # The number of epoch it has waited when loss is no longer minimum.
        self.wait = 0
        # The epoch the training stops at.
        self.stopped_epoch = 0
        # Initialize the best as infinity.
        self.best = np.Inf

    def on_epoch_end(self, epoch, logs=None):
        current = logs.get('loss')
        if np.less(current, self.best):
            self.best = current
            self.wait = 0
              # Record the best weights if current results is better (less).
            self.best_weights = self.model.get_weights()
        else:
            self.wait += 1
            if self.wait >= self.patience:
                self.stopped_epoch = epoch
                self.model.stop_training = True
                print('Restoring model weights from the end of the best epoch.')
                self.model.set_weights(self.best_weights)

    def on_train_end(self, logs=None):
        if self.stopped_epoch > 0:
            print('Epoch %05d: early stopping' % (self.stopped_epoch + 1))

class LossAndErrorPrintingCallback(tf.keras.callbacks.Callback):
    
    def on_train_batch_end(self, batch, logs=None):
        print('For batch {}, loss is {:7.2f}.'.format(batch, logs['loss']))

    def on_test_batch_end(self, batch, logs=None):
        print('For batch {}, loss is {:7.2f}.'.format(batch, logs['loss']))

    def on_epoch_end(self, epoch, logs=None):
        print('The average loss for epoch {} is {:7.2f} and mean absolute error is {:7.2f}.'.format(epoch, logs['loss'], logs['mae']))

        
def main(callback=None, cargs=()):
    print('Calling callback.')
    if callback != None:
        callback(*cargs)


# In[ ]:




