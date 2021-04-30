import time
from read_file import read_file


def verify_old_password(previous_password):

    password_mismatch = True

    print("\nIf you want go back type \"Exit\"\n")
    for i in range(3):
        entered_value = input('\nEnter The Old Password : ')
        if entered_value == "Exit":
            return '-1'
        if entered_value == previous_password:
            password_mismatch = False
            break

    if password_mismatch:
        return '1'
    else:
        return '0'


def change_password(ls):

    old_password = ls[2]

    flag = verify_old_password(old_password)

    if flag == '0':
        new_password = input("\nEnter the new password: ")

        file_name = ls[0] + '.txt'
        process_list = read_file(file_name)
        id_file = open(file_name, 'ab')

        if len(process_list) == 0:
            last_id = 1
        else:
            last_id = int(process_list[len(process_list) - 1][0]) + 1

        id_file.write(
            ('{0}\tchange_password\t\t{1}\t{2}\t{3}\n'.format(str(last_id), str(time.ctime()), old_password, str(new_password))).encode('utf-8'))
        id_file.close()

        ls[2] = new_password

    elif flag == '1':
        input("Out of range of try ... press Enter")
