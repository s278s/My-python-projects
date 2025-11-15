i = 0
x = '1386'
p = False

while True:
    password = input('Enter your password').strip()

    if i >=3:
        p = False
        while True:
            if p:
                break

            y = input('wanna change your password?\n1)Yes\t2)No')

            if y == '1':
                while True:
                    new_password = input('Enter your new password').strip()

                    if len(new_password) < 4:
                        print('You must enter 4 numbers')

                    elif len(new_password) > 4:
                        print('You can enter up to 4 numbers')

                    elif not new_password.isalnum():
                        print('Just words and numbers')

                    elif len(new_password) == 4:
                        print('Your password changed successfully')
                        i = 0
                        x = new_password
                        p = True
                        break

            elif y == '2':
                i = 0
                break

            else:
                print('wrong option')

    elif len(password) < 4:
        print('You must enter 4 numbers')

    elif len(password) > 4:
        print('You can enter up to 4 numbers')

    elif not password.isalnum():
        print('Just words and numbers')

    elif password == x:
        print('Password is correct\n')
        print('Your mom is dead!!')
        break

    else:
        print('Password is wrong')
        i +=1
