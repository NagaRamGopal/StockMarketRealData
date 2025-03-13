import pandas as pd
from nsetools import Nse
from tqdm import tqdm
import yfinance as yf

class Code:
    def Data_Collection(self):
        nse = Nse()
        all_stocks = nse.get_stock_codes()
        


class main:
    c1=Code()  
    c1.Data_Collection()