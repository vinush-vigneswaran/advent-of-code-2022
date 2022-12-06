file = "data.txt"
read_file = open(file, 'r')

lines = read_file.readlines()

def convert_to_priority(char:str):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96

sum_of_priorities = 0

for line in lines:
    items = line.rstrip('\n')
    n = int(len(items)/2)

    rucksack_1_items = items[:n]
    rucksack_2_items = items[n:]

    common_letter = ''.join(set(rucksack_1_items).intersection(rucksack_2_items))
    sum_of_priorities += convert_to_priority(common_letter)

print("Sum of priorities: ", str(sum_of_priorities))