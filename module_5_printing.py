# Part 1
quiz_questions = ['what are three datatypes?', 'what are lists?', 'what is the difference between print and return']

for question in quiz_questions:
    input(question)
    print (question) 


# Part 2
todo_list = ["Do laundry"]

command = input("would you like to A) add a todo list item or B) quit ")
while todo_list:
    if command == 'add':
        command = input('what would you like to add? ')
        todo_list.append(command)
    elif command == 'quit':
        break
    else:
        print('please enter add or quit')

print (todo_list)
