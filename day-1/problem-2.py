file = "data.txt"
read_file = open(file, 'r')

lines = read_file.readlines()


total_for_elf = 0
total_for_all_elves = []

# create list of totals for each elf
for line in lines:
    #print(line)
    if line != "\n":
        value_i = int(line)
        total_for_elf += value_i
    else:
        total_for_all_elves.append(total_for_elf)
        total_for_elf = 0

total_for_all_elves.sort(reverse=True)

# find top 3 sum value
print("sorted_total_for_all_elves:", total_for_all_elves)
print("Top three values", total_for_all_elves[0:3])
print("Top three sum values", sum(total_for_all_elves[0:3]))