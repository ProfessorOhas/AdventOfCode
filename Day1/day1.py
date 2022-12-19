input = []
input = (open("day1.txt", "r")).readlines()
# print(input)

input2 = []
for line in input:
    if line != "\n":
        input2.append(int(line.strip()))
    else:
        input2.append(line)
print(input2)

sums = []
sum = 0
for i in range(len(input2)):
    if input2[i] != "\n":
        print(input2[i])
        sum += input2[i]
    else:
        sums.append(sum)
        sum = 0

print(sums)
max1 = 0
for sum in sums:
    if sum > max1:
        max1 = sum
print(max1)

sums.remove(max1)
max2 = 0
for sum in sums:
    if sum > max2:
        max2 = sum
print(max2)

sums.remove(max2)
max3 = 0
for sum in sums:
    if sum > max3:
        max3 = sum
print(max3)

maxes = max1 + max2 + max3
print(maxes)