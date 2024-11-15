import pandas as pd
PATH = r"./Day 25 - CSV & Pandas/squirrel_census/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241114.csv"
OUT_PATH = r"./Day 25 - CSV & Pandas/squirrel_census/fur_colors.csv"


data = pd.read_csv(PATH)
furs = data["Primary Fur Color"]
fur = furs.to_list()
gray = fur.count("Gray")
cinnamon = fur.count("Cinnamon")
black = fur.count("Black")
data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [gray, cinnamon, black]
}

out = pd.DataFrame(data_dict)
print(out)
out.to_csv(OUT_PATH)