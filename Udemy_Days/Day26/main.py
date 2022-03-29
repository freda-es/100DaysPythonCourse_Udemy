
#exercise list comprehesion: create a new list with the numbers that appears in all two files of text
# f1 = open("Udemy_Days\\Day26\\file1.txt", "r").readlines()
# f2 = open("Udemy_Days\\Day26\\file2.txt", "r").readlines()
# f1_list = [int(num1) for num1 in f1]
# f2_list = [int(num2) for num2 in f2]
# result  = [num for num in f1_list if num in f2_list]
# # # Write your code above 👆
# print(result)



#dictionary comprehension: create a dict with the names given in a list and attach them a random r=number form1 to 100 as scores
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleonor', 'Freddie']
# import random
# student_scores = {name_stud:random.randint(1,100) for name_stud in names}
# print(student_scores)
# passing_students = {name_stud:scores for (name_stud, scores) in student_scores.items() if scores >= 60}
# print(passing_students)


#dict comprehesion exercise #create a dict with the word and thair length fro the word in the sentence
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# list_word = sentence.split()
# result = {
#     word:len(word) for word in sentence.split()
#     }
# print(result)


#dict comprehesion exercise #create a new dict with the temp in farhenheit given in degrees
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day:((temp_c * 9/5) + 32) for (day,temp_c) in weather_c.items()}
# print(weather_f)


# iterate through a dataframe in pandas
# from doctest import OutputChecker
# from optparse import Values
# import pandas
# studen_dict = {
#     "student":["Freda", "Ledi", "Ansi", "Vesa"],
#     "scores" : [87, 99, 67, 60]
# }
# data = pandas.DataFrame(studen_dict)

## for (key, value) in data.items():#print the list of values(name student, scores)
    # print(value)
    #output
    # 0    Freda
    # 1     Ledi
    # 2     Ansi
    # 3     Vesa
    # Name: student, dtype: object
    # 0    87
    # 1    99
    # 2    67
    # 3    60
    # Name: scores, dtype: int64
    
#loop through rows in dataframe
## for (index, row) in data.iterrows():
    # print(index)
    #output
    # 0
    # 1
    # 2
    # 3
    ## print(row)# prints eatch row
    # output
    # student    Freda
    # scores        87
    # Name: 0, dtype: object
    # student    Ledi
    # scores       99
    # Name: 1, dtype: object
    # student    Ansi
    # scores       67
    # Name: 2, dtype: object
    # student    Vesa
    # scores       60
    # Name: 3, dtype: object
    ## if row.student == "Freda":
    #     print(row.scores)
    # output
    # 87
