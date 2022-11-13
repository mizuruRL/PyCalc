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
ui = tui.UI()

ui.show_title_screen()
ui.show_description()
ui.show_help_tip()
ui.show_quit_tip()

while True:
    expr = ui.show_input_space()
    if expr == "help":
        ui.show_help()
    elif expr == "quit":
        ui.show_terminated()
        exit(0)
    else:
        try:
            pexpr = prsr.prep_expression(expr)
            print(">", prsr.calc_expression(pexpr))
        except TypeError:
            ui.show_invalid_expression()
        except SyntaxError:
            ui.show_invalid_expression()
        
