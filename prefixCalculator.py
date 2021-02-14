from collections import deque

class Calculator(object):
    def eval(self, tokens):
        token=tokens.popleft()
        if token=='+': 
            return self.eval(tokens)+self.eval(tokens)
        elif token=='-':
            return self.eval(tokens)-self.eval(tokens)
        elif token=='*':
            return self.eval(tokens)*self.eval(tokens)
        elif token=='/':
            return self.eval(tokens)/self.eval(tokens)
        else:   
             # must be just a number
             return int(token)

    def evaluate(self, expression):
        # print(self.to_suffix(string))
        return self.eval(deque(expression.split()))


calc = Calculator()
# input should split each operator/number with space, can handle float, negative and brackets
expression= '- / 10 + 1 1 * 1 2'
print(calc.evaluate(expression))





