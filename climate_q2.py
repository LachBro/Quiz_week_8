import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('climate.csv') #load the datafile climate.csv using pandas

#get data from data frame
years = df['Year']
co2 = df['CO2']
temp = df['Temperature']

#create subplots
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

