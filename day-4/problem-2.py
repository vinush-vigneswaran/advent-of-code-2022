import re

file = "data.txt"
read_file = open(file, 'r')

lines = read_file.readlines()

total = 0

for line in lines:
    coverage = line.rstrip('\n')
    a, b, c, d = re.findall(r'\d+', coverage)
    elf_1_lower, elf_1_upper, elf_2_lower, elf_2_upper = int(a), int(b), int(c), int(d)

    if (elf_1_upper >= elf_2_upper) and (elf_1_lower <= elf_2_lower):
        total += 1
    elif (elf_2_upper >= elf_1_upper) and (elf_2_lower <= elf_1_lower):
        total += 1
    elif (elf_1_upper >= elf_2_lower) and (elf_2_lower >= elf_1_lower):
        total += 1
    elif (elf_2_upper >= elf_1_lower) and (elf_1_lower >= elf_2_lower):
        total += 1

print(total)
