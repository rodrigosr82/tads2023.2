import yfinance as yf
import pandas as pd

def download_data (ticker:str) -> pd.DataFrame:
    
    """Download data from yahoo fiances

    Args:
        ticker (str): the ticker of financial asset.

    Returns:
        pd.DataFrame: datafram, restrived from yahoo Finances.
    """

    data = yf.download(ticker)
    
    return data


