
cats = input("Do you like cats? Answer Y or N: ")

if cats == "N":
    not_cats = input("What is your favortie animal? ")
else:
    print ("Cats are cool!")

chocolate = input("Do you like chocolate? Answer Y or N: ")

if chocolate == "N":
    not_chocolate = input("What is your favorite dessert? ")
else:
    print ("YUM!")

coffee = input("Do you drink coffee? Answer Y or N: ")

if coffee == "Y":
    how_do_you_like_it = input("Do you put sugar in it? ")
else:
    what_do_you_drink = input("What is your favorite morning drink? ")

cali = input("Do you live in California? Answer Y or N: ")

if cali == 'Y':
    city = input("What city do you live in? ")
else:
    state = input("What state do you live in? ")

jokes = input ("Do you enjoy jokes? Answer Y or N: ")

if jokes == "Y":
    joke = input("What kinds of melon can't marry? " )
    print ("Catelopes")
else:
    no_jokes = input("Why? ")

print ("Here are the user's answers!")
try:
    not_cats
except NameError:
    print ("User did not answer this question")
else:
    print (not_cats)

try:
  not_chocolate
except NameError:
    print ("User did not answer this question")
else:
    print (not_chocolate)

try:
   how_do_you_like_it
except NameError:
    print ("User did not answer this question")
else:
    print (how_do_you_like_it)

try:
   what_do_you_drink
except NameError:
    print ("User did not answer this question")
else:
    print (what_do_you_drink)

try:
   how_do_you_like_it
except NameError:
    print ("User did not answer this question")
else:
    print (how_do_you_like_it)

try:
   cali
except NameError:
    print ("User did not answer this question")
else:
    print (cali)

try:
   state
except NameError:
    print ("User did not answer this question")
else:
    print (state)

try:
   jokes
except NameError:
    print ("User did not answer this question")
else:
    print (jokes)

try:
   no_jokes
except NameError:
    print ("User did not answer this question")
else:
    print (no_jokes)
