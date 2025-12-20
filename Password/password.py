def check_password():
    while True:
        x = input('enter your password: ')
        if len(x) < 4:
            print('at least enter 4 characters')
            continue

        if not x.isalnum():
            print('just enter only alphanumeric characters')
            continue

        else:
            print('your password is set')
            break
    return x


i = 0
print('first of all,set your password')
password_user = check_password()

while True:
    password = check_password()
    if password != password_user:
        print('password is wrong')
        i = i + 1

    else:
        print('password is correct')
        break

    if i % 3 == 0:
        while True:
            choice = input('wanna change your password? y/n')
            if choice == 'y':
                password_user = check_password()
                password = password_user
                print('you changed your password')
                i = 0
                break

            elif choice == 'n':
                break

            print('please enter y or n')
