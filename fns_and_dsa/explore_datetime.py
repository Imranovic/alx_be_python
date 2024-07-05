from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date: {current_date}")
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"formatted date: {formatted_date}")

# display_current_datetime()

def calculate_future_date():
    no_of_days = int(input("Enter the number of days: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=no_of_days)
    formatted_date = future_date.strftime("%Y-%m-%d")
    print(formatted_date)

# calculate_future_date()
