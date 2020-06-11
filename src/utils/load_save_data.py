'''

.. module:: load_save_data
:synopsis: Contains functions to load and save files, either static data, or pickle files
'''

import pandas as pd
import os
from config_load import *


def load_static_files():
    '''
    Loads static files
    '''

    # load environment variables
    static_files = {}

    # load data
    static_files['TRAIN_DATA'] = pd.read_csv(env["TRAIN_FILE"])
    static_files['TEST_DATA'] = pd.read_csv(env["TEST_FILE"])
    static_files['ITEM_CATS_DATA'] = pd.read_csv(env['ITEM_CATS_FILE'])
    static_files['ITEMS_DATA'] = pd.read_csv(env['ITEMS_FILE'])
    static_files['SHOPS_DATA'] = pd.read_csv(env['SHOPS_FILE'])

    return static_files

def load_preprocessed_files():

    preprocessed_files = {}
    
    preprocessed_files['PREPROCESSED_TRAIN_DATA'] = pd.read_csv(env['PREPROCESSED_TRAIN_FILE'], index_col = 0)

    return preprocessed_files