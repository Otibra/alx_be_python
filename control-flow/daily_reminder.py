# Ask the user to input a task description and save it into a variable
task = input("Enter the task you need to complete: ")

# Ask for the task’s priority
priority = input("Enter the task priority (high, medium, low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Process the task based on priority using match-case
match priority:
    case "high":
        reminder = f"The task '{task}' is HIGH priority."
    case "medium":
        reminder = f"The task '{task}' is MEDIUM priority."
    case "low":
        reminder = f"The task '{task}' is LOW priority."
    case _:
        reminder = f"The task '{task}' has an UNKNOWN priority."

# Modify reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This is a time-sensitive task that requires immediate attention today!"

# Provide final customized reminder
print("\n--- Reminder ---")
print(reminder)
