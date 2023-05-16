class toDo_list():
    def __init__(self, description= ""):
        self.description=description
        self.completed=False
    
    def completed (self):
        self.completed= True
class ToDoList():
    def __init__(self,):
        self.tasks=[]

# method to add new task 
    def add_task(self, task):
        self.tasks.append(task)

#method to delete a task 
    def delete_task(self, task):
        self.tasks.remove(task)

    def complete_task(self,task):
        task.completed= True

#method to dsplay all tasks
    def display_task(self):
        for i, task in enumerate(self.tasks, 1):
            print(f" {i}. {task.description} {'(completed)' if task.completed else ' '}")

if __name__ == '__main__':
    
    taskList=ToDoList()

    while True:
        
#Outline instructions for user
        print(" Enter 1 to add new task \n") 
        print(" Enter 2 to delete task \n")
        print(" Enter 3 to mark completed task \n")
        print(" Enter 4 display all tasks \n")
        print(" Enter 5 to exit \n ") 
        

        user_input= input(" Enter your choice: ")

# Ask user to enter name of new task
        if user_input == "1":
            description= input("Enter new task name: ")
            new_task=toDo_list(description)
            taskList.add_task(new_task)
            print ("Task added succesfully! \n")

#Ask user to delete task, of his/her choice
        elif user_input== "2":
            task_index= int(input("Enter task index to remove: "))
            try:
                index= int(task_index) -1
                task=taskList.tasks[task_index]
                taskList.delete_task(task)
                print ("Task removal successful")
            except (IndexError, ValueError):
                print ("Task index not found [X]")

#To mark completed task 
        elif user_input== "3":
            task_index= int(input("Enter task index of completed task: "))
            try:
                task=taskList.tasks[task_index -1]
                taskList.complete_task(task)
                print ("Task marked as completed ")
            except IndexError:
                print ("Task index is invalid")

# To view list
        elif user_input== "4":
            print("Tasks: ")
            taskList.display_task()
            

#To exit application
        elif user_input== "5":
            print("Closing App...")
            break

        else:
            print("Invalid entry, please try again!")
# 

