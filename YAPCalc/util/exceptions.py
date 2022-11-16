class InvalidExpressionException(Exception):
    def __init__(self, expr):
        Exception.__init__(self, f'Invalid expression starting from {expr}')

class InvalidElementException(Exception):
    def __init__(self, elem):
        Exception.__init__(self, f'Invalid element on expression: {elem}')

class InvalidSyntaxException(Exception):
    def __init__(self):
        Exception.__init__(self, f'Invalid syntax on expression')

class DivisionByZeroException(Exception):
    def __init__(self):
        Exception.__init__(self, f'Zero division')