from collections import deque

class PrefixCalc(object):

    def eval(self, tokens):
        token = tokens.popleft()
        if token == '+':
            return self.eval(tokens) + self.eval(tokens)
        else:
            if token == '-':
                return self.eval(tokens) - self.eval(tokens)
            if token == '*':
                return self.eval(tokens) * self.eval(tokens)
            if token == '/':
                return self.eval(tokens) / self.eval(tokens)
            return int(token)

    def prefixEvaluator(self, expression):
        print expression
        return self.eval(deque(expression.split()))
