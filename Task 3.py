from datetime import datetime, timedelta

days = 5
work_days = 2
rest_days = 1
start_date = datetime(2020,1,30)

def schedule(days, work_days, rest_days, start_date):
    
    list = []
    work_days_count = 0
    current_day = start_date

    try:
        for i in range(days):
            if work_days_count == work_days:
                current_day += timedelta(days = rest_days)
                work_days_count = 0
                continue
            if i == 0:
                list.append(current_day)
                work_days_count += 1
            else:
                current_day += timedelta(days = 1)
                list.append(current_day)
                work_days_count += 1
        return list
    except TypeError:
        print("Error: Numeric data type expected.")
result = schedule(days, work_days, rest_days, start_date)
print(result)

        

