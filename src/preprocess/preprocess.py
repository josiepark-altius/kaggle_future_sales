import sys
sys.path.append('../../')

import pandas as pd
import os
import numpy as np
from dotenv import load_dotenv
from itertools import product
from src.utils.load_save_data import load_environment, load_static_files, load_preprocessed_files
from config_load import *

def remove_duplicate_shops(df):

    df.loc[df['shop_id'] == 0, 'shop_id'] = 57
    df.loc[df['shop_id'] == 1, 'shop_id'] = 58
    df.loc[df['shop_id'] == 10, 'shop_id'] = 11

    return df

def make_grouped_dataset(train, save_file = False):

    grouped_train = train.groupby(['date_block_num', 'shop_id','item_id'])['date','item_price', 'item_cnt_day'].agg({'date' : ['min','max'], 'item_price' : 'mean', 'item_cnt_day':'sum'}).reset_index()

    if save_file:
        # save to file
        grouped_train.to_csv(env['GROUPED_TRAIN_FILE'])
        
    return grouped_train

def create_shop_item_month_dataset(train):

    train['date'] = pd.to_datetime(train['date'], format = '%d.%m.%Y')

    # get unique month identifiers
    months = train['date_block_num'].unique()

    cartesian = []

    for month in months:
        shops_in_month = train.loc[train['date_block_num'] == month, 'shop_id'].unique()
        items_in_month = train.loc[train['date_block_num'] == month, 'item_id'].unique()
        cartesian.append(np.array(list(product(*[shops_in_month, items_in_month, [month]])), dtype = 'int32'))

    cartesian_df = pd.DataFrame(np.vstack(cartesian), columns = ['shop_id', 'item_id', 'date_block_num'], dtype = np.int32)
    
    return cartesian_df

def preprocess_train(train, save_file = False):

    train = train[train['item_price'] < 100000]
    train = train[train['item_cnt_day'] < 1000]

    tmp_mean = train[(train['date_block_num'] == 4) & (train['item_id'] == 2973) & (train['item_price'] > 0) & (train['shop_id'] == 32)].mean()
    train.loc[train['item_price'] < 0, 'item_price'] = tmp_mean

    train = remove_duplicate_shops(train)

    grouped_train = make_grouped_dataset(train, save_file = save_file)
    cartesian_df = create_shop_item_month_dataset(train)

    train = pd.merge(cartesian_df, grouped_train, on = ['shop_id', 'item_id', 'date_block_num'], how = 'left').fillna(0)
    train.sort_values(['date_block_num','shop_id','item_id'], inplace = True)

    # rename columns 
    train = train.rename(columns = {'(\'item_price\', \'mean\')' : 'item_price', '(\'item_cnt_day\', \'sum\')' : 'item_cnt'}, inplace = True)
    

    if save_file:
        train.to_csv(env['PREPROCESSED_TRAIN_FILE'])
    
    return train

def main():

    # check if preprocessed file exists
    preprocess_file_name = env["PREPROCESSED_TRAIN_FILE"]
    read_file = os.path.exists(preprocess_file_name)

    if read_file:
        print('Preprocessed training file already exists, reading from file')
        preprocessed_files = load_preprocessed_files()
        train = preprocessed_files['PREPROCESSED_TRAIN_DATA']
    else:
        print('Preprocess training file does not exist, generating file')
        static_files = load_static_files()
        train = preprocess_train(static_files['TRAIN_DATA'], save_file = True)

    return train

if __name__ == '__main__':

    main()