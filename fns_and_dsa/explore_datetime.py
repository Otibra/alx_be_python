from datetime import datetime, timedelta  # Import the necessary modules

def display_current_datetime():
    current_date = datetime.now()          # Get the current datetime
    print(current_date)                     # Use the correct variable name

# Ask the user for input
integer = int(input("Enter the number of days: "))

def calculate_future_date(days):
    current_date = datetime.now()          # datetime.now() needs the module reference
    future_date = current_date + timedelta(days=days)  # Use correct variable 'days'
    print(future_date)

# Call the function using the user input
calculate_future_date(integer)
