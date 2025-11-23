from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    # Format the datetime as "YYYY-MM-DD HH:MM:SS"
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))

integer = int(input("Enter the number of days: "))

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    # Format the future datetime the same way
    print(future_date.strftime("%Y-%m-%d %H:%M:%S"))

# Display current datetime
display_current_datetime()
# Display future datetime
calculate_future_date(integer)
