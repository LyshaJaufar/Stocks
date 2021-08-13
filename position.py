from stock import Stock

class Position:
    def __init__(self, symbol, quantity, avg_price):
        self.symbol = symbol
        self.quantity = quantity
        self.avg_price = avg_price
        self.stock = Stock(symbol, "2021-08-11")

    def open_pnl(self):
        # (current price - purchase price) x (number of outstanding shares purchased today)
        return (self.stock.get_current_price() - self.avg_price) * self.quantity

    def total_cost(self):
        return self.avg_price * self.quantity

    def current_value(self):
        return self.stock.get_current_price() * self.quantity

if __name__ == '__main__':
    td = Position("VXUS", 1, 143.47)
    shop = Position("TSLA", 10, 133.93)
    print(td.open_pnl())