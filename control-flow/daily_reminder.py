"""
task= input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bond= input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bond == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            pass
    case "medium":
        if time_bond == "no":
           print(f"Note: '{task}' is a medium priority task. Consider completing it when you have free time.")
        else:
            pass 
    case "low":
        if time_bond == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            pass
    case _:
        print("Invalid input!")

"""
# daily_reminder.py

# Prompt for a single task
task = input("Enter your task for the day: ")

# Prompt for the task's priority
priority = input("Enter the task's priority (high, medium, low): ").strip().lower()

# Prompt if the task is time-bound
time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()

# Provide a customized reminder based on the priority and time sensitivity
reminder = f"{task} (Priority: {priority.capitalize()})"

# Use a Match Case statement to handle different priorities
match priority:
    case "high":
        reminder += " - This is a high priority task."
        if time_bound == "yes":
            reminder += " It requires immediate attention today!"
    case "medium":
        reminder += " - This is a medium priority task."
        if time_bound == "yes":
            reminder += " It requires immediate attention today!"
    case "low":
        reminder += " - This is a low priority task."
        if time_bound == "yes":
            reminder += " It requires immediate attention today!"
    case _:
        reminder = "Invalid priority level provided."

# Print the reminder
print("Reminder: ",reminder)


