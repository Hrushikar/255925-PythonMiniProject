import withdrawal
import deposition
import activity_history
import change_password
from utilts import clear_screen


def dashboard(account):
    # account is a list of account information
    # account[0] -> id
    # account[1] -> name
    # account[2] -> password
    # account[3] -> balance

    print("\n------Hello, {0}------ ".format(account[1]))
    ch = int(input("\n1) show info \n2) show process history\n3) deposit\n4) withdraw\n"
                   "5) change password \n6) logout\n\nchoice>> "))

    clear_screen()
    if ch == 1:
        print("ID: {}\nName: {}\nBalance: {}\n".format(account[0], account[1], account[3]))
    elif ch == 2:
        activity_history.activity_history(account)
    elif ch == 3:
        deposition.deposit(account)
    elif ch == 4:
        withdrawal.withdrawal(account)
    elif ch == 5:
        change_password.change_password(account)
    elif ch == 6:
        return
        # logout - go back to menu1
    else:
        print("ERROR: Wrong choice\n")

    dashboard(account)
