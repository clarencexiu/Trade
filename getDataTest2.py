from ctaTemplate import *
from vtObject import *

"""
获取买1-5，卖1-5
"""
class getDataTest2(CtaTemplate):
    author = 'shushi'
    className = 'getDataTest2'

    # 参数映射表
    paramMap = {
        'exchange': '交易所',
        'vtSymbol': '标准套利合约',
        'period': '分钟线周期'
    }

    # 参数列表，保存了参数的名称
    paramList = list(paramMap.keys())

    # 变量映射表
    varMap = {
        'trading': '交易中',
        'pos': '当前持仓'
    }

    # 变量列表，保存了变量的名称
    varList = list(varMap.keys())

    def __init__(self,ctaEngine=None,setting={}):
        super(getDataTest2,self).__init__(ctaEngine,setting)
        self.period = 5
        self.exchange = "SHFE"
        self.vtSymbol = "ag2401"


    def onTick(self, tick: VtTickData):
        self.output('time: {} {}'.format(tick.date,tick.time))
        self.output('s5: {}   {}'.format(tick.askPrice5,tick.askVolume5))
        self.output('s4: {}   {}'.format(tick.askPrice4,tick.askVolume4))
        self.output('s3: {}   {}'.format(tick.askPrice3,tick.askVolume3))
        self.output('s2: {}   {}'.format(tick.askPrice2,tick.askVolume2))
        self.output('s1: {}   {}'.format(tick.askPrice1,tick.askVolume1))
        self.output('b1: {}   {}'.format(tick.bidPrice1,tick.bidVolume1))
        self.output('b2: {}   {}'.format(tick.bidPrice2,tick.bidVolume2))
        self.output('b3: {}   {}'.format(tick.bidPrice3,tick.bidVolume3))
        self.output('b4: {}   {}'.format(tick.bidPrice4,tick.bidVolume4))
        self.output('b5: {}   {}'.format(tick.bidPrice5,tick.bidVolume5))
        self.output('-----------------------------------------------------')
        flag = (tick.bidPrice1 + tick.bidPrice2 + tick.bidPrice3 + tick.bidPrice4 + tick.bidPrice5)/(tick.askPrice1 + tick.askPrice2 + tick.askPrice3 + tick.askPrice4 + tick.askPrice5)
        self.output('支撑强度: {}'.format(flag))
        if flag > 3:
            self.output("{} {} : {}异动".format(tick.date,tick.time,self.vtSymbol))
        self.output('=================================================')
        super().onTick(tick)
        #self.bm.updateTick(tick)
    #
    # def onBar(self, bar):
    #     self.am3.updateBar(bar)
    #     self.bm.updateBar(bar)
    #
    # def on_xmin_bar(self,bar):
    #     self.am1.updateBar(bar)
    #
    # def on_day_bar(self,bar):
    #     self.am2.updateBar(bar)

    def onStart(self):
        #self.bm = BarManager(self.onBar,1)
        self.loadTick(200)
        super().onStart()

    def onStop(self):
        super().onStop()
