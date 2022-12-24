import operator
import math

all_monkey_items = {
    0: [65, 78],
    1: [54, 78, 86, 79, 73, 64, 85, 88],
    2: [69, 97, 77, 88, 87],
    3: [99],
    4: [60, 57, 52],
    5: [91, 82, 85, 73, 84, 53],
    6: [88, 74, 68, 56],
    7: [54, 82, 72, 71, 53, 99, 67],
}

monkey_function = {
    0: 'old * 3',
    1: 'old + 8',
    2: 'old + 2',
    3: 'old + 4',
    4: 'old * 19',
    5: 'old + 5',
    6: 'old * old',
    7: 'old + 1',
}

monkey_throw_to = {
    0: [3,2],
    1: [7,4],
    2: [3,5],
    3: [5,1],
    4: [6,7],
    5: [1,4],
    6: [2,0],
    7: [0,6],
}

monkey_test_val = {
    0: 5,
    1: 11,
    2: 2,
    3: 13,
    4: 7,
    5: 3,
    6: 17,
    7: 19,
}

monkey_inspection_counts = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
}

def parse_monkey_function(monk_num, worry_lvl, monkey_function=monkey_function):
    op_1_str, operation_str, op_2_str = (monkey_function[monk_num]).split()

    if op_1_str == "old":
        op1 = worry_lvl
    else:
        op1 = int(op_1_str)

    if op_2_str == "old":
        op2 = worry_lvl
    else:
        op2 = int(op_2_str)

    if operation_str == "+":
        return op1 + op2
    elif operation_str == "-":
        return op1 - op2
    elif operation_str == "*":
        return op1 * op2
    elif operation_str == "/":
        return op1 / op2

def run_test(monkey_num, worry_level):
    if worry_level % monkey_test_val[monkey_num] == 0:
        return 1
    else:
        return 0


worry_level = 0
rounds = 20

for round in range(1, rounds+1):

    for monkey_num, monkey_items in all_monkey_items.items():
        temp = monkey_items.copy()

        for worry_level in temp:

            #worry level
            worry_level = parse_monkey_function(monkey_num, worry_level)
            worry_level = math.floor(worry_level/3)

            #conduct test to find out which monkey to throw to
            to_monkey = monkey_throw_to[monkey_num][run_test(monkey_num, worry_level)]

            # throw item from_monkey to to_monkey
            all_monkey_items[to_monkey].append(worry_level)
            monkey_items.pop(0)

            #count number of inspections
            monkey_inspection_counts[monkey_num] += 1

    #print(round, all_monkey_items)


print("All results: ", monkey_inspection_counts)
results = [v for k, v in sorted(monkey_inspection_counts.items(), key=lambda item: item[1], reverse=True)]
results = results[0] * results[1]
print("Results: ", results)