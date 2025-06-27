# Errors and Exceptions

#keyError

#IndexError

#TypeError

#FileNotFound

#try something that might cause an exception
#except: Do this if there was an exception
#else: Do this if there were no exceptions
#finally Do this no matter what happens
#
# try:
#     file = open("a_file.txt")
#     a_dict = { "key": "value"}
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message: #catching exception and get hold of error message
#     print("The key does not exist")
#     print(f"The key {error_message } does not exist")
#
# else:
#     content  = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")


# Generating/raising your own exception
# height = float(input("Height: "))
# weight = float(input("weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")
#
# bmi = weight / height ** 2
# print(bmi)
#
#
# fruits = ["Apple", "Pear", "Orange"]
#
#
# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(4)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            pass

    return total_likes


count_likes(facebook_posts)
