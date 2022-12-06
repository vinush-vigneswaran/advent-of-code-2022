file = "data.txt"
read_file = open(file, 'r')

lines = read_file.readlines()

def convert_to_priority(char:str):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96

sum_of_priorities = 0
num = 3

for i in range(num-1, len(lines), num):

    rucksack1 = lines[i].rstrip('\n')
    rucksack2 = lines[i-1].rstrip('\n')
    rucksack3 = lines[i-2].rstrip('\n')

    common_letter = ''.join(set(rucksack1).intersection(rucksack2))
    common_letter = ''.join(set(common_letter).intersection(rucksack3))

    sum_of_priorities += convert_to_priority(common_letter)

print("Sum of priorities pt2: ", str(sum_of_priorities))