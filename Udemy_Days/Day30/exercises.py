#dealing with errors


# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")#if the file does not exist we create it
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")#key error message, the dict doesnt have the key
# else:#if anything of the errors happens than continue
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")

#BMI Example

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.") #here we make our own error to control the height tha the user will enter

# bmi = weight / height ** 2
# print(bmi)



#TODO: Catch the exception and make sure the code runs without crashing.
# fruits = ["Apple", "Pear", "Orange"]
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")

# make_pie(4)


# facebook_posts = [
#     {'Likes': 21, 'Comments': 2}, 
#     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#     {'Comments': 4, 'Shares': 2}, 
#     {'Comments': 1, 'Shares': 1}, 
#     {'Likes': 19, 'Comments': 3}
# ]
# total_likes = 0
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass
# print(total_likes)