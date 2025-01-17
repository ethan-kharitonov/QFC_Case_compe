class Market:
    def __init__(self) -> None:
        self.stocks = {"PeePee": 123, "PooPoo": 456}

    def updateMarket(self):
        #Will be implemented during grading
        pass
 
class Portfollio:
    def __init__(self) -> None:
        self.shares = {"PeePee": 0, "PooPoo": 0}
        self.cash = 1

    def evaluate(self, curMarket: Market) -> float:
        valueA = self.numSharesA * curMarket.stockPriceA
        valueB = self.numSharesB * curMarket.stockPriceB

        return valueA + valueB + self.cash

    def sell(self, stock_TSLA: str, sharesToSell: float, curMarket: Market) -> None:
        if sharesToSell > self.shares[stock_TSLA]:
            raise ValueError("Attempted to sell more stock that is available")

        self.shares[stock_TSLA] -= sharesToSell
        self.cash += sharesToSell * curMarket.stocks[stock_TSLA]

    def buy(self, stock_TSLA: str, sharesToBuy: float, curMarket: Market) -> None:
        cost = sharesToBuy * curMarket.stocks[stock_TSLA]
        if cost > self.cash:
            raise ValueError("Attempted to spend more cash than available")

        self.shares[stock_TSLA] += sharesToBuy
        self.cash -= cost

class Context:
    def __init__(self) -> None:
        pass

    #PUT WHATEVEAR YOU WANT HERE

def update_portfollio(curMarket: Market, curPortfollio: Portfollio, context: Context) -> Portfollio:
    #CODE HERE
    pass

###SIMULATION###
market = Market()
portfollio = Portfollio()
context = Context()

for i in range(1000):
    portfollio = update_portfollio(market, portfollio, context)
    market.updateMarket()

print(portfollio.evaluate())


