# Use the file name words.txt as the file name
file_name = input(f"Enter file name: ")
try:
    file_handle = open(file_name)
except:
    print(f"Error!! File '{file_name}' does not exist.")
    quit()
for line in file_handle:
    print(f"{line.rstrip().upper()}")
