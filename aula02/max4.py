# coding: utf-8
# This program finds the maximum of two numbers.
# It uses the built-in max function.
# Can you do it with a conditional statement (if / if-else) instead?

x1 = float(input("number? "))
x2 = float(input("number? "))
x3 = float(input("number? "))
x4 = float(input("number? "))

# Use a conditional statement instead of max function!
#mx = max(x1, x2)

if x1>x2 and x1>x3 and x1>x4:
    print("Maximum:",x1)
elif x2>x3 and x2>x1 and x2>x4:
    print("Maximum:",x2)
elif x3>x1 and x3>x2 and x3>x4:
    print("Maximum:",x3)
else:
    print("Maximum:",x4)
