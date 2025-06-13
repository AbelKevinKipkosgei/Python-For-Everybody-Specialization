# Use the file name mbox-short.txt as the file name
file_name = input(f"Enter file name: ")
count = 0
extracted_value = 0
try:
    file_handle = open(file_name)
except:
    print(f"ERROR!!, file name does not exist.")
    quit()

for line in file_handle:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        start_pos = line.find("0")
        extracted_value += float(line[start_pos:])
        average_value = extracted_value / count

print(f"Average spam confidence: {average_value}")
