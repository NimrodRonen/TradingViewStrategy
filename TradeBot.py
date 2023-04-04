import ibapi as ap
from ibapi.client import EClient 
from ibapi.wrapper import EWrapper 

#class for interactive Brocker Connection
class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)

#Bot Logic
class Bot:
    ib = None
    def __init__(self):
        ib = IBApi()
        ib.connect("109.186.151.94", 7496, 1)
        ib.run()

#start Bot
bot = Bot()