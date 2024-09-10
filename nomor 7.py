month, day, year = map(int,input("enter the mm/dd/yyyy: ").split("/"))

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_in_month[1] = 29

day_number = sum(days_in_month[:month - 1]) + day

print(f"The day number for {month} / {day} / {year} is: {day_number}")