with open(r'inputs\day2.txt') as input_file:
    moves_list = input_file.readlines()

e_opt = 'ABC'
y_opt = 'XYZ'
your_score = 0

for line in moves_list:
    em = e_opt.index(line[0])
    ym = y_opt.index(line[2])
    your_score += ym + 1
    your_score += ((ym - em + 1) % 3) * 3

print(your_score)

# part 2

your_score = 0

for line in moves_list:
    em = e_opt.index(line[0])
    ym = y_opt.index(line[2])
    your_score += ym * 3
    your_score += ((em + ym - 1) % 3) + 1

print(your_score)
