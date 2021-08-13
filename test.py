import requests, math,json,csv
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

class Stock:
    def __init__(self, symbol, date):
        # Set symbol, date
        self.symbol = str(symbol)
        self.date = date
        self.api_key = "EHYOFYX5N9729SP3"
        self.time_series = TimeSeries(key=self.api_key, output_format='pandas')
        self.tech_indicators = TechIndicators(key=self.api_key, output_format='pandas')
        # Get daily data
        #self.daily_data = self.get_daily_data()

    def get_daily_data(self):
        # Get daily prices of stock for past 200 days
        data_ts, meta_data_ts = self.time_series.get_daily(symbol=self.symbol, outputsize='full')
        
        # Get data from json of successful request
        return data_ts

    def get_current_price(self):
        # Get current price of stock (realtime)
        data_ts, meta_data_ts = self.time_series.get_intraday(symbol=self.symbol, interval='1min', outputsize='full')
       
        # Return most recent data
        return float(data_ts['4. close'][0])

    
