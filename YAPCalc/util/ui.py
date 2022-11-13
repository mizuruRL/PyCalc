class UI:

    def show_title_screen(self):
        print('''       
         __     __      _____   _____      _      
         \\ \\   / //\\   |  __ \\ / ____|    | |     
          \\ \\_/ //  \\  | |__) | |     __ _| | ___ 
           \\   // /\\ \\ |  ___/| |    / _` | |/ __|
            | |/ ____ \\| |    | |___| (_| | | (__ 
            |_/_/    \\_\\_|     \\_____\\__,_|_|\\___|\n''')

    def show_description(self):
        print("Welcome to YAPCalc, an expression parser and calculator written in python.\nYou may enter an expression below, after the \">\" symbol.\n")

    def show_help_tip(self):
        print("Type help for information on what the calculator does and how to use it.")

    def show_quit_tip(self):
        print("Type quit or press CTRL+C to exit the program.")

    def show_input_space(self):
        try:
            return input("\n> ")
        except KeyboardInterrupt:
            self.show_terminated()
            exit(0)

    def show_terminated(self):
        print("Program Terminated.")

    def show_help(self):
        print('''\nYAPCalc Help

YAPCalc allows calculation of mathematical expressions with a mixture of the program's default supported operands.

**Supported math operations**
Addition (a+b)
Subtraction (a-b)
Division (a/b)
Multiplication (a*b)
Power (a**b)
Percentage (a%*b)

The calculator is also able to parse parenthesis priority.
You can mix and match different operands to create complex expressions, and the calculator will parse the request and solve it for you.
e.g.: > (1*4)+%50*100 => 54
''')
        self.show_quit_tip()

    def show_invalid_expression(self):
        print("Invalid Expression")