import time
import withdrawal
import deposition
import activity_history
import change_password
from utilts import clear_screen


def dashboard(account):

    print("\n------Hello, {0}------ ".format(account[1]))
    ch = int(input("\n1) Show my information \n2) Show process history\n3) Deposit money\n4) Withdraw money\n"
                   "5) Change password\n6) Logout\n\nChoice: "))

    clear_screen()
    if ch == 1:
        print("ID: {}\nName: {}\nBalance: {}\n".format(account[0], account[1], account[3]))
        print('Please wait while you are being redirected...')
        time.sleep(5)
    elif ch == 2:
        activity_history.activity_history(account)
    elif ch == 3:
        deposition.deposit(account)
        print('Please wait while you are being redirected...')
        time.sleep(5)
    elif ch == 4:
        withdrawal.withdrawal(account)
        print('Please wait while you are being redirected...')
        time.sleep(5)
    elif ch == 5:
        change_password.change_password(account)
        print('Please wait while you are being redirected...')
        time.sleep(5)
    elif ch == 6:
        return
    else:
        print("Wrong choice. Please try again\n")

    dashboard(account)
