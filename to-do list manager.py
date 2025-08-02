# this is a to-do list manager
def to_do_list():
    alltasks=[]
    while True:
        print("1.add tasks\n2.view tasks\n3.remove tasks\n4.Exit")
        choice=input("Enter you preference:")

        if(choice=='1'):
            task=input("Enter the task:")
            alltasks.append(task)
            print("Done")
        elif(choice=='2'):
            print("Your tasks are", alltasks)      
        elif(choice=='3'):
            task=input("enter the task to remove:")
            if(task in alltasks):
                alltasks.remove(task)
                print("Task is removed")
                print("updated task are:", alltasks)
            else:
                return ValueError
        elif(choice=='4'):
            break
        else:
            print("Wrong choice")

to_do_list()