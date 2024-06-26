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
