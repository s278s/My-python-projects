
x = input().strip()

if x.isalnum() == False:
    print('Just words and numbers')

elif len(x) < 1 :
    print('You must enter at least a number')

elif len(x) > 4:
    print('You must enter up to 4 numbers')

elif x == '1386':
    print('Password is correct',end='\n\n')
    print('Your wifi password is 9786216')

else:
    print('Password is wrong')