
from stock import Stock

class MovingAverage():
    def decision(self, stock):
        # Compare 50 and 200 day averages. 
        # If 50 is greater, bullish -> buy
        # If 200 is greater, bearish -> sell

        two_hundred_day_average = stock.get_moving_average(200)
        fifty_day_average = stock.get_moving_average(50)

        if (fifty_day_average > two_hundred_day_average):
            return 1
        elif (fifty_day_average < two_hundred_day_average):
            return -1
        else:
            return 0

if __name__ == '__main__':
    strategy = MovingAverage()
    stock = Stock("IBM", "2021-08-12")
    #stock1 = Stock("MSFT", "2021-08-12")
    #stock2 = Stock("TSLA", "2021-08-12")
    decision = strategy.decision(stock)

    print(decision)