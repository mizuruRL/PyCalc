import ast
import operator

class Parser:

    def __init__(self, ops = {
        ast.Add: operator.add, 
        ast.Sub: operator.sub, 
        ast.Mult: operator.mul, 
        ast.Div: operator.truediv, 
        ast.Pow: operator.pow,
    }):
        self.ops = ops
        
    def calc_expression(self, expression):
        return self.calc_node(ast.parse(expression, mode = 'eval').body)

    def calc_node(self, node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return self.ops[type(node.op)](self.calc_node(node.left), self.calc_node(node.right))
        elif isinstance(node, ast.UnaryOp):
            return self.ops[type(node.op)](self.calc_node(node.operand))