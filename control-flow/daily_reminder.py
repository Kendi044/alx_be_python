
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

task_description = ""

match priority:
    case 'high':
        task_description = f"'{task}' is a high priority task"
    case 'medium':
        task_description = f"'{task}' is a medium priority task"
    case 'low':
        task_description = f"'{task}' is a low priority task"
    case _:
        print("Invalid priority entered. Please choose 'high', 'medium', or 'low'.")
        exit() 


if time_bound == 'yes':
    print(f"Reminder: {task_description} that requires immediate attention today!")
elif priority == 'low' and time_bound == 'no':
    print(f"Note: {task_description}. Consider completing it when you have free time.")
else:
    print(f"Reminder: {task_description}")



        
