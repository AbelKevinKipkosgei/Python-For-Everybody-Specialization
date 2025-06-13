largest_number = None
smallest_number = None
invalid_occurred = False

print(
    f"""Input a number
Enter 'done' when finished"""
)
while True:
    user_input = input(f"\nEnter a number: ")
    if str(user_input).lower() == "done":
        break
    try:
        number = int(user_input)
    except:
        invalid_occurred = True
        continue
    if largest_number is None or number > largest_number:
        largest_number = number
    if smallest_number is None or number < smallest_number:
        smallest_number = number

if invalid_occurred:
    print(f"Invalid input")
print(f"Maximum is {largest_number}")
print(f"Minimum is {smallest_number}")
