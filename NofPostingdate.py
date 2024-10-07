from datetime import datetime, timedelta

def generate_future_dates(start_date_str, days_interval, iterations):
    # Convert the input date string to a datetime object
    start_date = datetime.strptime(start_date_str, '%d/%m/%Y')
    
    # Initialize an empty list to store the future dates
    future_dates = []
    
    # Generate future dates
    for i in range(iterations):
        future_date = start_date + timedelta(days=days_interval * (i + 1))
        future_dates.append(future_date.strftime('%d/%m/%Y'))
    
    return future_dates

# Example usage
input_date = '12/04/2023'
interval = 7
number_of_dates = 50

future_dates_list = generate_future_dates(input_date, interval, number_of_dates)
for date in future_dates_list:
    print(date)
