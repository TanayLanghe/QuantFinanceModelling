# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def main():
    ###SIMULATION###
    market = Market()
    portfolio = Portfolio()
    context = Context()


    # for i in range(7):
    #     update_portfolio(market, portfolio, context)
    #     market.updateMarket()
    # print(portfolio.evaluate(market))
    with open('data.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        values = line.strip().split()
        update(market, float(values[0]), float(values[1]))
        update_portfolio(market, portfolio, context)


class Market:
    transaction_fee = 0.005

    def __init__(self) -> None:
        self.stocks = {"HydroCorp": 123, "BrightFuture": 456}

    def updateMarket(self):
        # Will be implemented during grading.
        # This function will update the stock values to their "real" values each day.
        pass

def update(market: Market, HC: float, BF: float) -> None:
    market.stocks["HydroCorp"] = HC
    market.stocks["BrightFuture"] = BF

class Portfolio:
    def __init__(self) -> None:
        self.shares = {"HydroCorp": 0, "BrightFuture": 0}
        self.cash = 100000

    def evaluate(self, curMarket: Market) -> float:
        valueA = self.shares["HydroCorp"] * curMarket.stocks["HydroCorp"]
        valueB = self.shares["BrightFuture"] * curMarket.stocks["BrightFuture"]

        return valueA + valueB + self.cash

    def sell(self, stock_TSLA: str, sharesToSell: float, curMarket: Market) -> None:
        if sharesToSell <= 0:
            raise ValueError("Number of shares must be positive")

        if sharesToSell > self.shares[stock_TSLA]:
            raise ValueError("Attempted to sell more stock than is available")

        self.shares[stock_TSLA] -= sharesToSell
        self.cash += (1 - Market.transaction_fee) * sharesToSell * curMarket.stocks[stock_TSLA]

    def buy(self, stock_TSLA: str, sharesToBuy: float, curMarket: Market) -> None:
        if sharesToBuy <= 0:
            raise ValueError("Number of shares must be positive")

        cost = (1 + Market.transaction_fee) * sharesToBuy * curMarket.stocks[stock_TSLA]
        if cost > self.cash:
            raise ValueError("Attempted to spend more cash than available")

        self.shares[stock_TSLA] += sharesToBuy
        self.cash -= cost


class Context:
    weekGrowthHC = [0.14837804, 0.171651949, 0.190007678, 0.204738707, 0.216817928, 0.226977484,
                    0.235769075, 0.24360935, 0.250814006, 0.257623369, 0.264221554, 0.270750813,
                    0.277322273, 0.284023969, 0.290926855, 0.298089299, 0.305560443, 0.313382724,
                    0.321593749, 0.330227704, 0.339316402, 0.348890063, 0.358977894, 0.369608517,
                    0.380810281, 0.392611485, 0.405040534, 0.418126041, 0.431896893, 0.446382207,
                    0.461507236, 0.350738539, -0.483432146, -0.319791801, -0.167983986]
    weekGrowthBF = [0.056158237, 0.090011356, 0.114879597, 0.132965591, 0.145925733, 0.155003018,
                    0.161128514, 0.16499841, 0.167132285, 0.167917018, 0.167639821, 0.166513044,
                    0.164692769, 0.162292746, 0.159394834, 0.156056796, 0.152318145, 0.1482045,
                    0.143730838, 0.138903921, 0.133724098, 0.128186635, 0.122282706, 0.116000108,
                    0.109323785, 0.102236193, 0.094717564, 0.086746064, 0.078297903, 0.069353785,
                    0.070088816, 6.846789615, 0.18574671, -0.924174129, -0.67044237]

    def __init__(self) -> None:
        self.day = 0
        self.first = []
        self.totalDay = 0
        self.noDay = [1]

    def weekByWeek(self, currWeek: float, company: str) -> float:
        close = 0
        if company == "HC":
            weekGrowth = Context.weekGrowthHC
        elif company == "BF":
            weekGrowth = Context.weekGrowthBF
        else:
            return 0
        for i in range(len(weekGrowth)):
            if abs(currWeek - weekGrowth[i]) < abs(currWeek - weekGrowth[close]):
                close = i
        # print(f"the week this is based off is week" + str(close))
        return weekGrowth[close + 1]

    def weekCalc(self, first: float, seventh: float) -> float:
        return round((seventh - first) / first, 10)


def update_portfolio(curMarket: Market, curPortfolio: Portfolio, context: Context) -> None:
    context.day = context.day + 1
    context.totalDay = context.totalDay + 1
    if context.totalDay not in context.noDay:
        print(context.day)
        HC = 0
        BF = 0
        Pass = False
        if context.day == 1 or context.first == []:
            context.first.append(curMarket.stocks["HydroCorp"])
            context.first.append(curMarket.stocks["BrightFuture"])
            Pass = True
        print(context.first)
        if context.day == 7 and Pass == True:
            weeklyHC = context.weekCalc(context.first[0], curMarket.stocks["HydroCorp"])
            weeklyBF = context.weekCalc(context.first[1], curMarket.stocks["BrightFuture"])
            HC = context.weekByWeek(weeklyHC, "HC")
            BF = context.weekByWeek(weeklyBF, "BF")
            context.first = []
            context.day = 0
            print(HC)
            print(BF)


if __name__ == '__main__':
    main()
