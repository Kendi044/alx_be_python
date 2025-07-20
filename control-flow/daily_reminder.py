task = input("Enter your task:").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder_prefix = "Reminder"
additional_phrase = ""
final_reminder = ""

match priority:
    case 'high':
        reminder_prefix = "Reminder:"
        final_reminder = f"'{task}' is a high priority task"
    case 'medium':
        reminder_prefix = "Reminder:"
        final_reminder = f"'{task}' is a medium priority task"
    case 'low':
        reminder_prefix = "Note:"
        final_reminder = f"'{task}' is a low priority task"
    case _: 
        print("Invalid priority entered. Please choose 'high', 'medium', or 'low'.")
        
        exit() 

if time_bound == 'yes':
    additional_phrase = " that requires immediate attention today!"
elif priority == 'low' and time_bound == 'no':
    additional_phrase = ". Consider completing it when you have free time."

print(f"{reminder_prefix} {final_reminder}{additional_phrase}")


        
