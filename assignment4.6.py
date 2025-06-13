def computepay(hours, rate_per_hour):
    if hours <= 40:
        gross_pay = hours * rate_per_hour
    else:
        extra_hours = hours - 40
        extra_hours_pay = (rate_per_hour * 1.5) * extra_hours
        normal_hours_pay = rate_per_hour * 40
        gross_pay = normal_hours_pay + extra_hours_pay
    return gross_pay


try:
    hours_worked = float(input("Enter hours: "))
    rate_per_hour_worked = float(input("Enter rate per hour: "))
except:
    print(f"Error, please enter a numeric input!!")
    quit()

total_pay = computepay(hours_worked, rate_per_hour_worked)
print(f"Pay {total_pay}")
