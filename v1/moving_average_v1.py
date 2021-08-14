import pandas as pd
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
from stock_v1 import Stock


class MovingAverage():
    def decision(self, stock):
        # Compare 50 and 200 day averages. 
        # If 50 is greater, bullish -> buy
        # If 200 is greater, bearish -> sell

        two_hundred_day_average = stock.get_moving_average(200)
        plot_two_hundred = stock.SMA_data

        fifty_day_average = stock.get_moving_average(50)
        plot_fifty = stock.SMA_data

        total_df = pd.concat([plot_two_hundred, plot_fifty], axis=1)
        total_df.plot()

        # Set legend
        legend = plt.legend()
        legend.get_texts()[0].set_text('SMA 200')
        legend.get_texts()[1].set_text('SMA 50')

        plt.savefig('SMA.png')
        plt.show()

        if (fifty_day_average > two_hundred_day_average):
            return 1
        elif (fifty_day_average < two_hundred_day_average):
            return -1
        else:
            return 0 

if __name__ == '__main__':
    strategy = MovingAverage()
    stock = Stock("IBM", "2021-08-12")
    decision = strategy.decision(stock)

    print(decision)