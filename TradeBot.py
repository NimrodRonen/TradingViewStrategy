import ibapi
from ibapi.client import EClient 
from ibapi.wrapper import EWrapper 
from ibapi.contract import Contract
from ibapi.order import *
import time
import threading
#class for interactive Brocker Connection
class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
    
    #listen to real time bars
    def realtimeBar(self, reqId, time, open_, high, low, close, volume, wap, count):
        super().realtimeBar(reqId, time, open_, high, low, close, volume, wap, count)
        try:
            bot.on_bar_update(reqId, time, open_, high, low, close, volume, wap, count)
        except Exception as e:
            print(e)
    
    def error(self, id, errorCode, errorMsg):
        print(errorCode)
        print(errorMsg)


#Bot Logic
class Bot:
    ib = None
    def __init__(self):
        #connect to IB on __init__ (constractor in c# and java therms)
        self.ib = IBApi()
        self.ib.connect("127.0.0.1", 7496, 1)

        #saperate to threads
        ib_thread = threading.Thread(target=self.run_loop, daemon=True)
        ib_thread.start()

        time.sleep(1) #connection take some time...

        #get symbol info
        symbol = input("Enter the symbol you want to trade in:")
        contract = Contract() #use to stream a real-time or historycal object
        contract.symbol = symbol.upper()
        contract.SecType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"

        self.ib.reqRealTimeBars(0, contract, 5,"TRADES", 1, [])

    #listen to socket in saperate thread
    def run_loop(self):
        self.ib.run()

    def on_bar_update(self, reqId, time, open_, high, low, close, volume, wap, count):
        print(close)


#start Bot
bot = Bot()