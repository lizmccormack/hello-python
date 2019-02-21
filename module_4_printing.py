# Part 1 ask the user to enter 3 places they would like to travel
travel = input("Where would you like to travel. Name one place.")
travel_2 = input("What is another place you would like to travel. Name one place.")
travel_3 = input("What is one more place you'd like to travel to. Name one place.")

# add the locations they would liek to travel to a list
travel_list = []
travel_list.append(travel)
travel_list.append(travel_2)
travel_list.append(travel_3)
# sort the list
travel_list.sort()
# print a string with a list of the places they would like to travel
print (("Here is a list of the places you would like to go: \n %s \n %s \n %s") % (travel, travel_2, travel_3))

# Part 2 create a program that prints the first and third letters in a list of strings
fun_words = ["elephant", "balloon", "macchiato", "angostura"]
first_letters = []
third_letters = []
# print all first letters
for word in fun_words:
    adding_letters = word[0]
    first_letters.append(adding_letters)

print (first_letters)
# print all third letters
for word in fun_words:
    adding_letters = word[2]
    third_letters.append(adding_letters)

print(third_letters)

# Part 3 find and print the lengths of the lists
websites = ["facebook", "twitter", "buzzfeed"]
fruits = ["apple", "banana", "mango", "berry"]
names = ["Bob", "Alice", "Henry", "Rick", "Carl"]

websites_len = len(websites)
fruits_len = len(fruits)
names_len = len(names)

lengths = []
lengths.append(websites_len)
lengths.append(fruits_len)
lengths.append(names_len)

print (lengths)

# Part 4 
for i in range(0, 26, 5):
    print (i)
