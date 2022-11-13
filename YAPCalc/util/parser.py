import ast
import string
import re

class Parser:

    def __init__(self, ops):
        self.ops = ops
        
    def calc_expression(self, expression):
        pexpression = self.prep_expression(expression)
        parsed_expression = ast.parse(pexpression, mode = 'eval')
        return self.calc_node(parsed_expression.body)

    def calc_node(self, node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return self.ops[type(node.op)](self.calc_node(node.left), self.calc_node(node.right))
        elif isinstance(node, ast.UnaryOp):
            return self.ops[type(node.op)](self.calc_node(node.operand))
        else:
            raise TypeError
    
    def prep_expression(self, expression):
        pexpression = expression.translate({ord(c): None for c in string.whitespace})
        if "%" in pexpression:
            tokens = r"([+*/%-])"
            tokexpr = re.split(tokens, pexpression)
            for i in range(len(tokexpr) - 1):
                if tokexpr[i] == "%" and self.is_float(tokexpr[i+1]):
                    print(tokexpr[i])
                    tokexpr[i+1] = str(float(tokexpr[i+1]) * 0.01)
                    tokexpr.pop(i)
            pexpression = ''.join(tokexpr)
        return pexpression

    def is_float(self, str):
        try:
            float(str)
            return True
        except ValueError:
            return False

