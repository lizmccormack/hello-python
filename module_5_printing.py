# Part 1: ask the user three quiz questions from a list of questions with a for loop
quiz_questions = ['what are three datatypes? ', 'what are lists? ', 'what is the difference between print and return? ']

for question in quiz_questions:
    response = input(question)
    print (response)


# Part 2: create a todo list program with a while loop that ends when the user enters quit 
todo_list = ["Do laundry"]

command = input("would you like to A) add a todo list item or B) quit? ")
while command != 'quit':
    if command == 'add':
        command = input('what would you like to add? ')
        todo_list.append(command)
        command = input('what would you like to do next? Enter add or quit. ')

print (todo_list)
