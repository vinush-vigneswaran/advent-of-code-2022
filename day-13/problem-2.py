import ast
import math

def is_right_order(left, right):
    # print(left)
    # print(right)
    left_is_short = False

    if len(left) < len(right):
        length = len(left)
        left_is_short = True
    elif len(left) > len(right):
        length = len(right)
        left_is_short = False
    else:
        length = len(right)
        left_is_short = False

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

ordered_list = [[[2]],[[6]]]

for line in lines:
    val1 = line.rstrip('\n')
    # print(val1)

    if val1 != "":
        # python literal
        val1 = ast.literal_eval(val1)

        temp_ordered_list = ordered_list.copy()

        appended_to_list = False
        for i in range(len(temp_ordered_list)):
            packet = temp_ordered_list[i]

            right_order = is_right_order(val1, packet)

            # print(right_order, "\n")

            if right_order:
                ordered_list.insert(i, val1)
                appended_to_list = True
                break

        if not appended_to_list:
            ordered_list.append(val1)

        #print("val1\t",val1)
        #print("ordered_list\t", ordered_list)

#result
i = 1
results = []
for x in ordered_list:
    print(i, '\t', x)
    if x == [[2]]:
        results.append(i)
    elif x == [[6]]:
        results.append(i)
    i += 1

print("results: ", results, " = ", math.prod(results))