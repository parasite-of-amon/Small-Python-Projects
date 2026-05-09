#region imports
from AlgorithmImports import *
#endregion

#region imports
from AlgorithmImports import *
#endregion

import pandas as pd
import numpy as np 

from keras.preprocessing.sequence import TimeseriesGenerator
from keras.models import Sequential
from keras.layers import LSTM, Dense

class MyAlgorithm(QCAlgorithm):

    def Initialize(self):
        # Define your starting and ending dates
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2022, 1, 1)

        # Define the symbols you want to retrieve data for
        symbols = [Symbol.Create("AAPL", SecurityType.Equity, Market.USA)]

        # Request historical data for the specified symbols and date range
        self.history = self.History(symbols, start_date, end_date, Resolution.Daily)
        
        # Perform data preprocessing
        if self.history is not None:
            # self.history.index = pd.to_datetime(self.history.index)
            self.Log(str(type(self.history['close'])))
            data = self.history['close']
            
            # Split the data into training and testing sets
            train_size = int(len(data) * 0.8)
            train_data, test_data = data[:train_size], data[train_size:]
            
            # Define the look-back window for the time series generator
            look_back = 10
            
            # Create the time series generator for training data
            train_generator = TimeseriesGenerator(train_data, train_data, length=look_back, batch_size=1)
            
            # Define and train a simple LSTM model
            model = Sequential()
            model.add(LSTM(50, activation='relu', input_shape=(look_back, 1)))
            model.add(Dense(1))
            model.compile(optimizer='adam', loss='mean_squared_error')
            
            # Track loss per epoch
            loss_per_epoch = []  # Initialize an empty list to store loss values
            
            # Train the model and collect loss values per epoch
            for epoch in range(10):
                model.fit(train_generator, epochs=1, verbose=0)  # Train for one epoch
                loss = model.evaluate(train_generator)  # Calculate loss for the current epoch
                loss_per_epoch.append(loss)
                self.Debug(f"Epoch {epoch + 1}, Loss: {loss:.4f}")
            
            self.model = model  # Store the trained model for later use
            self.look_back = look_back  # Store the look-back window size

    def OnData(self, slice):
        # This method is called for each data update
        
        if self.IsWarmingUp:
            return  # Do nothing during the warm-up period
        
        # Get the most recent price data
        price = self.Securities["AAPL"].Price
        
        # Create a window of past data for prediction
        past_data = self.history['close'][-self.look_back:].values
        
        # Reshape data to match the model's input shape
        past_data = past_data.reshape(1, -1, 1)
        
        # Make a prediction using the trained model
        prediction = self.model.predict(past_data)[0][0]
        
        # Define a threshold for trading decisions
        threshold = 0.01  # For simplicity, consider a buy/sell if the prediction is above/below this threshold
        
        if prediction > threshold:
            # Buy signal
            self.SetHoldings("AAPL", 1.0)  # Invest all capital in AAPL
        elif prediction < -threshold:
            # Sell signal
            self.Liquidate("AAPL")  # Liquidate all holdings of AAPL
