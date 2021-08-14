from position_v1 import Position

class Portfolio:
    def __init__(self, positions):
        # positions: array of Position objects
        self.positions = positions

    def open_pnl(self):
        self.pnl = 0
        for position in self.positions:
            openpnl = position.open_pnl()
            print(openpnl)
            self.pnl += openpnl
        return self.pnl

    def total_cost(self):
        self.cost = 0
        for position in self.positions:
            self.cost += position.total_cost()
        return self.cost

    def current_value(self):
        self.value = 0
        for position in self.positions:
            self.value += position.current_value()
        return self.value

if __name__ == '__main__':
    p = Portfolio([Position("TSLA", 2, 722.25), Position("MSFT", 5, 289.81), Position("IBM", 5, 143.07)])
    print(p.total_cost())
    print(p.current_value())