name = input("Enter the student name : ")

#subject1
x = input('Enter the first subject name: ');f = input(f'Enter the {x} mark')
#subject2
y = input('Enter the second subject name : ');r = input(f'Enter the {y} mark')
#subject3
z = input('Enter the last subject name: ');a = input(f"Enter the {z} mark")


m = [f'average{round((int(f) + int(r) + int(a)) / 3,2)}']

print(f'{x} {[f]} \n {y} {[r]} \n {z} {[a]} \n{m}')
