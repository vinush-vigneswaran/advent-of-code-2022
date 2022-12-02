file = "data.txt"
read_file = open(file, 'r')

lines = read_file.readlines()

get_scores ={
    'A Y':6,'B Z':6, 'C X':6,
    'A X':3,'B Y':3,'C Z':3,
    'B X':0,'C Y':0,'A Z':0,
    'X':1,
    'Y':2,
    'Z':3
 }

scores = []

# create list of totals for each elf
for line in lines:
    play = line.rstrip('\n')

    score = get_scores[play] + get_scores[play[2]]
    scores.append(score)

print("total score:"+ str(sum(scores)))