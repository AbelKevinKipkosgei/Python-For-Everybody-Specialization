# Use 'regex_sum_2234715.txt' as the file name
import re

file_name = input("Enter file name: ")
# try:
file_handle = open(file_name, "r")
# except:
#     print(f"ERROR!! file does not exist.")
#     quit()

total = 0
for line in file_handle:
    line = line.rstrip()
    numbers = re.findall(r"[0-9]+", line)
    for num in numbers:
        total = total + int(num)

print(total)
