programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# print(programming_dictionary["Bug"])

programming_dictionary["virus"] = "A computer that software ment to slow the performance of CPU"
print(programming_dictionary)

# for key in programming_dictionary:
#     print(programming_dictionary[key])

colours = {"apple": "green", "pear": "green", "banana": "yellow"}


colours["apple"] = "red"
print(colours)


# Empty Dictionary
Dictionary =  {}

Dictionary =  {"key": "value", "key": "value"}

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

grades = {"A", "B", "C", "D", "E"}
for key in student_scores:
    if student_scores[key] >= 90:
        student_scores[key] = "A+"
    elif student_scores[key] < 90 and student_scores[key] >= 80:

        student_scores[key] = "A-"

    elif student_scores[key] < 80 and student_scores[key] >= 70:

        student_scores[key] = "B"
    elif student_scores[key] < 70 and student_scores[key] >= 60:

        student_scores[key] = "C"
print(student_scores)
# student_grades =
