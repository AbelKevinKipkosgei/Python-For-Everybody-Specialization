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
        sender = word_list[1]
        counts[sender] = counts.get(sender, 0) + 1

# print(counts)

big_sender = None
big_count = None

for sender, count in counts.items():
    if big_count is None or count > big_count:
        big_sender = sender
        big_count = count

print(f"{big_sender} {big_count}")
