capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}
#
# #Nested List in a dictionary
#
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }
# print(travel_log["France"][1])
#
# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])


travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visit": 22
    },
    "Germany": {
       "cities_visited": ["Stuttgart", "Berlin", "Hamburg"],
        "total_visit": 22
    }

}
print(travel_log["Germany"]["cities_visited"][0])


starting_dictionary = {
    "a": 9,
    "b": 8,
}

starting_dictionary["c"] = 7

print(starting_dictionary)