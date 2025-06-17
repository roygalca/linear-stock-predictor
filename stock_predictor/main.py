from data_fetcher import fetch_stock_data
from data_fetcher import add_features
from LRmodel import train_model
from visualize import plot_predictions
data = fetch_stock_data("AAPL", "2020-01-01", "2023-12-31")
data = add_features(data)
model = train_model(data)
plot_predictions(data, model)
