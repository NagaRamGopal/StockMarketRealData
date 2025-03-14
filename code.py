import pandas as pd
import yfinance as yf
from tqdm import tqdm
from datetime import datetime, timedelta
import pytz  # Add this for timezone handling

class Code:
    def Data_Collection(self):
        # Sample list of NSE symbols (replace with complete list)
        nse_stocks = ['RELIANCE', 'TCS', 'HDFCBANK', 'INFY', 'HINDUNILVR']
        
        # Prepare data storage
        stock_data = {
            'Name': [],
            'Price_Yesterday': [],
            'Price_Today': [],
            'Change_Week_Percent': [],
            'Change_Month_Percent': []
        }
        
        # Set timezone to match yfinance data (Asia/Kolkata for NSE)
        tz = pytz.timezone('Asia/Kolkata')
        today = datetime.now(tz)
        yesterday = today - timedelta(days=1)
        week_ago = today - timedelta(days=7)
        month_ago = today - timedelta(days=30)
        
        # Process each stock
        for symbol in tqdm(nse_stocks, desc="Fetching stock data"):
            try:
                ticker = f"{symbol}.NS"
                stock = yf.Ticker(ticker)
                hist = stock.history(period="1mo")
                
                if not hist.empty and len(hist) >= 2:
                    # Use iloc for positional access
                    price_today = hist['Close'].iloc[-1]
                    price_yesterday = hist['Close'].iloc[-2]
                    
                    # Ensure index is timezone-aware for comparison
                    week_data = hist[hist.index >= week_ago]
                    if not week_data.empty:
                        week_start = week_data['Close'].iloc[0]
                        week_change = ((price_today - week_start) / week_start) * 100
                    else:
                        week_change = None
                        
                    month_start = hist['Close'].iloc[0]
                    month_change = ((price_today - month_start) / month_start) * 100
                    
                    stock_data['Name'].append(symbol)
                    stock_data['Price_Yesterday'].append(price_yesterday)
                    stock_data['Price_Today'].append(price_today)
                    stock_data['Change_Week_Percent'].append(week_change)
                    stock_data['Change_Month_Percent'].append(month_change)
                    
            except Exception as e:
                print(f"Error processing {symbol}: {str(e)}")
                continue
        
        # Create DataFrame
        df = pd.DataFrame(stock_data)
        
        # Define numeric columns
        numeric_columns = ['Price_Yesterday', 'Price_Today', 
                         'Change_Week_Percent', 'Change_Month_Percent']
        
        # Round numeric columns to 2 decimal places
        df[numeric_columns] = df[numeric_columns].round(2)
        
        # Save to CSV
        df.to_csv('nse_stock_data.csv', index=False)
        return df

class main:
    def __init__(self):
        self.c1 = Code()
        
    def run(self):
        df = self.c1.Data_Collection()
        print("\nFirst few rows of the data:")
        print(df.head())
        return df

if __name__ == "__main__":
    m = main()
    stock_df = m.run()