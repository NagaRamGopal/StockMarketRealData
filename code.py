import pandas as pd
from nsetools import Nse
from tqdm import tqdm

class Code:


    def Data_Collection(self):
        nse = Nse()
        all_stocks = nse.get_stock_codes()
        quote = nse.get_quote('INFY')  # Fetch details for Infosys (INFY)
        print(quote)


class main:
    c1=Code()  
    c1.Data_Collection()