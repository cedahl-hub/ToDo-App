print("Welcome to your to-do list application!")

def menu():
  print("[1] Add tasks")
  print("[2] View tasks")
  print("[3] Delete tasks")
  print("[4] Quit")

menu()

option = int(input("Please choose an option by entering its number:"))

todo_string = []

def option1():
  print()
  new_tasks = input("Please enter the task or tasks you would like to add, separated by a comma:")
  for task in new_tasks.split(","):
    todo_string.append(task.strip())
  print()
  print("Your to-do list has been updated!")

def option2():
  print()
  if not todo_string:
    print("There are no tasks to view.")
  else:
    print(f"Here's your current to-do list: {todo_string}")

def option3():
  print()
  if not todo_string:
    print("Your to-do list is empty, so there are no tasks to delete.")
  else:
    print(f"Here's your current to-do list:")
    for index, item in enumerate(todo_string, start=1):
      print(f"[{index}] {item}")
    try:
      user_choice = int(input("Please enter the number of the task you'd like to delete:"))
      if 1 <= user_choice <= len(todo_string):
        todo_string.pop(user_choice - 1)
        print()
        print("The task has been deleted!")
      else:
        print()
        print("Sorry, that's not a valid option. You must enter a number from the list.")
    except ValueError:
      print("Invalid input. You must enter a number.")

while option != 4:
  if option == 1:
    option1()
  elif option == 2:
    option2()
  elif option == 3:
    option3()
  else:
    print()
    print("Sorry, that's not a menu option. Please enter a number from the menu.")

  print()
  menu()
  option = int(input("Please choose an option by entering its number:"))
  
print("You've quit the application.")