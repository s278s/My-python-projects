from random import choice

print('Michael','CJ','Niko','tommy')
x = ['Michael','CJ','Niko','tommy']

while True:
    y = choice(x)
    z = input(f"It's  {y}  Is it right? " if len(x) >= 2 else f'Then {y} must be your guess')
    if z.lower() == 'yes':
        print('YES!!!!!')
        break
    else:
        print('I will try again')
    x.remove(y)
