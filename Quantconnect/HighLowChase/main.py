# region imports
from AlgorithmImports import *
# endregion


class UglyFluorescentPinkDinosaur(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2024, 5, 19)
        self.SetCash(100000)

        self.symbol = self.AddEquity("AAPL", Resolution.Minute).Symbol

        self.AddEquity("GOOGL", Resolution.Minute)
        self.AddEquity("MSFT", Resolution.Minute)

        history = self.History(self.symbol, 200, Resolution.Daily)

        if history.empty:
            self.Debug("No historical data found.")
            return

        self.high_prices = history["high"].values
        self.low_prices = history["low"].values

        self.high_value = max(self.high_prices)
        self.low_value = min(self.low_prices)

        self.Debug(f"200-day high: {self.high_value}")
        self.Debug(f"200-day low: {self.low_value}")

    def OnData(self, slice):
        if self.symbol not in slice:
            return

        apple_data = slice[self.symbol]
        close_price = apple_data.Close

        self.Debug(f"AAPL Close Price: {close_price}")

        if close_price > self.high_value + 1:
            self.Debug("Price broke above high. Liquidating AAPL.")
            self.Liquidate(self.symbol)

        elif close_price < self.low_value - 1:
            self.Debug("Price broke below low. Buying AAPL.")
            self.SetHoldings(self.symbol, 0.999)
