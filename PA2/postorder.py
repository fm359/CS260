#!/usr/bin/python


def postorder(expression):
    stack = []
    for i in expression:
        if i == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(str(int(a) + int(b)))
        elif i == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(str(int(b) - int(a)))
        elif i == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(str(int(b) * int(a)))
        elif i == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(str(int(int(b) / int(a))))
        else:
            stack.append(int(i))
    return stack.pop()


print ("postorder.py tests")
print
print("Testing postfix: 5 5 5 - + 10 0 - 4 1 + 3 - / * (should return 25)")
print "..."
test = ['5', '5', '5', '-', '+', '10', '0', '-', '4', '1', '+', '3', '-', '/', '*']
print(postorder(test))
