import pandas as pd


def read_books():
    books = pd.read_csv("books.csv", header=None)
    books.columns = ["id", "title", "price"]
    return books.to_dict(orient='records')