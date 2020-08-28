import os
import math


def rename_images(path, image_class):
  """
  Standardize file names.
  @param path - the path to the image directory
  @param image_class - name of the image class, such as black measles or black rot
  """
  for i, image in enumerate(os.listdir(path)):
    name = image_class + str(i) + '.jpg'
    source = os.path.join(path, image)
    dest = os.path.join(path, name)
    os.rename(source, dest)
  print('Finish renaming.')


def train_test_split_data(data_source, class_name, val_size=0.2, test_size=0.2):
  
  assert class_name in ['phylloxera', 'mealybug', 'black_measles', 'black_rot', 'leaf_blight', 'healthy'], \
    "Class name is invalid!"
  
  train_folder = os.path.join(data_source, 'train', class_name)
  val_folder = os.path.join(data_source, 'validation', class_name)
  test_folder = os.path.join(data_source, 'test', class_name)
  
  assert len(os.listdir(train_folder)) == 0, "Training directory must be empty."
  assert len(os.listdir(val_folder)) == 0, "Validation directory must be empty."
  assert len(os.listdir(test_folder)) == 0, "Test directory must be empty."
  
  path = os.path.join(data_source, class_name)
  total = len(os.listdir(path))
  
  # Shuffle the data
  data = os.listdir(path)
  random.shuffle(data)
  
  # Split train and test data: 80-20
  total_train = math.floor(total*0.8)
  total_test = total - total_train
  
  # Split train-validation data from train data: 80-20
  total_val = math.floor(total_train*0.2)
  total_train = total_train - total_val
  
  # Set data index
  train_dat = data[:total_train]
  val_dat = data[total_train:total_train+total_val]
  test_dat = data[total_train+total_val:]
    
  # Copy training data
  for file in train_dat:
    source = os.path.join(data_source, class_name, file)
    dest = os.path.join(train_folder, file)
    shutil.copyfile(source, dest)
    
  # Copy validation data
  for file in val_dat:
    source = os.path.join(data_source, class_name, file)
    dest = os.path.join(val_folder, file)
    shutil.copyfile(source, dest)
    
  # Copy test data
  for file in test_dat:
    source = os.path.join(data_source, class_name, file)
    dest = os.path.join(test_folder, file)
    shutil.copyfile(source, dest)