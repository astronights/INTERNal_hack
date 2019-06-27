def scrape(stock, start_date=[2019,1,1], end_date=[2019, 6, 25]):
    from yahoo_historical import Fetcher
    data = Fetcher(stock, start_date, end_date)
    stock_data = data.getHistorical()
    stock_data.to_csv(stock +".csv")

def plot(stock, col):
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn.linear_model import LinearRegression
    data = pd.read_csv(stock + ".csv")
    # data = data.set_index("Date")
    pos = data.index[data[col] == 1]
    neg = data.index[data[col] == 0]
    plt.figure(figsize=(20,10))
    ax = data.set_index(data["Date"])["Close"].plot()
    for x in pos:
        ax.axvline(x, color='green',linewidth=10, alpha=0.3)
    for x in neg:
         ax.axvline(x, color='red', linewidth=10,alpha=0.3)
    plt.savefig(stock+'.png')

plot("BILI", "Score")
# scrape("JPM")
# import pandas as pd
# data_to_csv = pd.read_csv("JPM.csv", usecols=["Date", "Open","Close", "Classes"])
# subset = data_to_csv[['Date', 'Open', 'Close', 'Classes']]
# tuples = [tuple(x) for x in subset.values]
# tuples
