'''
'''

class timeSeriesForecast(df, method = 'ARIMA'):

    def __init__(self):
        self.method = method
        self.df = df

    def _preprocess_df(self):

        return self.df
