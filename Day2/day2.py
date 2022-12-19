score = 0

input = (open("day2.txt", "r")).readlines()
input2 = [line.strip() for line in input]
input3 = [input2[i].split() for i in range(len(input2))]
for i in range(len(input3)):
    if input3[i][1] == "X":
        score += 0
    elif input3[i][1] == "Y":
        score += 3
    elif input3[i][1] == "Z":
        score += 6

for i in range(len(input3)):
    if input3[i][0] == "A": #rock
        if input3[i][1] == "X": #lose
            score += 3
        elif input3[i][1] == "Y": #draw
            score += 1
        elif input3[i][1] == "Z": #win
            score += 2
    elif input3[i][0] == "B": #paper
        if input3[i][1] == "X": #lose
            score += 1
        elif input3[i][1] == "Y": #draw
            score += 2
        elif input3[i][1] == "Z": #win
            score += 3
    elif input3[i][0] == "C": #scissors
        if input3[i][1] == "X": #lose
            score += 2
        elif input3[i][1] == "Y": #draw
            score += 3
        elif input3[i][1] == "Z": #win
            score += 1
    

print(score)