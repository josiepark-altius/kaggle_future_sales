'''

.. module:: load_save_data
:synopsis: Contains functions to load and save files, either static data, or pickle files
'''

import pandas as pd
import os

def load_environment():
    '''
    Function that defines the names of configuration and data files

    Returns:
        environment_dict (dictionary) : 
    '''

    # load environment variables
    
    data_folder = os.environ.get("DATA_FOLDER")
    config_folder = os.environ.get("MODEL_CONFIG_FOLDER")

    # define environment dictionary

    environment_dict = {
        "TRAIN_FILE" : os.path.join(data_folder, "sales_train.csv"),
        "TEST_FILE" : os.path.join(data_folder, "test.csv"),
        "ITEM_CATS_FILE" : os.path.join(data_folder, "item_categories.csv"),
        "ITEMS_FILE" : os.path.join(data_folder, "items.csv"),
        "SHOPS_FILE" : os.path.join(data_folder, "shops.csv"),
        "SUBMISSION_FILE" : os.path.join(data_folder, "submission.csv"),
        "CONFIG_FILE" : os.path.join(config_folder, "dev.yaml"),
        "GROUPED_TRAIN_FILE" : os.path.join(data_folder, "grouped_train.csv"),
        "PREPROCESSED_TRAIN_FILE" : os.path.join(data_folder, "preprocessed_train.csv")
    }

    return environment_dict

def load_static_files():
    '''
    Loads static files
    '''

    # load environment variables
    static_files = {}
    env = load_environment()

    # load data
    static_files['TRAIN_DATA'] = pd.read_csv(env["TRAIN_FILE"])
    static_files['TEST_DATA'] = pd.read_csv(env["TEST_FILE"])
    static_files['ITEM_CATS_DATA'] = pd.read_csv(env['ITEM_CATS_FILE'])
    static_files['ITEMS_DATA'] = pd.read_csv(env['ITEMS_FILE'])
    static_files['SHOPS_DATA'] = pd.read_csv(env['SHOPS_FILE'])

    return static_files