i = 0


x = input('set your password').strip()


while True:
    password = input('Enter your password').strip()

    if len(password) == 0:
        print('You must at least enter a character')

    elif password != x:
        print('Password is wrong')
        i += 1
        print(f'you entered {i} times wrong password')

    else:
        print('_____Password is correct_____')
        break

    if i % 3 == 0:
        y = input('wanna change your password?\n1)Yes\t2)No')

        while True:
            if y == '1':
                new_password = input('Enter your new password').strip()

                if len(new_password) != 4:
                    print('You must enter 4 numbers ')

                if not new_password.isalnum():
                    print('Just words and numbers')
                    continue

                else:
                    print('Your password changed successfully')
                    i = 0
                    x = new_password
                    break

            if y == '2':
                break

            else:
                print('Wrong option')
