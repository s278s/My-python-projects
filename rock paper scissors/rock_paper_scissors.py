from random import choice

possibilities = ['rock', 'paper', 'scissors']
wins = 0
loses = 0
ties = 0
print('welcome to rock paper scissors game\nyou can exit by typing "exit"\n')


while True:
    user_choice = input('rock or paper or scissors: ')
    pc_choice = choice(['rock', 'paper', 'scissors'])

    if user_choice.lower() == 'exit':
        break

    if user_choice not in possibilities:
        print('wrong choice')
        continue

    if user_choice == pc_choice:
        print('tie')
        ties = ties + 1
        continue

    if user_choice == 'rock' and pc_choice == 'scissors' or\
        user_choice == 'paper' and pc_choice == 'rock' or\
        user_choice == 'scissors' and pc_choice == 'paper':
        print(pc_choice)
        print('You win')
        wins = wins + 1
        continue

    print(pc_choice)
    print('You lost try again')
    loses = loses + 1

print(f'You won {wins} times and lost {loses} times and {ties} times')
