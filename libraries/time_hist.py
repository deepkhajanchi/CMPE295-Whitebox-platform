
import tensorflow as tf

### Chi Tran: Master of Science - Software Engineering - SJSU - CMPE 295B - Fall 2020
### Common function to get average training time on each epoch.

class TimeHistory(tf.keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.times = []

    def on_epoch_begin(self, batch, logs={}):
        self.epoch_time_start = time.time()

    def on_epoch_end(self, batch, logs={}):
        self.times.append(time.time() - self.epoch_time_start)