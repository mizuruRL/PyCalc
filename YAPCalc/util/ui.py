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

    def show_input_space(self):
        try:
            return input("> ")
        except KeyboardInterrupt:
            print("\nProgram Terminated.")