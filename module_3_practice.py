# 1
adjective = "absolutely fabulous"
adjective2 = "supercalifragilisticexpialidocious"
noun = "aardvarks"
noun2 = "billygoats"
verb = "lollygaggings"
verb2 = "jogging"
# 2
if len(adjective) > 9:
    print ("long string")
else: print ("not a long string")

if len(adjective2) > 9:
    print ("long string")
else: print ("not a long string")

if len(noun) > 9:
    print ("long string")
else: print ("not a long string")

if len(noun2) > 9:
    print ("long string")
else: print ("not a long string")

if len(verb) > 9:
    print ("long string")
else: print ("not a long string")

if len(verb2) > 9:
    print ("long string")
else: print ("not a long string")
# 3
my_input = input("what did you do for exercise today?")
print (len(my_input))
# 4
answer = input("What is 2 + 2 ?")
answer_as_integer = int(answer)

if answer_as_integer == 4:
    print ("You are correct!")
elif answer_as_integer > 4:
    print ("too high...")
else:
    print ("too low...")
# 5
if verb == verb2:
    print ("They are equal!")
else:
    print (verb)
    print (verb2)
    print ("They are not the same.")
#6
rating = input("On a 1-10 scale, how would you rate the Wizard of Oz?")
rating_as_integer = int(rating)

if rating_as_integer < 5:
    print ("Wow, you hated it!")
elif 5 < rating_as_integer < 7:
    print ("You are meh about this movie.")
elif rating_as_integer > 7:
    print ("You loved it. There's no place like home.")
else:
    "Rate the movie!"
    
