# with open("C:\\Users\\esoft\\Documents\\GitHub\\100DaysPythonCourse_Udemy\\Udemy_Days\\Day25\\Exercises\\weather_data.csv") as weatherdata:
#     data = weatherdata.readlines()

# How to read in csv file without pandas
# import csv
# with open("C:\\Users\\esoft\\Documents\\GitHub\\100DaysPythonCourse_Udemy\\Udemy_Days\\Day25\\Exercises\\weather_data.csv") as weatherdata:
#     data = csv.reader(weatherdata)
#     temperature = []
#     for row in data:
#         for number in row[1].split():
#             if number.isdigit():
#                 temperature.append(int(number))
# print(temperature)

#USING PANDAS
# import pandas
# data = pandas.read_csv("C:\\Users\\esoft\\Documents\\GitHub\\100DaysPythonCourse_Udemy\\Udemy_Days\\Day25\\Exercises\\weather_data.csv")


#data_dict = data.to_dict()#convert the table into a dictionary
# mean1 = data['temp'].mean()#statistical func
# max1 = data['temp'].max()

#find the row where is the max of the temperature
# max_temp = data.temp.max()
# the_row = data[data.temp == max_temp]
# print(the_row)

#find the temp in fahrenheit of mondey day
# monday = data[data.day == 'Monday']
# fahr_temp = int((monday.temp) * 1.8) +32
# print(fahr_temp)


# #create a dataframe from scratch
# data_dict = {
#     "students" : ["Ann", "Jon", "Andy"],
#     "scores" : [10, 23, 45]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("C:\\Users\\esoft\\Documents\\GitHub\\100DaysPythonCourse_Udemy\\Udemy_Days\\Day25\\Exercises\\new_data.csv")





#challenge: from the file of central park count how many red, gray, black squirrels there are and create a dataframe with that
import pandas
data = pandas.read_csv("Udemy_Days\\Day25\\Exercises\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_color = len(data[data['Primary Fur Color']== "Gray"])
black_color = len(data[data['Primary Fur Color']== "Black"])
cinn_color = len(data[data['Primary Fur Color']== "Cinnamon"])

colors_dict = {
    "Fur color" : ["Gray", "Black", "Cinnamon"],
    "count" : [gray_color, black_color, cinn_color]
    }

data_colors = pandas.DataFrame(colors_dict)
data_colors.to_csv("Udemy_Days\\Day25\\Exercises\\squirrels_colors.csv")

