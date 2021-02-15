from operator import add, sub, mul, truediv


class Calculator(object):

    def infix_to_prefix(formula):
        op_stack = []
        exp_stack = []
        for ch in formula:
            if not ch in OPERATORS:
                exp_stack.append(ch)
            elif ch == '(':
                op_stack.append(ch)
            elif ch == ')':
                while op_stack[-1] != '(':
                    op = op_stack.pop()
                    a = exp_stack.pop()
                    b = exp_stack.pop()
                    exp_stack.append( op+b+a )
                op_stack.pop() # pop '('
            else:
                while op_stack and op_stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[op_stack[-1]]:
                    op = op_stack.pop()
                    a = exp_stack.pop()
                    b = exp_stack.pop()
                    exp_stack.append( op+b+a )
                op_stack.append(ch)

        # leftover
        while op_stack:
            op = op_stack.pop()
            a = exp_stack.pop()
            b = exp_stack.pop()
            exp_stack.append( op+b+a )
        print exp_stack[-1]
        return exp_stack[-1]


    def evaluate(self, string):
        # print(self.to_suffix(string))
        return self.infix_to_prefix(string)


calc = Calculator()
# input should split each operator/number with space, can handle float, negative and brackets
print(calc.evaluate('( 20.0 / 2 ) + ( 3 * ( 1 + 2 ) )'))
