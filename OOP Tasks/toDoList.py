#Create an empty list 
toDo_list= []
while True:
#Outline instructions for user
    instructions= "\n Enter 1 to add new task \n Enter 2 to delete task \n Enter 3 to view task \n Enter 4 to exit the App" 
    print(instructions)

    user_input= input(" Enter your choice: ")

# Ask user to enter name of new task
    if user_input == "1":
        task= input("Enter new task name: ")
        toDo_list.append(task)
        print ("Task added succesfully!")

#Ask user to delete task, of his/her choice
    elif user_input== "2":
        task= input("Enter name of task to be deleted")
        if task in toDo_list:
            toDo_list.remove(task)
            print ("Task removal successful")
        else:
            print ("Task nmae not found [X]")

# To view list
    elif user_input== "3":
        print("toDo_list: ")
        for task in toDo_list:
            print (task)

#To exit application
    elif user_input== "4":
        print("Closing App...")
        break

    else:
        print("Invalid entry, please try again!")








