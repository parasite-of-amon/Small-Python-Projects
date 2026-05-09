import yfinance as yf

import pandas as pd
import numpy as np

from keras.preprocessing.sequence import TimeseriesGenerator
from keras.models import Sequential
from keras.layers import LSTM, Dense

import tensorflow 


class YahooFinanceStockData:
    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol

    def get_historical_data(self, start_date, end_date):
        stock_data = yf.download(self.stock_symbol, start=start_date, end=end_date)
        return stock_data

class StockPricePredictor:
    def __init__(self, stock_symbol, start_date, end_date):
        self.stock_data = YahooFinanceStockData(stock_symbol).get_historical_data(start_date, end_date)

    def train_lstm_model(self, look_back=10, num_epochs=10):
        if self.stock_data is not None:
            data = self.stock_data['Adj Close'].values
            train_size = int(len(data) * 0.8)
            train_data, test_data = data[:train_size], data[train_size:]
            train_generator = TimeseriesGenerator(train_data, train_data, length=look_back, batch_size=1)

            model = Sequential()
            model.add(LSTM(50, activation='relu', input_shape=(look_back, 1)))
            model.add(Dense(1))
            model.compile(optimizer='adam', loss='mean_squared_error')

            for epoch in range(num_epochs):
                model.fit(train_generator, epochs=1, verbose=0)
                loss = model.evaluate(train_generator)
                print(f"Epoch {epoch + 1}, Loss: {loss:.4f}")

            self.model = model
            self.look_back = look_back

    def predict_price(self):
        past_data = self.stock_data['Adj Close'][-self.look_back:].values
        past_data = past_data.reshape(1, -1, 1)
        prediction = self.model.predict(past_data)[0][0]
        return prediction

if __name__ == "__main__":
    stock_symbol = "AAPL"  # Replace with the stock symbol you're interested in
    start_date = "2022-01-01"
    end_date = "2022-12-31"

    price_predictor = StockPricePredictor(stock_symbol, start_date, end_date)
    price_predictor.train_lstm_model(look_back=10, num_epochs=10)
    prediction = price_predictor.predict_price()

    print(f"Predicted Price Change: {prediction:.4f}")
