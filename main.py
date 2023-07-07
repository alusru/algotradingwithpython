import yfinance as yt
import pandas as pd
import matplotlib.pyplot as plt


def download_data():
    ticker = ["AAPL", "SPY", "TSLA"]
    stocks = yt.download(ticker, start="2009-01-01", end="2023-01-01")
    return stocks


def read_stocks_csv(file_name: str):
    stocks = pd.read_csv(file_name, header=[0, 1], index_col=[0], parse_dates=[0])

    print(stocks)

    # # convert multi index to flat index (tuple)
    # stocks.columns = stocks.columns.to_flat_index() remove for now as its converting from multi to flat

    # Generate descriptive statistics.
    print(stocks.describe())

    # Access a group of rows and columns by label(s) or a boolean array.
    # .loc[] is primarily label based, but may also be used with a boolean array.
    print(stocks.loc[:, "Close"])

    close = stocks.loc[:, "Close"]

    plot_graph(close)

    normalize_data(close)


def normalize_data(close):
    normalize = close.div(close.iloc[0]).mul(100)

    plot_graph(normalize)


def plot_graph(close):
    plt.style.use("seaborn-v0_8")

    close.plot(figsize=(15, 8), fontsize=12)

    plt.legend(fontsize=12)

    # https://stackoverflow.com/questions/24886625/pycharm-does-not-show-plot
    plt.show()


def save_stocks_csv(data, file_name: str):
    data.to_csv(f"{file_name}")

    print(f"{file_name} has been saved successfully")


if __name__ == '__main__':
    filename = "stocks.csv"

    data = download_data()

    save_stocks_csv(data, filename)

    read_stocks_csv(filename)
