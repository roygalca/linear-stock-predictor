import matplotlib.pyplot as plt


def plot_predictions(data, model):
    features = ['moving_avg_5']

    x = data[features].dropna()

    actual = data.loc[x.index, 'Close']
    predictions = model.predict(x)

    plt.figure(figsize=(10, 6))
    plt.plot(actual.index, actual, label='Actual Price')
    plt.plot(actual.index, predictions, label='Predicted Price')
    plt.legend()
    plt.show()
