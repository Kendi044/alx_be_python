
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

final_reminder = ""
priority_message = ""

match priority:
    case 'high':
        priority_message = f"'{task}' is a high priority task"
    case 'medium':
        priority_message = f"'{task}' is a medium priority task"
    case 'low':
        priority_message = f"'{task}' is a low priority task"
    case _:
        print("Invalid priority entered. Please choose 'high', 'medium', or 'low'.")
        exit() 


if time_bound == 'yes':
    final_reminder = f"Reminder: {priority_message} that requires immediate attention today!"
elif priority == 'low' and time_bound == 'no':
    final_reminder = f"Note: {priority_message}. Consider completing it when you have free time."
else:
    final_reminder = f"Reminder: {priority_message}"

print(final_reminder)


        
