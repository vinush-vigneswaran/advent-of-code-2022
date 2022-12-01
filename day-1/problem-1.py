file = "data.txt"
read_file = open(file, 'r')

lines = read_file.readlines()

total_for_elf = 0
total_for_all_elves = []

# create list of totals for each elf
for line in lines:

    if line != "\n":
        value_i = int(line)
        total_for_elf += value_i
    else:
        total_for_all_elves.append(total_for_elf)
        total_for_elf = 0

# find max value
print("total_for_all_elves:", total_for_all_elves)
print("Max value:", max(total_for_all_elves))