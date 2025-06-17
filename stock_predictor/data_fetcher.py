import yfinance as yf


def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start_date, end_date)
    data.columns = data.columns.get_level_values(0)

    return data


def add_features(data):
    data['daily return'] = data['Close'].pct_change()
    data['moving_avg_5'] = data['Close'].rolling(window=5).mean()
    return data
