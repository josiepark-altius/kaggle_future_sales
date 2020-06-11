from sklearn.preprocessing import MinMaxScaler

def scale_data(train, test):
    scaler = MinMaxScaler
    scaler.fit(train)
    train = scaler.transform(train)
    test = scaler.transform(test) 

    return train, test, scaler 