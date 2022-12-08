with open(r'inputs\day1.txt') as input_file:
    calories_list = input_file.readlines()

cals = [0]
for line in calories_list:
    if line.rstrip('\n').isnumeric():
        cals[-1] += int(line)
    else:
        cals.append(0)
print(max(cals))

# part 2
cals.sort()
top_three_elves_calories = sum(cals[-3:])
print(top_three_elves_calories)
