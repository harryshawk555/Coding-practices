import pandas as pd
import csv

PATH = r"./Day 25 - CSV & Pandas/weather/weather_data.csv"
NEW_PATH = r"./Day 25 - CSV & Pandas/weather/scores.csv"

#data = pd.read_csv(PATH)
#print(type(data["temp"]))
#print(data["temp"])

#data_dict = data.to_dict()
#print(data_dict)
#series = data["temp"]
#series_list = series.to_list()
#avg = series.mean()
#print(series.max())

#print(data.condition)

#day = data[data.temp == data.temp.max()]
#print(day.condition)

#day = data[data.day == "Monday"]
#temp_f = int(day.temp)
#temp_c = ((temp_f-32)*5)/9
#print(f"{temp_f} degrees Farenheit\n{temp_c} degrees Celcius")

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
data.to_csv(NEW_PATH)
