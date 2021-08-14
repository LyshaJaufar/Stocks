from stock_v1 import Stock

class Position:
    def __init__(self, symbol, quantity, avg_price):
        self.symbol = symbol
        self.quantity = quantity
        self.avg_price = avg_price
        self.stock = Stock(symbol, "2021-08-11")

    def open_pnl(self):
        # (current price - purchase price) x (number of outstanding shares purchased today)
        current = self.stock.get_current_price()
        print('current is: ', current)
        return (current - self.avg_price) * self.quantity

    def total_cost(self):
        return self.avg_price * self.quantity

    def current_value(self):
        return self.stock.get_current_price() * self.quantity

if __name__ == '__main__':
    IBM = Position("IBM", 5, 143.07)
    TESLA = Position("TSLA", 2, 722.25)
    print(IBM.open_pnl())