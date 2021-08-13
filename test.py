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

        self.file = open('daily_data.csv', 'w', newline='')

        self.daily_data = self.get_daily_data()
        self.current_price = self.get_current_price()
        self.moving_average = self.get_moving_average(60)

    def get_daily_data(self):
        # Get daily prices of stock for past 200 days
        request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={0}&apikey={1}".format(self.symbol, self.api_key)
        r = requests.get(request_url)
        if r.status_code != 200:
            print("ERROR")
            return False
        
        # Get data from json of successful request
        response_dict = r.json()
        _, header = r.json()

        # Convert to pandas dataframe
        df = pd.DataFrame.from_dict(response_dict[header])

        # Write to csv file
        fieldnames = ['Date','Open','Low','Close', 'Volume']
        csvWriter = csv.DictWriter(self.file, fieldnames=fieldnames)
        csvWriter.writeheader()

        df.T.to_csv(self.file, header=False)

        df = pd.DataFrame.from_dict(response_dict[header], orient='index')
        return df

    def get_current_price(self):
        # Get current price of stock (realtime)
        data_ts, meta_data_ts = self.time_series.get_intraday(symbol=self.symbol, interval='1min', outputsize='full')
       
        # Return most recent data
        return float(data_ts['4. close'][0])

    def get_moving_average(self, timeperiod):
        data_ti, meta_data_ti = self.tech_indicators.get_sma(symbol=self.symbol, interval='daily',
                                            time_period=timeperiod, series_type='low')
        
        return float(data_ti['SMA'][-1])

    def plot_SMA(self, timeperiod):
        data_ts, meta_data_ts = self.time_series.get_intraday(symbol=self.symbol, interval='1min', outputsize='full')
        data_ti, meta_data_ti = self.tech_indicators.get_sma(symbol=self.symbol, interval='daily',
                                            time_period=timeperiod, series_type='low')
        
        df1 = data_ti
        df2 = data_ts['4. close'].iloc[timeperiod-1::]
        df2.index = df1.index

        total_df = pd.concat([df1, df2], axis=1)
        total_df.plot()
        plt.show()


if __name__ == '__main__':
    stock = Stock("MSFT", "2021-08-12")
    print(stock.plot_SMA(60))