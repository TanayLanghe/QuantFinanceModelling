# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def main():
    ###SIMULATION###
    market = Market()
    portfolio = Portfolio()
    context = Context()

    for i in range(7):
        update_portfolio(market, portfolio, context)
        market.updateMarket()
    print(portfolio.evaluate(market))

class Market:
    transaction_fee = 0.005

    def __init__(self) -> None:
        self.stocks = {"HydroCorp": 123, "BrightFuture": 456}

    def updateMarket(self):
        # Will be implemented during grading.
        # This function will update the stock values to their "real" values each day.
        pass

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
    weekGrowthHC = [0.14837804, 0.152063779, 0.155620595, 0.159053872, 0.16236878, 0.165570283, 0.168663147, 0.171651949, 0.174541081, 0.177334764, 0.180037048, 0.182651821, 0.185182817, 0.187633622, 0.190007678, 0.192308288, 0.194538627, 0.196701739, 0.198800551, 0.20083787, 0.202816392, 0.204738707, 0.206607301, 0.208424559, 0.210192774, 0.211914147, 0.213590791, 0.215224735, 0.216817928, 0.218372241, 0.219889473, 0.221371348, 0.222819526, 0.224235598, 0.225621094, 0.226977484, 0.228306178, 0.229608534, 0.230885853, 0.232139387, 0.233370339, 0.234579865, 0.235769075, 0.236939037, 0.238090776, 0.23922528, 0.240343495, 0.241446333, 0.24253467, 0.24360935, 0.244671182, 0.245720945, 0.24675939, 0.247787238, 0.248805182, 0.249813891, 0.250814006, 0.251806147, 0.252790908, 0.253768864, 0.254740566, 0.255706546, 0.256667316, 0.257623369, 0.258575182, 0.259523212, 0.260467902, 0.261409677, 0.262348949, 0.263286114, 0.264221554, 0.265155639, 0.266088724, 0.267021155, 0.267953264, 0.268885371, 0.269817787, 0.270750813, 0.271684737, 0.272619842, 0.273556398, 0.274494669, 0.275434908, 0.276377363, 0.277322273, 0.278269868, 0.279220374, 0.280174009, 0.281130983, 0.282091502, 0.283055766, 0.284023969, 0.284996298, 0.285972937, 0.286954064, 0.287939852, 0.288930471, 0.289926085, 0.290926855, 0.291932937, 0.292944484, 0.293961646, 0.294984567, 0.296013391, 0.297048256, 0.298089299, 0.299136652, 0.300190448, 0.301250813, 0.302317873, 0.303391751, 0.304472568, 0.305560443, 0.306655491, 0.307757828, 0.308867567, 0.309984817, 0.311109688, 0.312242289, 0.313382724, 0.314531098, 0.315687514, 0.316852074, 0.318024879, 0.319206028, 0.320395619, 0.321593749, 0.322800514, 0.324016009, 0.325240328, 0.326473566, 0.327715813, 0.328967162, 0.330227704, 0.331497529, 0.332776727, 0.334065386, 0.335363596, 0.336671444, 0.337989017, 0.339316402, 0.340653686, 0.342000956, 0.343358296, 0.344725791, 0.346103528, 0.34749159, 0.348890063, 0.35029903, 0.351718574, 0.353148781, 0.354589733, 0.356041514, 0.357504206, 0.358977894, 0.360462659, 0.361958585, 0.363465754, 0.36498425, 0.366514154, 0.368055549, 0.369608517, 0.371173142, 0.372749505, 0.374337688, 0.375937775, 0.377549848, 0.379173989, 0.380810281, 0.382458806, 0.384119647, 0.385792887, 0.387478607, 0.389176892, 0.390887824, 0.392611485, 0.394347959, 0.396097329, 0.397859678, 0.39963509, 0.401423647, 0.403225434, 0.405040534, 0.40686903, 0.408711007, 0.410566548, 0.412435738, 0.41431866, 0.4162154, 0.418126041, 0.420050668, 0.421989367, 0.42394222, 0.425909315, 0.427890735, 0.429886566, 0.431896893, 0.433921802, 0.435961378, 0.438015706, 0.440084873, 0.44216896, 0.444268049, 0.446382207, 0.448511469, 0.450655771, 0.452814771, 0.45498733, 0.45717002, 0.459352877, 0.461507236, 0.463551035, 0.4652501, 0.465939648, 0.463756788, 0.453664573, 0.423364659, 0.350738539, 0.224859571, 0.078041365, -0.066152961, -0.203170609, -0.328017889, -0.42868702, -0.483432146, -0.481460713, -0.454636965, -0.425815243, -0.397837666, -0.370858714, -0.344854799, -0.319791801, -0.295635894, -0.272354267, -0.249915156, -0.228287822, -0.207442528, -0.187350518, -0.167983986, -0.149316059, -0.131320768, -0.113973024, -0.097248594, -0.081124079, -0.065576889, -0.050585218, -0.036128023, -0.022184999, -0.00873656, 0.004236188, 0.016751463, 0.028826832, 0.040479233, 0.051724991, 0.06257984, 0.073058944, 0.083176914, 0.092947825, 0.102385239, 0.111502218, 0.120311342, 0.128824726, 0.137054037, 0.145010508, 0.152704954, 0.160147788, 0.16734903, 0.174318331, 0.181064973, 0.187597896, 0.193925698, 0.200056657, 0.205998736, 0.211759599, 0.217346619, 0.222766889, 0.228027235, 0.233134223, 0.238094169, 0.24291315, 0.24759701, 0.252151372, 0.256581645, 0.26089303, 0.265090532, 0.269178962, 0.27316295, 0.277046947, 0.280835236, 0.284531936, 0.288141006, 0.291666256, 0.295111351, 0.298479815, 0.301775035, 0.305000272, 0.308158661, 0.311253217, 0.31428684, 0.317262319, 0.320182337, 0.323049475, 0.325866214, 0.328634941, 0.331357954, 0.334037461, 0.336675587, 0.339274377, 0.341835797, 0.344361738, 0.346854021, 0.349314398, 0.351744553, 0.354146108, 0.356520623, 0.358869599, 0.361194481, 0.36349666, 0.365777474, 0.368038211, 0.370280112, 0.372504369, 0.374712133, 0.376904509, 0.379082564, 0.381247323, 0.383399774, 0.385540869, 0.387671525, 0.389792624, 0.391905016, 0.394009523, 0.396106932, 0.398198006, 0.400283478, 0.402364055, 0.404440417, 0.406513222, 0.408583101, 0.410650658, 0.412716467, 0.414781057, 0.416844877, 0.418908204, 0.420970913, 0.42303189, 0.425087543, 0.427128045, 0.429127784, 0.431021203, 0.432641727, 0.433568514, 0.432749049, 0.427615073, 0.412281874, 0.375308745, 0.302801309, 0.196906078, 0.080456388]
    weekGrowthBF = [0.056158237, 0.061646181, 0.06690221, 0.071935467, 0.076754736, 0.081368457, 0.085784735, 0.090011356, 0.0940558, 0.097925247, 0.101626596, 0.10516647, 0.108551231, 0.111786985, 0.114879597, 0.117834697, 0.120657691, 0.123353767, 0.125927909, 0.128384897, 0.130729322, 0.132965591, 0.135097933, 0.137130406, 0.139066906, 0.140911173, 0.142666794, 0.144337213, 0.145925733, 0.147435526, 0.148869633, 0.150230974, 0.15152235, 0.152746448, 0.153905846, 0.155003018, 0.156040337, 0.157020078, 0.157944426, 0.158815475, 0.159635234, 0.160405631, 0.161128514, 0.161805655, 0.162438754, 0.163029443, 0.163579284, 0.164089777, 0.16456236, 0.16499841, 0.16539925, 0.165766148, 0.166100316, 0.166402921, 0.166675078, 0.166917858, 0.167132285, 0.167319343, 0.167479974, 0.16761508, 0.167725526, 0.16781214, 0.167875717, 0.167917018, 0.167936769, 0.167935669, 0.167914387, 0.167873561, 0.167813805, 0.167735705, 0.167639821, 0.167526692, 0.167396832, 0.167250732, 0.167088862, 0.166911674, 0.166719598, 0.166513044, 0.166292408, 0.166058064, 0.165810372, 0.165549677, 0.165276304, 0.164990569, 0.164692769, 0.16438319, 0.164062104, 0.163729771, 0.163386439, 0.163032342, 0.162667707, 0.162292746, 0.161907665, 0.161512655, 0.161107903, 0.160693582, 0.16026986, 0.159836894, 0.159394834, 0.158943821, 0.158483991, 0.158015471, 0.157538381, 0.157052835, 0.156558939, 0.156056796, 0.155546499, 0.15502814, 0.1545018, 0.15396756, 0.153425492, 0.152875666, 0.152318145, 0.151752988, 0.151180252, 0.150599985, 0.150012236, 0.149417046, 0.148814456, 0.1482045, 0.14758721, 0.146962615, 0.14633074, 0.145691607, 0.145045235, 0.144391641, 0.143730838, 0.143062836, 0.142387643, 0.141705264, 0.141015704, 0.140318961, 0.139615035, 0.138903921, 0.138185614, 0.137460104, 0.136727382, 0.135987435, 0.13524025, 0.13448581, 0.133724098, 0.132955093, 0.132178776, 0.131395122, 0.130604108, 0.129805707, 0.128999893, 0.128186635, 0.127365904, 0.126537668, 0.125701894, 0.124858547, 0.124007592, 0.123148991, 0.122282706, 0.121408698, 0.120526927, 0.119637349, 0.118739923, 0.117834605, 0.116921348, 0.116000108, 0.115070837, 0.114133486, 0.113188007, 0.112234349, 0.111272461, 0.11030229, 0.109323785, 0.108336889, 0.107341549, 0.106337709, 0.105325311, 0.104304298, 0.103274612, 0.102236193, 0.101188981, 0.100132914, 0.099067931, 0.097993968, 0.096910963, 0.09581885, 0.094717564, 0.093607039, 0.092487208, 0.091358004, 0.090219357, 0.089071198, 0.087913458, 0.086746064, 0.085568946, 0.084382031, 0.083185245, 0.081978514, 0.080761764, 0.079534919, 0.078297903, 0.077050643, 0.07579307, 0.07452513, 0.073246819, 0.071958273, 0.070660029, 0.069353785, 0.06804456, 0.066746898, 0.065502641, 0.064431821, 0.0638783, 0.06482623, 0.070088816, 0.087687449, 0.140350066, 0.291375648, 0.708638013, 1.776758348, 4.017929571, 6.846789615, 7.978179293, 7.864424503, 7.501707558, 6.855507504, 5.542731855, 3.087908129, 0.18574671, -1.040044527, -1.139625403, -1.101007153, -1.054807694, -1.009681005, -0.966140781, -0.924174129, -0.883733142, -0.844768493, -0.807231878, -0.77107621, -0.736255626, -0.702725488, -0.67044237, -0.639364051, -0.609449499, -0.580658857, -0.552953431, -0.526295669, -0.500649143, -0.475978531, -0.452249595, -0.429429162, -0.4074851, -0.386386298, -0.36610264, -0.346604986, -0.327865148, -0.309855863, -0.292550774, -0.275924407, -0.259952142, -0.244610196, -0.229875597, -0.215726161, -0.202140472, -0.189097856, -0.176578361, -0.164562738, -0.153032414, -0.141969474, -0.131356644, -0.121177265, -0.111415275, -0.102055194, -0.0930821, -0.084481612, -0.076239874, -0.068343537, -0.060779739, -0.053536095, -0.046600671, -0.03996198, -0.033608957, -0.027530951, -0.021717705, -0.016159349, -0.010846378, -0.005769648, -0.000920355, 0.00370997, 0.008129478, 0.012346012, 0.016367117, 0.020200052, 0.023851799, 0.027329076, 0.030638343, 0.033785814, 0.036777464, 0.03961904, 0.042316069, 0.044873865, 0.047297536, 0.049591995, 0.051761965, 0.053811985, 0.055746421, 0.057569468, 0.059285158, 0.060897367, 0.06240982, 0.063826097, 0.065149638, 0.066383751, 0.067531611, 0.06859627, 0.069580663, 0.070487605, 0.071319805, 0.072079863, 0.072770277, 0.073393445, 0.073951674, 0.074447175, 0.074882076, 0.075258416, 0.075578157, 0.075843181, 0.076055294, 0.076216231, 0.076327659, 0.076391175, 0.076408314, 0.07638055, 0.076309295, 0.076195906, 0.076041686, 0.075847885, 0.075615706, 0.075346311, 0.075040834, 0.074700414, 0.074326268, 0.073919885, 0.073483494, 0.073021263, 0.072542315, 0.07206837, 0.071653084, 0.071431086, 0.071742349, 0.073447659, 0.078728096, 0.093103944, 0.130482297, 0.225443446, 0.461047671, 1.019258237, 2.205611298, 4.157594758, 6.000083083, 6.597446904, 6.457402016]

    def __init__(self) -> None:
        self.first = []
        self.totalDay = 0
        self.noDay = [0, 1, 2, 3, 4, 5, 6, 7]
        self.prevDay = []
        self.hasVal = False
        self.confidence = [0, 0]
        self.BFCALC = 0
        self.HCCALC = 0
        self.buy = False

    def weekByWeek(self, currWeek: float, company: str) -> float:
        if company == "HC":
            weekGrowth = Context.weekGrowthHC
        elif company == "BF":
            weekGrowth = Context.weekGrowthBF
        else:
            return 0
        close = min(enumerate(weekGrowth), key=lambda x: abs(x[1] - currWeek))[0]
        if close == len(weekGrowth) - 1:
            return weekGrowth[close]
        return weekGrowth[close + 1]

    def weekCalc(self, first: float, seventh: float) -> float:
        return (seventh - first)/first * 100

    def dayAssign(self, market: Market) -> None:
        if len(self.prevDay) <= 4:
            self.prevDay.append(market.stocks["HydroCorp"])
            self.prevDay.append(market.stocks["BrightFuture"])
        else:
            self.prevDay[0] = self.prevDay[2]
            self.prevDay[1] = self.prevDay[3]
            self.prevDay[2] = self.prevDay[4]
            self.prevDay[3] = self.prevDay[5]
            self.prevDay[4] = market.stocks["HydroCorp"]
            self.prevDay[5] = market.stocks["BrightFuture"]

    def growth(self):
        if len(self.prevDay) == 6:
            HCOne = abs(self.prevDay[2] - self.prevDay[0])
            HCSec = abs(self.prevDay[4] - self.prevDay[2])
            BFOne = abs(self.prevDay[3] - self.prevDay[1])
            BFSec = abs(self.prevDay[5] - self.prevDay[3])
            if HCOne == 0 and BFOne != 0:
                return [HCSec, abs(BFSec - BFOne) / BFOne]
            elif HCOne != 0 and BFOne == 0:
                return [abs(HCSec - HCOne) / HCOne, BFSec]
            elif HCOne == 0 and BFOne == 0:
                return [HCSec, BFSec]
            else:
                DDHC = abs(HCSec - HCOne) / HCOne
                DDBF = abs(BFSec - BFOne) / BFOne
                return [DDHC, DDBF]
        return

def update_portfolio(curMarket: Market, curPortfolio: Portfolio, context: Context) -> None:
    context.totalDay = context.totalDay + 1
    context.dayAssign(curMarket)
    context.first.append(curMarket.stocks["HydroCorp"])
    context.first.append(curMarket.stocks["BrightFuture"])
    if context.totalDay not in context.noDay:
        HC = 0
        BF = 0
        if context.buy is False:
            HCshares = curPortfolio.cash * 0.7/((1 + curMarket.transaction_fee) * curMarket.stocks["HydroCorp"])
            curPortfolio.buy("HydroCorp", HCshares, curMarket)
            BFshares = curPortfolio.cash / ((1 + curMarket.transaction_fee) * curMarket.stocks["HydroCorp"])
            curPortfolio.buy("BrightFuture", BFshares, curMarket)
            context.buy = True
        if context.totalDay >= 6:
            context.hasVal = True
        weeklyHC = context.weekCalc(context.first[0], curMarket.stocks["HydroCorp"])
        weeklyBF = context.weekCalc(context.first[1], curMarket.stocks["BrightFuture"])
        context.weekGrowthHC.append(weeklyHC)
        context.weekGrowthBF.append(weeklyBF)
        if weeklyBF > 0.25 or weeklyHC > 0.25:
            grow = context.growth()
            if grow[0] < 0 or grow[1] < 0:
                context.noDay.append(context.totalDay + 1)
                context.noDay.append(context.totalDay + 2)
                context.noDay.append(context.totalDay + 3)
                curPortfolio.sell("HydroCorp", curPortfolio.shares["HydroCorp"], curMarket)
                curPortfolio.sell("BrightFuture", curPortfolio.shares["BrightFuture"], curMarket)

        if context.hasVal is True:
            context.first.pop(0)
            context.first.pop(0)
            HC = context.weekByWeek(weeklyHC, "HC")
            BF = context.weekByWeek(weeklyBF, "BF")
            context.hasVal = False
            context.HCCALC = context.confidence[0]/context.totalDay
            context.BFCALC = context.confidence[1] / context.totalDay
            netPercentHC = curPortfolio.shares["HydroCorp"] * curMarket.stocks["HydroCorp"] / curPortfolio.evaluate(curMarket)
            netPercentBF = curPortfolio.shares["BrightFuture"] * curMarket.stocks["BrightFuture"] / curPortfolio.evaluate(curMarket)
            if HC > BF:
                if netPercentHC < 0.80:
                    missingPerc = 0.80 - netPercentHC
                    neededMoney = curPortfolio.evaluate(curMarket) * missingPerc
                    stockToSell = neededMoney / ((1 + curMarket.transaction_fee) * curMarket.stocks["BrightFuture"])
                    if stockToSell > 0 and stockToSell <= curPortfolio.shares["BrightFuture"]:
                        curPortfolio.sell("BrightFuture", stockToSell, curMarket)
                        stockToBuy = curPortfolio.cash / (
                                    (1 + curMarket.transaction_fee) * curMarket.stocks["HydroCorp"])
                        curPortfolio.buy("HydroCorp", (stockToBuy - 1), curMarket)
                    elif stockToSell > 0 and stockToSell > curPortfolio.shares["BrightFuture"]:
                        curPortfolio.sell("BrightFuture", curPortfolio.shares["BrightFuture"], curMarket)
                        stockToBuy = curPortfolio.cash / (
                                    (1 + curMarket.transaction_fee) * curMarket.stocks["HydroCorp"])
                        curPortfolio.buy("HydroCorp", (stockToBuy - 1), curMarket)
            elif BF > HC:
                if netPercentBF < 0.80:
                    missingPerc = 0.80 - netPercentHC
                    neededMoney = curPortfolio.evaluate(curMarket) * missingPerc
                    stockToSell = neededMoney/((1 + curMarket.transaction_fee) * curMarket.stocks["HydroCorp"])
                    if stockToSell > 0 and stockToSell <= curPortfolio.shares["HydroCorp"]:
                        curPortfolio.sell("HydroCorp", stockToSell, curMarket)
                        stockToBuy = curPortfolio.cash/((1 + curMarket.transaction_fee) * curMarket.stocks["BrightFuture"])
                        curPortfolio.buy("BrightFuture", (stockToBuy - 1), curMarket)
                    elif stockToSell > 0 and stockToSell > curPortfolio.shares["HydroCorp"]:
                        curPortfolio.sell("HydroCorp", curPortfolio.shares["HydroCorp"], curMarket)
                        stockToBuy = curPortfolio.cash / ((1 + curMarket.transaction_fee) * curMarket.stocks["BrightFuture"])
                        curPortfolio.buy("BrightFuture", (stockToBuy - 1), curMarket)
            if curPortfolio.evaluate(curMarket) < 50000:
                curPortfolio.sell("HydroCorp", curPortfolio.shares["HydroCorp"], curMarket)
                curPortfolio.sell("BrightFuture", curPortfolio.shares["BrightFuture"], curMarket)


if __name__ == '__main__':
    main()
