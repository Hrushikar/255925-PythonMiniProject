import time
from utilts import clear_screen


def signup_and_create_account(ls):

    clear_screen()
    account_name = input('Enter Your Name (WITHOUT SPACES): ')
    account_password = input('Enter Your Password (WITHOUT SPACES): ')

    print("Creating Your Account .....")
    accounts_file = open('Accounts.txt', 'ab')

    if len(ls) == 0:
        new_last_id = 1
    else:
        new_last_id = int(ls[len(ls) - 1][0]) + 1

    line = ('{0}\t{1}\t{2}\t0\n'.format(str(new_last_id), account_name, account_password)).encode('utf-8')

    accounts_file.write(line)
    id_file_name = str(new_last_id) + '.txt'
    id_file = open(id_file_name, 'wb')

    print("Your Account Has Been Created And Your Id Is " + str(new_last_id))
    id_file.close()
    accounts_file.close()
    ls.append([str(new_last_id), account_name, account_password, '0'])
    time.sleep(5)
