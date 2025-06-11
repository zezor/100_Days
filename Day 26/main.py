numbers = [1, 2, 3]
new_numbers = [(n + 1) for n in numbers]
print(new_numbers)

#LIST COMPREHENSION
# new_numbers = [(n + 1) for n in numbers]
# print(new_numbers)
# [2, 3, 4]
# range_1 = range(1, 5)
# new_numb = [num * 2 for num in range_1]
# print(new_numb)
# [2, 4, 6, 8]
# names = ["Glorieta", "Ben", "Nana", "Emmanuel", "Nyamekye", "Glory"  ]
# names
# ['Glorieta', 'Ben', 'Nana', 'Emmanuel', 'Nyamekye', 'Glory']
# short_names = [name for name in names if len(name) < 5]
# short_names
# ['Ben', 'Nana']

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(numbers)
print(result)


#DICTIONARY COMPREHENSION

#new_dict = {new_key: new_value for item in list}
#new_dict = {new_key: new_value for (key, value) in dict.items()}
#new_dict = {new_key: new_value for (key, value) in dict.items() if test}