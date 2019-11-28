#!/usr/bin/env python

#evaluates prefix expression and returns output
def preorder(expression):
	token = expression.pop(0)
	if token == '+':
		return preorder(expression) + preorder(expression)
	elif token == '-':
		return preorder(expression) - preorder(expression)
	elif token == '*':
		return preorder(expression) * preorder(expression)
	elif token == '/':
		return preorder(expression) / preorder(expression)
	else:
		return int(token)

print "preorder.py tests"
print
print "Testing prefix: - * / 15 - 7 + 1 1 3 + 2 + 1 1 (should return 5)"
print "..."
test = ['-','*','/',"15",'-','7','+','1','1','3','+','2','+','1','1']
print preorder(test)
