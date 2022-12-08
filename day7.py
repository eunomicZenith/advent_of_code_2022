with open(r'inputs\day7.txt') as input_file:
    raw_input = input_file.readlines()
input_list = [line.rstrip('\n') for line in raw_input]


def folderize(commands_list):
    for line in commands_list:
        line_pieces = line.split()
        if line_pieces[1] == 'cd':
            if line_pieces[2] == '/':
                root = {'__size': 0}
                current_folder = root
                path = [root]
            elif line_pieces[2] == '..':
                path.pop()
                current_folder = path[-1]
            else:
                current_folder[f'{line_pieces[2]}'] = {'__size': 0}
                current_folder = current_folder[f'{line_pieces[2]}']
                path.append(current_folder)
        elif line_pieces[0].isnumeric():
            current_folder['__size'] += int(line_pieces[0])
    return root


def calc_size(folder):
    folder_sizes = []
    for key in folder.keys():
        if type(folder[key]) is dict:
            child_data = calc_size(folder[key])
            child_size = child_data[0]
            child_folder_sizes = child_data[1]
            folder_sizes.append(child_size)
            folder_sizes.extend(child_folder_sizes)
            folder['__size'] += child_size
    return folder['__size'], folder_sizes


root_size, folder_sizes = calc_size(folderize(input_list))
small_folders_total = sum([size for size in folder_sizes if size <= 100_000])
print(small_folders_total)

# part 2's solution
needed_space = 30_000_000 - (70_000_000 - root_size)
deletion_candidates_sizes = [size for size in folder_sizes if size >= needed_space]
size_to_delete = min(deletion_candidates_sizes)
print(size_to_delete)
