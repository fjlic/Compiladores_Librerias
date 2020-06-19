# Description: program converts infix to postfix and prefix notation
# https://gist.github.com/awadalaa/7ef7dc7e41edb501d44d1ba41cbf0dc6
# https://www.web4college.com/converters/infix-to-postfix-prefix.php
# https://www.infor.uva.es/~cvaca/asigs/AlgInfPost.htm

import sys

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[self.size()-1]

     def size(self):
         return len(self.items)

class InfixConverter:
    def __init__(self):
        self.stack = Stack()
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
		
# define fucntion that is used to assign precendence to operator.
# Here ^ denotes exponent operator.
# In this fucntion we assume that higher integer value
# means higher precendence */
    def hasLessOrEqualPriority(self, a, b):
        if a not in self.precedence:
            return False
        if b not in self.precedence:
            return False
        return self.precedence[a] <= self.precedence[b]

    def isOperator(self, x):
        ops = ['+', '-', '/', '*']
        return x in ops

    def isOperand(self, ch):
        return ch.isalpha() or ch.isdigit()

    def isOpenParenthesis(self, ch):
        return ch == '('

    def isCloseParenthesis(self, ch):
        return ch == ')'

    def toPostfix(self, expr):
        expr = expr.replace(" ", "")
        self.stack = Stack()
        output = ''
#  run loop till end of infix expression 
        for c in expr:
            if self.isOperand(c):
			    #add operand symbol to postfix expr
                output += c
            else:
                if self.isOpenParenthesis(c):
                    self.stack.push(c)
                elif self.isCloseParenthesis(c):
                    operator = self.stack.pop()
					#pop and keep popping until 
					#'(' encounterd 
                    while not self.isOpenParenthesis(operator):
                        output += operator
                        operator = self.stack.pop()              
                else:
                    while (not self.stack.isEmpty()) and self.hasLessOrEqualPriority(c,self.stack.peek()):
                        output += self.stack.pop()		# add them to postfix expresion 
                    self.stack.push(c)
					#because just above while loop will terminate we have oppped one extra item
					#for which condition fails and loop terminates, so that one
        while (not self.stack.isEmpty()):
            output += self.stack.pop()
        return output
    
    '''
     1. Reverse expression string
     2. Replace open paren with close paren and vice versa
     3. Get Postfix and reverse it
    '''
    def toPrefix(self, expr):
        reverse_expr =''
        for c in expr[::-1]:
            if c == '(':
                reverse_expr += ")"
            elif c == ')':
                reverse_expr += "("
            else:
                reverse_expr += c

        reverse_postfix = self.toPostfix(reverse_expr)
        return reverse_postfix[::-1]


    def convert(self, expr):
        try:
            result = eval(expr)
        except:
            result = expr
        print """
            Original expr is: {}
            Postfix is: {}
            Prefix is: {}
            result is: {}
        """.format(expr, self.toPostfix(expr), self.toPrefix(expr), result)

def main(argv):
    infix = InfixConverter()
    while True:
        infix_expression = raw_input("Enter an expression in infix notation or 'exit' to stop: ")
        if (infix_expression.lower() == 'exit'):
            break
        infix.convert(infix_expression)


if __name__ == "__main__":
    main(sys.argv)
