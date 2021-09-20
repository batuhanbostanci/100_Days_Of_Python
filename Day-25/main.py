
import pandas as pd

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#
#
#     print(temperatures)


# data = pd.read_csv("weather_data.csv")
# data_dict = data.to_dict()

# print(data_dict)
#
# temp_list = data["temp"].to_list()
# avg_temp_list = sum(temp_list) / len(temp_list)
# print(avg_temp_list)
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# max_temp = max(data["temp"])
# print(data[data.day == "Monday"])
#
# print(data[data.temp == max_temp])
#
# monday = data[data.day == "Monday"]
# print(type(monday))

# data_dict ={
#     "students": ["Amy", "James", "Angela"],
#     "scores": [60, 34, 63]
# }
#
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)


data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_colors = len(data[data["Primary Fur Color"] == "Gray"])
red_colors = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_colors = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Counts": [gray_colors, red_colors, black_colors]
}

data = pd.DataFrame(data_dict)
data.to_csv("Central Park New Data.csv")
