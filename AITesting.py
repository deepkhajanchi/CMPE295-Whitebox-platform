#!/usr/bin/env python
# coding: utf-8

# In[6]:


print('Model-Based AI Testing and Automation library imported')
import tensorflow as tf
import numpy as np
import io

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
        #print('The average loss for epoch {} is {:7.2f} and mean absolute error is {:7.2f}.'.format(epoch, logs['loss'], logs['mae']))
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
        
        
def get_model_summary(model):
    stream = io.StringIO()
    model.summary(print_fn=lambda x: stream.write(x + '\n'))
    summary_string = stream.getvalue()
    stream.close()
    return summary_string

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




