try:
    hours = float(input("Enter hours: "))
    rate_per_hour = float(input("Enter rate per hour: "))
except:
    print(f"Error, please enter a numeric input!!")
    quit()

if hours <= 40:
    gross_pay = hours * rate_per_hour
    print(f"{gross_pay}")
else:
    extra_hours = hours - 40
    extra_hours_pay = (rate_per_hour * 1.5) * extra_hours
    normal_hours_pay = rate_per_hour * 40
    gross_pay = normal_hours_pay + extra_hours_pay
    print(f"{gross_pay}")
