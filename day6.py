with open(r'inputs\day6.txt') as input_file:
    signal = input_file.readline().rstrip('\n')


def find_signal_start(seq, size):
    for i in range(len(seq) - size + 1):
        if len(set(seq[i:i+size])) == size:
            return i + size


print(find_signal_start(signal, 4))
print(find_signal_start(signal, 14))
