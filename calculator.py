from decimal import Decimal as D
from fractions import Fraction as F

num1 = D(input("Enter a number: "))
num2 = D(input("Enter another number: "))

print("%.2f + %.2f = %.2f " % (num1, num2, num1 + num2))
print("%.2f - %.2f = %.2f " % (num1, num2, num1 - num2))
print("%.2f * %.2f = %.2f " % (num1, num2, num1 * num2))
print("%.2f / %.2f = %.2f " % (num1, num2, num1 / num2))
print('num1 = %s' % F(num1),"\nnum2 = %s" % F(num2))