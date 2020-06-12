import sys
sys.path.append('../../')

from config_load import *

from keras.layers import Dense, Activation, Dropout, LSTM
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler

import numpy as np
import pandas as pd

class LSTMModel():
    '''
    LSTM model
    '''
    def __init__(self, config):

        self.model = Sequential()
        self.batch_size = config["batch_size"]
        self.neurons = config["neurons"]
        self.optimzer = config["optimizer"]
        self.loss = config["loss"]
        self.drop_out = config["drop_out"]
        self.activation = config["activation"]
        self.n_epochs = config["n_epochs"]

    def prepare_data(self, train, test):

        self.n_input = len(train['date_block_num'].drop_duplicates()) - 1 
        self.n_features = 1

        self.scaler = MinMaxScaler()
        self.scaler.fit(train['item_cnt_day'].values.reshape(1,-1))
        train['scaled_item_cnt_day'] = self.scaler.transform(train['item_cnt_day'].values.reshape(1,-1))
        test['scaled_item_cnt_day'] = self.scaler.transform(test['item_cnt_day'].values.reshape(1,-1))

        train.drop(['item_cnt_day'], inplace = True, axis = 1)
        test.drop(['item_cnt_day'], inplace = True, axis = 1)

        df = train.pivot_table(index = ['shop_id', 'item_id'], 
        values = ['scaled_item_cnt_day'],
        columns = ['date_block_num'],
        fill_value = 0,
        aggfunc = 'sum')
        df.reset_index(inplace = True)
        df = pd.merge(test, df, on = ['item_id', 'shop_id'], how = 'left')

        df.fillna(0, inplace = True)
        df.drop(['shop_id', 'item_id', 'ID'], inplace = True, axis = 1)


        self.X_train = np.expand_dims(df.values[:,:-1], axis = 2)
        self.y_train = df.values[:, -1:]

        self.X_test = np.expand_dims(df.values[:,1:], axis = 2)
    
    def build(self):
        self.model.add(LSTM(self.neurons,
        input_shape = (self.n_input, self.n_features),
        activation = self.activation))
        self.model.add(Dropout(self.drop_out))
        self.model.add(Dense(1))
        self.model.compile(optimizer = self.optimzer, loss = self.loss)

    def fit(self):
        self.model.fit(self.X_train, self.y_train, 
        epochs = self.n_epochs, batch_size = self.batch_size)

    def predict(self):
        _prediction = self.model.predict(self.X_test)
        y_test = self.scaler.inverse_transform(_prediction)
        self.prediction = y_test.clip(0,20)

    def generate_submission(self, test):
        submission_df = pd.DataFrame({'ID': test['ID'], 
        'item_cnt_month' : self.prediction.ravel()})

        submission_df.to_csv(env['SUBMISSION_FILE'])

    def main(self, train, test):
        self.prepare_data(train, test)
        self.build()
        self.fit()
        self.predict()
        self.generate_submission(test)


