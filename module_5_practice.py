# 1 while loop that stops when counter is greater than 8
counter = 1

while counter < 8:
    print (counter)
    counter = counter + 1

# 2 for loop that prints the numbers 0- 20
for num in range(21):
    print (num)

# 3 for loop that prints tne numbers 0-10, but skips 3 and 5
for num in range(11):
    if num != 3:
        if num != 5:
            print (num)
# 4 while loops taht prints the numbers backwards from 100 to 0
counter = 100

while counter > 0:
    print (counter)
    counter = counter - 1

# 5 for loop that prints all of the numbers from 1-100 divisible by 11
for num in range(1, 101):
    if num % 11 == 0:
        print (num)


# 6 for loop that prints the numbers from 0-80
for num in range(80):
    print (num)

# 7 for loop that prints the colors in the list
colors = ["black", "orange", "purple"]
for color in colors:
    print (color)

# 8 for loop that prints the first letter of the colors in the list
for color in colors:
    print (color[0])

# 9 for loop that prints the numbers 7-12
for n in range (7,13):
    print (n)

# 10 for loop that prints that even numbers from 8 - 12 
for n in range (8,13):
    if n % 2 == 0:
        print (n)
