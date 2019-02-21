# create a dictionary of cake ingredients
cake_ingredients = {'butter': 1, 'shortening': 0.5, 'sugar': 3, \
'egg substitutes': 1.5, 'flour': 3, 'milk': 1, 'salt': 0.01,\
'baking powder': 0.01}

# write a for loop that doubles the cake ingredients and prints the new amounts
print ("To make two cakes, you need: ")
for ing in cake_ingredients:
    doubled = cake_ingredients[ing]*2
    print(("%s cups of %s") % (doubled, ing))

# ask the user if they have any questions
question = input("What ingredient do you want to know about?")
if question in cake_ingredients:
    print (("One cake has %s cups of %s") % (cake_ingredients[question], question))
else:
    print (("This cake does not contain %s.") % question)
