task = input("Enter your task: ")


# Ask for the task’s priority
priority = input("Priority (high/medium/low): ").lower()


# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()


# Process the task based on priority using match-case
match priority:
    case "high":
        reminder = f"'{task}' is HIGH priority."
    case "medium":
        reminder = f"'{task}' is MEDIUM priority."
    case "low":
        reminder = f"'{task}' is LOW priority."
    case _:
        reminder = f"'{task}' has an UNKNOWN priority."


# Modify reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This is a time-sensitive task that requires immediate attention today!"


# Print final customized reminder
print()
print(f"reminder: {reminder}")
