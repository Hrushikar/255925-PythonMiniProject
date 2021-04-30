def read_file(file_name):
    opened_file = open(file_name, 'rb')
    lines_list = []
    for line in opened_file:
        line = line.decode('utf-8').split()
        lines_list.append(line)

    return lines_list
