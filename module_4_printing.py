# Part 1
travel = input("Where would you like to travel. Name one place.")
travel_2 = input("What is another place you would like to travel. Name one place.")
travel_3 = input("What is one more place you'd like to travel to. Name one place.")

travel_list = []
travel_list.append(travel)
travel_list.append(travel_2)
travel_list.append(travel_3)

travel_list.sort()

print (("Here is a list of the places you would like to go: \n %s \n %s \n %s") % (travel, travel_2, travel_3))

# Part 2
fun_words = ["elephant", "balloon", "macchiato", "angostura"]
first_letters = []
third_letters = []

for word in fun_words:
    adding_letters = word[0]
    first_letters.append(adding_letters)

print (first_letters)

for word in fun_words:
    adding_letters = word[2]
    third_letters.append(adding_letters)

print(third_letters)

# Part 3
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
