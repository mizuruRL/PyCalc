import ast
import operator
import util.parser as parser
import util.ui as tui
import util.exceptions as pe

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
    try:
        expr = ui.show_input_space()
    except KeyboardInterrupt:
        ui.show_terminated()
        exit(0)
    if expr == "help":
        ui.show_help()
    elif expr == "quit":
        ui.show_terminated()
        exit(0)
    else:
        try:
            res = prsr.calc_expression(expr)
            print(">", res)
        except pe.InvalidExpressionException as e:
            ui.show_exception(e)
        except pe.InvalidElementException as e:
            ui.show_exception(e)
        except pe.InvalidSyntaxException as e:
            ui.show_exception(e)
        except pe.DivisionByZeroException as e:
            ui.show_exception(e)
