# Use the file name romeo.txt as the file name
file_name = input(f"Enter file name: ")
try:
    file_handle = open(file_name)
except:
    print(f"ERROR!! file name does not exist.")
    quit()

word_list = list()

for line in file_handle:
    line_list = line.split()
    # print(line_list)
    for word in line_list:
        if word not in word_list:
            word_list.append(word)

word_list.sort()
print(word_list)
