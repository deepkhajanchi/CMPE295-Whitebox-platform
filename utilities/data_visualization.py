
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

### Chi Tran: Master of Science - Software Engineering - SJSU - CMPE 295B - Fall 2020
### Common functions to plot input data.

def pca(X=np.array([]), num_dimensions=60):
  """
  Runs PCA on an array X to reduce its dimensonality to 
  num_dimensions dimensions.
  
  """
  print('Running PCA ...')
  mean_vector = np.mean(a=X, axis=0)
  X_cov = (X-mean_vec).T.dot(X-mean_vec) / (X.shape[0]-1)
  eig_vals, eig_vectors = np.linalg.eig(X_cov.T)
  idx = np.argsort(np.abs(eig_vals))[::-1]
  eig_vectors = eig_vectors[:, idx]
  Y = np.dot(X, eig_vectors[:, 0:num_dimensions])
  return Y


def plot_scatter(x, class_name):
  """
  Function to create a scatter plot for visualization of data
  along with respective colors/labels.
 
  """
  no_class = len(np.unique(class_name))
  color_palette = np.array(sns.color_palette('Set2', no_class))
  f = plt.figure(figsize=(10,10))
  ax = plt.subplot(aspect='equal')
  for i, pic_label in enumerate(np.unique(class_name)):
    idx = np.where(class_name == pic_label)
    ax.scatter(x[idx,0], x[idx,1], s=30, alpha=0.6, 
                    c=[color_palette[i]], label=pic_label)
  ax.legend(loc='best', fontsize='medium')
  ax.axis('off')
  ax.axis('tight')
  plt.title('Visualization of grape diseases and pests in 2D')