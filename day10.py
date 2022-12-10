with open(r'inputs\day10.txt') as input_file:
    raw_input = input_file.readlines()
input_instructions = [line.rstrip('\n') for line in raw_input]


def calc_signal(instructions):
    cycles, x = 0, 1
    signal_strengths = []
    pixels = ''
    for line in instructions:
        if abs((cycles % 40) - x) <= 1:
            pixels += '#'
        else:
            pixels += ' '
        cycles += 1
        if cycles % 40 == 20:
            signal_strengths.append(cycles * x)
        line_pieces = line.split()
        if line_pieces[0] == 'addx':
            if cycles % 40 == 19:
                signal_strengths.append((cycles + 1) * x)
            if abs((cycles % 40) - x) <= 1:
                pixels += '#'
            else:
                pixels += ' '
            cycles += 1
            x += int(line_pieces[1])
    return sum(signal_strengths), pixels


signal_data = calc_signal(input_instructions)
pixel_data = signal_data[1]
print(signal_data[0])
for i in range(0, 240, 40):
    print(pixel_data[i:i + 40])
