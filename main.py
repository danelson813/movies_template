# Testing2/main.py
# import sqlite3

from helpers.utils import get_soup, parse_page, make_df
from helpers.database import put_into_sqlite3, get_sqlite3_to_df

url = "https://www.imdb.com/chart/top/"
soup = get_soup(url, 'data/soup.txt', False)

df = make_df(parse_page(soup))
df.to_csv('data/results.csv', index=False)
put_into_sqlite3(df, 'flix', 'flix')
new_df = get_sqlite3_to_df('flix', 'flix')
print(new_df.head())
