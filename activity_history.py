import time

import read_file
from utilts import clear_screen


def print_activity(process):
    date = '{}'.format(process[2:7])
    print('{0}\t{1}\t{2}{3: ^10} {4: ^10}'.format(process[0], process[1].center(len('change_password')), date.center(len(date)), process[7], process[8]))


def activity_history(ls):

    choice = int(input('1) Show deposit activity\n2) Show withdrawal activity\n3) Show '
                       'password change activity\n4) Show all activities\n'
                       '5) Clear activities\n\nChoice: '))

    file_name = ls[0] + '.txt'
    id_list = read_file.read_file(file_name)

    clear_screen()
    top_line = '\nID\t' + 'Type'.center(len('change_password')) + 'Date and Time'.center(40) + 'before'.center(
        10) + 'after'.center(15)
    print(top_line)
    print('-' * len(top_line))
    if choice == 1:
        for line in id_list:
            if line[1] == 'deposit':
                print_activity(line)
    elif choice == 2:
        for line in id_list:
            if line[1] == 'withdraw':
                print_activity(line)
    elif choice == 3:
        for line in id_list:
            if line[1] == 'change_password':
                print_activity(line)
    elif choice == 4:
        for line in id_list:
            print_activity(line)
    elif choice == 5:
        new_file = open(file_name, 'wb')
        new_file.close()
    else:
        print('Wrong choice. Please try again later')

    input('\nPress Enter to go back..')
    time.sleep(3)
    clear_screen()
