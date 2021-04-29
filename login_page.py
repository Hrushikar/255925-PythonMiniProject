from dashboard import dashboard
from utilts import clear_screen


def login_page(acc_list):

    login_id = input('Please, Enter your info(press "Ctrl+C" to go back) \nID: ')
    login_password = input('Enter your Password: ')
    found = False
    for account in acc_list:
        if account[0] == login_id and account[2] == login_password:
            found = True
            clear_screen()
            dashboard(account)
            break
        else:
            continue

    if not found:
        clear_screen()
        print('The entered ID or Password is incorrect\nWould you like to try again? (y/n)', end='')
        char = input()
        if char == 'y' or char == 'Y':
            login_page(acc_list)
        else:
            print('Exiting...')
            exit(0)

    else:
        acc_file = open('Accounts.txt', 'wb')
        print('Saving changes...')
        for acc in acc_list:
            for elements in acc:
                acc_file.write(("%s\t" % elements).encode('utf-8'))
            acc_file.write('\n'.encode('utf-8'))
