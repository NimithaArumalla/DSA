import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("C:/Users/Gopi/Documents/nimmy/pokemon_data.csv",header=0,sep=",")
data.plot(x='HP',y='Attack')
plt.show()
print(data.head())