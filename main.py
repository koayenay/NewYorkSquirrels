# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# using python csv reader
# with open("weather-data.csv.csv") as file:
#     data = file.readlines()
#     print(data)

#Lets use CSV library

# import csv
# with open("weather-data.csv.csv") as file:
#     data = csv.reader(file)
#     print(data) # this will print the object <_csv.reader object at 0x0000028F449E7820>
#     temp = []
#     # to print the data in a list format
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#         # print(row)
#     print(temp)


# Better way: PANDAS

import pandas

# data = pandas.read_csv("weather-data.csv.csv")
# print(type(data))
#
# print(data["temp"]) # this will print the temp column
#
# data_dict = data.to_dict()
#
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# # average temp
# print(data["temp"].mean())
#
# # max temp
# print(data["temp"].max())

# get data in columns
# print(data["condition"])
#alternative way
# print(data.condition)
#
# # data Data in row
# # print
# print(data[data.day == "Monday"])
#
# # Max temp row
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# # monday temp -> fahrenheit
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp*9/5+32
# print(monday_temp_F)
#
#
# student_dict = {
#     "student": ["Arfan","Roaf","Rayhan"],
#     "score": [100,99,98]
# }
#
# data=  pandas.DataFrame(student_dict)
# data.to_csv("new_data.csv")


#Squirrel data analysis

data = pandas.read_csv("squirrel_data.csv")
# print(data)

#Lets get the count of each color
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squrrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels)

#Lets create a dictionary
data_dict = {
    "Fur Color": ["Gray","Red","Black"],
    "Count": [gray_squirrels,red_squrrels,black_squirrels]
}

#We need to convert the dictionary to a Panda Dataframe
data_dict= pandas.DataFrame(data_dict)
data_dict.to_csv("squirrel_count.csv")