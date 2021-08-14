import requests, math,json,csv
import pandas as pd

class Stock:
    def __init__(self, symbol, date):
        # Set symbol, date
        self.symbol = str(symbol)
        self.date = date
        self.alphavantage_api_key = "EHYOFYX5N9729SP3"

        self.file = open('daily_data.csv', 'w', newline="")

        # Get daily data
        #self.daily_data = self.get_daily_data()

    def get_daily_data(self):
        # Get daily prices of stock for past 200 days
        request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={0}&apikey={1}".format(self.symbol, self.alphavantage_api_key)
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
        request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={0}&interval=1min&apikey={1}".format(self.symbol, self.alphavantage_api_key)
        r = requests.get(request_url)
        if r.status_code != 200:
            print("ERROR")
            return False

        # Return most recent data
        for key, value in r.json()["Time Series (1min)"].items():
            return float(value["4. close"])

    def get_moving_average(self, timeperiod):
        request_url = "https://www.alphavantage.co/query?function=SMA&symbol={0}&interval=daily&time_period={1}&series_type=close&apikey={2}".format(self.symbol, timeperiod, self.alphavantage_api_key)
        r = requests.get(request_url)
        if r.status_code != 200:
            return False
                                                                                                                                                                                                                                                                                                                                    
        data = requests.get(request_url)
        return data.json()["Technical Analysis: SMA"][self.date]["SMA"]

if __name__ == '__main__':
    stock = Stock("MSFT", "2021-05-27")
    print(stock.get_moving_average(200))
