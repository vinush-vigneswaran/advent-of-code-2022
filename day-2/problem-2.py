file = "data.txt"
read_file = open(file, 'r')

lines = read_file.readlines()

get_scores ={
    'A':1,
    'B':2,
    'C':3,
    'X':0,
    'Y':3,
    'Z':6
 }

def user_play(play):

    elf_play = play[0]
    action = play[2]

    #draw
    if action == "Y":
        return elf_play

    #lose or win
    elif elf_play == 'A':
        if action == "X":#lose
            return 'C'
        if action == "Z":#win
            return 'B'
    elif elf_play == 'B':
        if action == "X":#lose
            return 'A'
        if action == "Z":#win
            return 'C'
    elif elf_play == 'C':
        if action == "X":#lose
            return 'B'
        if action == "Z":#win
            return 'A'

scores = []

# create list of totals for each elf
for line in lines:
    play = line.rstrip('\n')
    score = get_scores[play[2]] + get_scores[user_play(play)]
    scores.append(score)

print("total score:"+str(sum(scores)))