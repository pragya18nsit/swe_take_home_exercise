from collections import deque


OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRIORITY = {'+':1, '-':1, '*':2, '/':2}

class Calc(object):

    def evaluate(self, tokens):
        token=tokens.popleft()
        if token=='+':
            return self.evaluate(tokens)+self.evaluate(tokens)
        elif token=='-':
            return self.evaluate(tokens)-self.evaluate(tokens)
        elif token=='*':
            return self.evaluate(tokens)*self.evaluate(tokens)
        elif token=='/':
            return self.evaluate(tokens)/self.evaluate(tokens)
        else:
             # must be just a number
             return int(token)

    def prefixEvaluator(self, expression):
        print expression
        return self.evaluate(deque(expression.split()))



    def infixEvaluator(self, expression):
        # print(self.to_suffix(string))
        token_list = expression.split()
        print(token_list)
             # Operator priority dictionary
        pre_dict = {'*':3,'/':3,'+':2,'-':2,'(':1}
             # Operator stack
        operator_stack = []
             # Operand stack
        operand_stack = []
        for token in token_list:
                     # Number into the operand stack
            if token.isdecimal() or token[1:].isdecimal():
                operand_stack.append(int(token))
                     # Left parenthesis into the operator stack
            elif token == '(':
                operator_stack.append(token)
                     # When the right bracket is encountered, the operators above the left bracket on the top of the stack must be evaluated
            elif token == ')':
                top = operator_stack.pop()
                while top != '(':
                                     # Every time an operator pops up, two operands must pop up to evaluate
                                     # Note that the order of the pop-up operands is reversed, the first pop-up number is op2
                    op2 = operand_stack.pop()
                    op1 = operand_stack.pop()
                                     # The value found should be pushed back to the operand stack
                                     # The function get_value used here is defined below
                    operand_stack.append(self.evaluator(top,op1,op2))
                                     # Pop the next top-of-stack operator
                    top = operator_stack.pop()
                     # When you encounter an operator, you must pop up and evaluate the stack with a priority of not lower than it.
            elif token in '+-*/':
                while operator_stack and pre_dict[operator_stack[-1]] >= pre_dict[token]:
                    top = operator_stack.pop()
                    op2 = operand_stack.pop()
                    op1 = operand_stack.pop()
                    operand_stack.append(self.evaluator(top,op1,op2))
                             # Don't forget to finally push the current operator onto the stack
                operator_stack.append(token)
             # After the expression traversal is completed, the remaining operators in the stack also require values
        while operator_stack:
            top = operator_stack.pop()
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            operand_stack.append(self.evaluator(top,op1,op2))
             # Finally, there is only one number left in the stack, this number is the final result of the entire expression
        return operand_stack[0]

    def evaluator(self, operator , op1 , op2 ):
        if operator == '+':
            return op1 + op2
        elif operator == '-':
            return op1 - op2
        elif operator == '*':
            return op1 * op2
        elif operator == '/':
            return op1 / op2
