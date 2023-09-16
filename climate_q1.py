import matplotlib.pyplot as plt
import sqlite3

connection = sqlite3.connect('climate.db')
cursor = connection.cursor()

#values to be inserted
insert_data = """
    INSERT INTO ClimateData (Year, CO2, Teamperature)
    VALUES
    (1950, 250, 14.1),
    (1960, 265, 15.5),
    (1970, 272, 16.3),
    (1980, 260, 18.1),
    (1990, 300, 17.3),
    (2000, 320, 19.1),
    (2010, 389, 20.2)
"""

#execute the query to insert values
cursor.execute(insert_data)

#commit changes to climate.db database
connection.commit()

# retrieve data from climate.db database
query = "SELECT Year, CO2, Temperature FROM ClimateData"
cursor.execute(query)
data = cursor.fetchall()

# this will seperate the lists of data into rows
years = [row[0] for row in data]
co2 = [row[1] for row in data]
temp = [row[2] for row in data]

# create subplots
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 

plt.savefig("co2_temp_1.png")
plt.show()

connection.close()
