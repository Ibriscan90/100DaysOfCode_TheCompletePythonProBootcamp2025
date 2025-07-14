# import csv
#
# import numpy
# import pandas
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # #get average temp
# # print(data["temp"].mean())
# # #get max value of the list
# # print(data["temp"].max())
# # #get data in columns
# # print(data["condition"])
# #print(data.condition)
#
# #get data from rows
# #print(data[data.day == "Monday"])
# # print(data[data.temp == data["temp"].max()])
# #
# # monday = data[data.day == "Monday"]
# # #print(monday.condition)
# # monday_temp = monday.temp[0]
# # mondaytemp_fahrenheit = monday_temp *9/5 + 32
# # print(mondaytemp_fahrenheit)
#
# #create a DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76,56,65]
# }
#
# new_table = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


#Squirrel data analysis
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250713.csv")
grey_data_count = len(data[data["Primary Fur Color"] == "Gray"])
red_data_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_data_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_data_count)
print(red_data_count)
print(black_data_count)

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_data_count, red_data_count, black_data_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")