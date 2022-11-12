import ast
import operator
import util.parser as parser
import util.ui as tui

ops = {
        ast.Add: operator.add, 
        ast.Sub: operator.sub, 
        ast.Mult: operator.mul, 
        ast.Div: operator.truediv, 
        ast.Pow: operator.pow,
    }
prsr = parser.Parser(ops)
expr = "0"
ui = tui.UI()

ui.show_title_screen()
ui.show_description()
expr = ui.show_input_space()