from __future__ import (absolute_import, 
                    division, 
                    print_function, 
                    unicode_literals)
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from setup import data_normalization

### Chi Tran: Master of Science - Software Engineering - SJSU - CMPE 295B - Fall 2020
### Common functions to create data folders, build dataset, collect data in each class, and visualize input  data.

def create_data_folders():
    
    global data
    global bin_data
    global trained_models
    
    global phylloxera_fold
    global mealybug_fold
    global b_measles_fold
    global b_rot_fold
    global leaf_blight_fold
    global healthy
    
    global train_fold
    global val_fold
    global test_fold

    global train_phylloxera
    global train_mealybug
    global train_b_measles
    global train_b_rot
    global train_leaf_blight
    global train_healthy

    global val_phylloxera
    global val_mealybug 
    global val_b_measles
    global val_b_rot
    global val_leaf_blight
    global val_healthy
    
    global test_phylloxera
    global test_mealybug
    global test_b_measles
    global test_b_rot
    global test_leaf_blight
    global test_healthy

    # Set up main folders to store original images, binary data, and trained models
    root = '.'
    data = os.path.join(root, 'img_data') 
    bin_data = os.path.join(root, 'bin_data')
    trained_models = os.path.join(root, 'trained_models')

    # Original images
    phylloxera_fold = os.path.join(data, 'phylloxera')
    mealybug_fold = os.path.join(data, 'mealybug')
    b_measles_fold = os.path.join(data, 'black_measles')
    b_rot_fold = os.path.join(data, 'black_rot')
    leaf_blight_fold = os.path.join(data, 'leaf_blight')
    healthy = os.path.join(data, 'healthy')

    # Define train, validation, and test folders
    train_fold = os.path.join(data, 'train')
    val_fold = os.path.join(data, 'validation')
    test_fold = os.path.join(data, 'test')

    # Create sub-folders for each class in train folder
    train_phylloxera = os.path.join(train_fold, 'phylloxera')
    train_mealybug = os.path.join(train_fold, 'mealybug')
    train_b_measles = os.path.join(train_fold, 'black_measles')
    train_b_rot = os.path.join(train_fold, 'black_rot')
    train_leaf_blight = os.path.join(train_fold, 'leaf_blight')
    train_healthy = os.path.join(train_fold, 'healthy')

    # Create sub-folders for each class in validation folder
    val_phylloxera = os.path.join(val_fold, 'phylloxera')
    val_mealybug = os.path.join(val_fold, 'mealybug')
    val_b_measles = os.path.join(val_fold, 'black_measles')
    val_b_rot = os.path.join(val_fold, 'black_rot')
    val_leaf_blight = os.path.join(val_fold, 'leaf_blight')
    val_healthy = os.path.join(val_fold, 'healthy')

    # Create sub-folders for each class in test folder
    test_phylloxera = os.path.join(test_fold, 'phylloxera')
    test_mealybug = os.path.join(test_fold, 'mealybug')
    test_b_measles = os.path.join(test_fold, 'black_measles')
    test_b_rot = os.path.join(test_fold, 'black_rot')
    test_leaf_blight = os.path.join(test_fold, 'leaf_blight')
    test_healthy = os.path.join(test_fold, 'healthy')
  
def collect_images():
    global total_phylloxera
    global total_mealybug
    global total_b_measles
    global total_b_rot
    global total_leaf_blight
    global total_healthy
    
    total_phylloxera = len(os.listdir(phylloxera_fold))
    total_mealybug = len(os.listdir(mealybug_fold))
    total_b_measles = len(os.listdir(b_measles_fold))
    total_b_rot = len(os.listdir(b_rot_fold))
    total_leaf_blight = len(os.listdir(leaf_blight_fold))
    total_healthy = len(os.listdir(healthy))

    total_images = total_phylloxera + total_mealybug + total_b_measles + total_b_rot + total_leaf_blight + total_healthy

    #print('Total Images: {}'.format(total_images))
    print('There are {} images in phylloxera class'.format(total_phylloxera))
    print('There are {} images in mealybug class'.format(total_mealybug))
    print('There are {} images in black measles class'.format(total_b_measles))
    print('There are {} images in black rot class'.format(total_b_rot))
    print('There are {} images in leaf blight class'.format(total_leaf_blight))
    print('There are {} images in healthy class'.format(total_healthy))
    
def build_dataset():
    
    # Create folders to store original images, binary data, and trained models
    os.mkdir(data)
    os.mkdir(bin_data)
    os.mkdir(trained_models)

    # Create train, validation, and test folders
    os.mkdir(train_fold)
    os.mkdir(val_fold)
    os.mkdir(test_fold)

    # Create sub-folders for each class inside the train folder
    os.mkdir(train_phylloxera)
    os.mkdir(train_mealybug)
    os.mkdir(train_b_measles)
    os.mkdir(train_b_rot)
    os.mkdir(train_leaf_blight)
    os.mkdir(train_healthy)

    # Create sub-folders for each class inside the validation folder
    os.mkdir(val_phylloxera)
    os.mkdir(val_mealybug)
    os.mkdir(val_b_measles)
    os.mkdir(val_b_rot)
    os.mkdir(val_leaf_blight)
    os.mkdir(val_healthy)

    # Create sub-folders for each class inside the test folder
    os.mkdir(test_phylloxera)
    os.mkdir(test_mealybug)
    os.mkdir(test_b_measles)
    os.mkdir(test_b_rot)
    os.mkdir(test_leaf_blight)
    os.mkdir(test_healthy)
    
def data_dist():
    # Show data distribution using bar charts
    data_col = pd.DataFrame.from_dict(data={ 'phylloxera': [total_phylloxera],
                                            'mealybug': [total_mealybug],
                                             'blk measles': [total_b_measles],
                                              'blk rot': [total_b_rot],
                                              'leaf blight': [total_leaf_blight],
                                              'healthy': [total_healthy]
                                              } )
    sns.barplot(data=data_col);
    plt.xlabel('Class name');
    plt.ylabel('Quantity');
    plt.title('Data distribution');


def rename_img():
    # Rename images in each folder
    data_normalization.rename_images(phylloxera_fold, image_class='phylloxera')
    data_normalization.rename_images(mealybug_fold, image_class='mealybug')
    data_normalization.rename_images(b_measles_fold, image_class='black_measles')
    data_normalization.rename_images(b_rot_fold, image_class='black_rot')
    data_normalization.rename_images(leaf_blight_fold, image_class='leaf_blight')
    data_normalization.rename_images(healthy, image_class='healthy')