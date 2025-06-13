# Use the file name mbox-short.txt as the file name
file_name = input(f"Enter the file name: ")
try:
    file_handle = open(file_name)
except:
    print(f"ERROR!! file does not exist.")
    quit()

count = 0
for line in file_handle:
    if line.startswith("From "):
        count += 1
        line_list = line.split()
        print(f"{line_list[1]}")

print(f"There were {count} lines in the file with From as the first word")
