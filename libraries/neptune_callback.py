
from tensorflow.keras.callbacks import Callback
import neptune
import numpy as np
from scikitplot.metrics import plot_confusion_matrix, plot_roc
import matplotlib.pyplot as plt


neptune.init('', api_token='')
neptune.create_experiment(name='minimal_example')

class NeptuneLoggerCallback(Callback):
    def __init__(self, model, generator, steps):
        super().__init__()
        self.model = model
        self.generator = generator
        self.steps = steps

    def on_batch_end(self, batch, logs={}):
        for log_name, log_value in logs.items():
            neptune.log_metric(f'batch_{log_name}', log_value)

    def on_epoch_end(self, epoch, logs={}):
        for log_name, log_value in logs.items():
            neptune.log_metric(f'epoch_{log_name}', log_value)

        y_pred = self.model.predict_generator(self.generator, self.steps)
        y_true = self.generator.classes

        y_pred_class = np.argmax(y_pred, axis=1)

        fig, ax = plt.subplots(figsize=(16, 12))
        plot_confusion_matrix(y_true, y_pred_class, ax=ax)
        neptune.log_image('confusion_matrix', fig)

        fig, ax = plt.subplots(figsize=(16, 12))
        plot_roc(y_true, y_pred, ax=ax)
        neptune.log_image('roc_curve', fig)