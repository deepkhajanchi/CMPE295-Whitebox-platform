
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from PIL import Image
from mpl_toolkits.axes_grid1 import ImageGrid
from keras.applications import imagenet_utils
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

def draw_acc_loss(points, factor=0.9):
  
  drawed_points = []
  for point in points:
    if drawed_points:
      prev = drawed_points[-1]
      drawed_points.append(prev * factor + point * (1 - factor))
    else:
      drawed_points.append(point)
  return drawed_points

def plot_data(history_data, smooth=False):

  accuracy = history_data.history['acc']
  validation_acc = history_data.history['val_acc']
  loss = history_data.history['loss']
  validation_loss = history_data.history['val_loss']

  epochs = range(1, len(accuracy)+1)
  
  if smooth == True:
    accuracy = draw_acc_loss(accuracy)
    validation_acc = draw_acc_loss(validation_acc)
    loss = draw_acc_loss(loss)
    validation_loss = draw_acc_loss(validation_loss)

  plt.plot(epochs, accuracy, 'g', label='Training accuracy')
  plt.plot(epochs, validation_acc,'r', label='Validation accuracy')
  plt.title('Training and validation accuracy')
  plt.legend()

  plt.figure()

  plt.plot(epochs, loss, 'g', label='Training loss')
  plt.plot(epochs, validation_loss, 'r', label='Validation loss')
  plt.title('Training and validation loss')
  plt.legend()

  plt.show()
  
def collect_metrics(model, generator, steps, class_names=[]):
  """
  Print out confusion matrix and classification report.
  """
  class_names = ['black_measles', 'black_rot', 'healthy', 'leaf_blight', 'mealybug', 'phylloxera']
  abbr = ['BM', 'BR', 'H', 'LB', 'M', 'P']
  
  # Generate predictions 
  y_pred = model.predict_generator(generator=generator, steps=steps)
  y_pred = np.argmax(a=y_pred, axis=1)
  
  # Generate confusion matrix
  con_matrix = confusion_matrix(y_true=generator.classes, y_pred=y_pred)
  fig, ax = plt.subplots(1)
  ax = sns.heatmap(con_matrix, ax=ax, cmap=plt.cm.YlOrRd, annot=True, fmt='g')
  ax.set_xticklabels(abbr)
  ax.set_yticklabels(abbr)
  plt.title('Confusion Matrix')
  plt.xlabel('Predicted Class')
  plt.ylabel('Real Class')
  plt.show()
  
  # Generate classification report
  print('Classification Report')
  print(classification_report(y_true=generator.classes, y_pred=y_pred, 
                              target_names=class_names))