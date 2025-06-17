from sklearn.linear_model import LinearRegression
import pandas as pd


def train_model(data):
    data = data.dropna()

    x = data[['moving_avg_5']]
    y = data['Close']

    model = LinearRegression()
    model.fit(x, y)

    return model
