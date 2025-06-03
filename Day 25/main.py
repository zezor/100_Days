# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)


# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)


import pandas as pd

# data = pd.read_csv("weather_data.csv")
# # print(data["temp"])
# data_dict = data.to_dict()
# # print(data_dict)
#
# # temp_list = data["temp"].to_list()
# # average = sum(temp_list) / len(temp_list)
# # print(average)
# #
# # print(data["temp"].mean())
# #
# # print(data["temp"].max())
# #
# # # Get data in column
# # print(data["condition"])
# # print(data.condition)
#
# print(data[data.day == "Monday"])
# # print(data.day == "Monday")
# #print(f"Min is {data["temp"].min}")
#
# print(data[data.temp == data.temp.max()])


# create dataframe from scratch
#
# data_dict = {
#     "students": ["Emma", "Gloria", "Maria"],
#     "score":[25, 87, 84]
# }
#
# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv("new_file.csv")


data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_Squirrel = data[data["Primary Fur Color"] == "Gray"]
print(gray_Squirrel)
