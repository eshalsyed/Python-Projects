# To-do List 

to_do_list = []

print("\nWELCOME TO YOUR DIGITAL TO DO LIST!🔖✍🏽")

def add_task():
    task = input("Enter task: ")
    store =[task,["Not Completed"]]
    to_do_list.append(store)
    print("Task added succesfully!")

def view_task():
    if not to_do_list:
        print("To-do List is Empty... ")
    else:
        print(f"Here is your to do list:\n")
        for objects in to_do_list:
            print(f"{objects[0]} : {objects[1]}")

def mark_done():
    if not to_do_list:
        print("To-do list is Empty. ")
        return
    
    print(f"\n\nHere is you To-do list:\n")
    for index, task in enumerate(to_do_list, start=1):
        print(f"{index}. {task[0]} : {task[1][0]}")

    number = int(input("What task would u like to mark as done?\n Please enter the number: ")) 

    if 1 <= number <= len(to_do_list):
        to_do_list[number - 1][1][0] = "Completed"
        print(f"Task '{to_do_list[number - 1][0]}' is marked as completed!")
    else:
        print("Invalid task number. Please try again.")




def main():
    while True:
        print("1.Add Task")
        print("2.View task list")
        print("3.Mark tasks as completed")
        print("4.Exit\n")
        ask = input("Enter options (1-4):")
        if ask == "1":
            add_task()
        elif ask == "2":
            view_task()
        elif ask == "3":
            mark_done()
        elif ask == "4":
            print("Bye Bye!")
            break
        else: 
            print("Invalid input")
main()
