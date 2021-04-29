def read_file(file_name):
    opened_file = open(file_name, 'r')
    lines_list = []
    for line in opened_file:
        line = line.split() # .decode('utf8').split()
        # print(line)
        lines_list.append(line)

    return lines_list
