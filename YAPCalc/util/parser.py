import ast
from math import sqrt
import string
import re
import util.exceptions as pe

class Parser:

    def __init__(self, ops):
        self.ops = ops
        
    def calc_expression(self, expression):
        pexpression = self.prep_expression(expression)
        try:
            parsed_expression = ast.parse(pexpression, mode = 'eval')
        except SyntaxError:
            raise pe.InvalidSyntaxException()
        return self.calc_node(parsed_expression.body)

    def calc_node(self, node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return self.ops[type(node.op)](self.calc_node(node.left), self.calc_node(node.right))
        elif isinstance(node, ast.UnaryOp):
            return self.ops[type(node.op)](self.calc_node(node.operand))
        elif isinstance(node, ast.Name):
            raise pe.InvalidElementException(str(node.id))
        else:
            raise pe.InvalidSyntaxException()
    
    def prep_expression(self, expression):
        pexpression = expression.translate({ord(c): None for c in string.whitespace})
        if "%" in pexpression:
            tokens = r"([+*/%-])"
            tokexpr = re.split(tokens, pexpression)
            self.parse_percent(tokexpr)
            pexpression = ''.join(tokexpr)
        if "sqrt" in pexpression:
            tokens = r"(sqrt)"
            tokexpr = re.split(tokens, pexpression)   
            self.parse_sqrt(tokexpr)
            pexpression = ''.join(tokexpr)
        return pexpression

    def parse_percent(self, tokexpr):
        while "%" in tokexpr:
            perc_index = tokexpr.index("%")
            if tokexpr[perc_index - 1] == '':
                try:
                    tokexpr[perc_index + 1] = str(float(tokexpr[perc_index + 1]) * 0.01)
                    tokexpr.pop(perc_index)
                except ValueError:
                    raise pe.InvalidExpressionException(''.join(tokexpr[perc_index:]))        
            else:
                raise pe.InvalidExpressionException(''.join(tokexpr[perc_index:]))

    def parse_sqrt(self, tokexpr):
        while "sqrt" in tokexpr:
            sqrt_index = tokexpr.index("sqrt")
            try:
                tokexpr[sqrt_index + 1] = str(sqrt(float(tokexpr[sqrt_index + 1])))
                tokexpr.pop(sqrt_index)
            except ValueError:
                raise pe.InvalidExpressionException(''.join(tokexpr[sqrt_index:])) 