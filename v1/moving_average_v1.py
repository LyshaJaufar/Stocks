import pandas as pd
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
from stock_v1 import Stock


class MovingAverage():
    def __init__(self, quantity, avg_price):
        self.invested = float(float(avg_price) * quantity)
        self.temp_value = 0
        self.profit = 0
        self.total_shares = quantity

        self.SMA_50 = None
        self.SMA_200 = None
        self.current_prices = None

    def decision(self, stock):
        # Compare 50 and 200 day averages. 
        # If 50 is greater, bullish -> buy
        # If 200 is greater, bearish -> sell

        # If price is greater than SMA, uptrend
        # price = SMA / crosses, trend reversal
        # price is less than SMA, downtrend

        # downtrend to uptrend --> buy
        # uptrend to downtrend --> sell

        self.current_prices = stock.get_daily_closing_price()
        print(self.current_prices)
        
        two_hundred_day_average = stock.get_moving_average(200)
        plot_two_hundred = stock.SMA_data
        self.SMA_200 = stock.SMA_values

        fifty_day_average = stock.get_moving_average(50)
        plot_fifty = stock.SMA_data
        self.SMA_50 = stock.SMA_values

        price = stock.price_data.iloc[0::]

        total_df = pd.concat([plot_two_hundred, plot_fifty, price], axis=1)
        total_df.plot()

        # Set legend
        legend = plt.legend()
        legend.get_texts()[0].set_text('SMA 200')
        legend.get_texts()[1].set_text('SMA 50')
        legend.get_texts()[2].set_text('Prices')


        plt.savefig('v1\SMA.png')
        plt.show()

        if (fifty_day_average > two_hundred_day_average):
            return 1
        elif (fifty_day_average < two_hundred_day_average):
            return -1
        else:
            return 0


if __name__ == '__main__':
    strategy = MovingAverage(10, '116.0')
    stock = Stock("IBM", "2021-08-12")
    decision = strategy.decision(stock)
    strategy.compare_two_hundred_and_fifty()

    print(decision)

