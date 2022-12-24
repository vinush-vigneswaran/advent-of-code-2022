import ast

def is_right_order(left, right):
    # print(left)
    # print(right)
    left_is_short = False

    if len(left) <= len(right):
        length = len(left)
        left_is_short = True
    else:
        length = len(right)

    for i in range(length):
        # print("--", left[i], right[i])
        # If identical continue
        if left[i] == right[i]:
            continue

        # If both values are integers, the lower integer should come first
        elif type(left[i])==int and type(right[i])==int and left[i] < right[i]:
            return True
        elif type(left[i])==int and type(right[i])==int and left[i] > right[i]:
            return False

        # If both values are lists, compare the first value of each list, then second, etc.
        elif type(left[i])==list and type(right[i])==list:
            return is_right_order(left[i], right[i])

        #If exactly one val is an int, convert the int to list which contains that int as its only val
        elif type(left[i])==int and type(right[i])==list:
            return is_right_order([left[i]], right[i])

        elif type(left[i])==list and type(right[i])==int:
            return is_right_order(left[i], [right[i]])

    return left_is_short


# read file
file = "data.txt"
read_file = open(file, 'r')
lines = read_file.readlines()
index = 0
count = 0

for i in range(0, len(lines), 3):
    left = lines[i].rstrip('\n')
    right = lines[i+1].rstrip('\n')

    # python literal
    left = ast.literal_eval(left)
    right = ast.literal_eval(right)

    index += 1
    right_order = is_right_order(left, right)

    if right_order:
        count += index

#result
print(count)
