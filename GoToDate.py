from datetime import datetime, timedelta

def calculate_date(input_request, weeks, direction='future'):
    try:
        date_obj = datetime.strptime(input_request, '%d/%m/%Y') 
        delta = timedelta(weeks=weeks)
        if direction == 'previous':
            result_date = date_obj - delta
        else:  
            result_date = date_obj + delta
        return result_date.strftime('%d/%m/%Y')  
    except ValueError:
        return "Invalid input date format. Please use DD/MM/YYYY."

input_date = "17/05/2023"
weeks =15



previous = calculate_date(input_date, weeks, 'previous')
future = calculate_date(input_date, weeks, 'future')

print("Previous date:", previous)
print("Future date:", future)
