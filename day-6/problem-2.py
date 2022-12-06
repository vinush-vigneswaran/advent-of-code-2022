import re

file = "data.txt"
read_file = open(file, 'r')

line = read_file.readlines()
line = line[0]

len_of_marker = 14


def is_unique_char(list):
    set_list = set(list)

    if (len(set_list) == len(list)):
        return True

    return False

for char_i in range(len_of_marker, len(line)+1):
    marker = line[char_i-len_of_marker:char_i]

    if is_unique_char(marker):
        print(marker, char_i)
        break

