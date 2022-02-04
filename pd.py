import pandas as pd
import csv

with open('data.csv', 'r') as csv_file:
    data = pd.read_csv['data.csv']
    print(data)
