# Employee Time Tracking
# Scenario: You are developing an employee time tracking system. 
# Employees clock in and out, and you need to calculate the total hours worked by each 
# employee in a given day.

# Question: Write a function that takes a list of clock-in and clock-out times 
# (each represented as a tuple of (employee_id, clock_in, clock_out)) and returns a dictionary
#  with employee IDs as keys and their total hours worked as values.
import datetime
employee_details=[("emp1", datetime.time(hour=8, minute=0), datetime.time(hour=16, minute=00)),
                 ("emp2", datetime.time(hour=9, minute=0), datetime.time(hour=17, minute=00)),
                 ("emp3", datetime.time(hour=9, minute=3), datetime.time(hour=18, minute=45))]

def total_hours(emp_details):
    total_hours={}
    for emp_id, check_in, check_out  in emp_details:
        # print(datetime.timedelta(check_in.hour))
        # if datetime.timedelta(check_in.hour) < datetime.timedelta(check_out.hour):
        if check_in.hour < check_out.hour:
            hour= check_out.hour - check_in.hour
            minute=check_out.minute-check_in.minute
            
            # hour=datetime.time(datetime.timedelta(hours=check_out.hour) - datetime.timedelta(hours=check_in.hour))
            # minute=datetime.time(datetime.timedelta(minutes=check_out.minute) - datetime.timedelta(minutes=check_in.minute))
            total_hours[emp_id] = datetime.time(hour=hour, minute=minute)
            ##print(check_in.hour)p
    return total_hours

print(total_hours(employee_details))
