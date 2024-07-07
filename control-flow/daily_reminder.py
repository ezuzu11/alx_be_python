
task= input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound= input("Is it time-bound? (yes/no): ").lower()
reminder = f" {task} (Priority: {priority.capitalize()})"
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

        
print("Reminder: ", reminder)

