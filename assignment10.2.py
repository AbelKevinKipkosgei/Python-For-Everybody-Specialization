# Use mbox-short.txt file name as the file name
file_name = input(f"Enter file name: ")
try:
    file_handle = open(file_name, "r")
except:
    print(f"ERROR!! file does not exist.")
    quit()

counts = {}
for line in file_handle:
    if line.startswith("From "):
        word_list = line.split()
        time_list = word_list[5].split(":")
        hour = time_list[0]
        counts[hour] = counts.get(hour, 0) + 1

# print(counts)

hour_list = []
for key, value in counts.items():
    hour_tuple = (key, value)
    hour_list.append(hour_tuple)
    hour_list.sort()

# print(hour_list)

for key, value in hour_list:
    print(f"{key} {value}")
