import sys
import matplotlib
matplotlib.use('Agg')


import pandas as pd

import matplotlib.pyplot as plt


data=pd.read_csv("C:\\Users\\Captain_Levi\\Downloads\\EcommercePurchases.csv")

print(data.info())

print(len(data.columns))

print("PANDA COLUMNS: ",data.columns)

print("MEAN IS :",data['Purchase Price'].mean())

print("Median: ",data['Purchase Price'].median())

print("MODE :",data['Purchase Price'].mode())

print("MAX PP :",data['Purchase Price'].max())

print("MIN PP :",data['Purchase Price'].min())

print(data.dropna)

print(data[data.duplicated()])

print(len(data[data['Job'].str.contains('engineer',case=False)]))

print(data[data['IP Address']=="132.207.160.22"]['Email'])

data.plot(kind='scatter',x= 'Company',y= 'Job')
print(plt.show)


