# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)



def equalpress():

    try:
        global expression


        total = str(eval(expression))

        equation.set(total)


        expression = ""


    except:
        equation.set(" error ")
        expression = ""


# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="grey")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("300x418")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression.
    expression_field = Entry(gui, textvariable=equation, font=("Arial", 20), bd=10, insertwidth=7, width=17)
    expression_field.grid(row=0, column=0, columnspan=4)

    # create a Buttons and place at a particular
    # location inside the root window.
    # when the user presses the button, the command or
    # function affiliated to that button is executed.
    buttons = [
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
        ('0', 5, 0), ('.', 5, 1), ('+', 5, 3),
    ]

    for (text, row, col) in buttons:
        button = Button(gui, text=text, fg='white', bg='black', font=("Arial", 15),
                        command=lambda num=text: press(num), height=2, width=5)
        button.grid(row=row, column=col, padx=5, pady=5)

    clear_button = Button(gui, text='Clear', fg='white', bg='red', font=("Arial", 15),
                          command=clear, height=2, width=5)
    clear_button.grid(row=1, column=3, padx=5, pady=5)

    equal_button = Button(gui, text='=', fg='white', bg='orange', font=("Arial", 15),
                          command=equalpress, height=2, width=5)
    equal_button.grid(row=5, column=2, padx=5, pady=5)

    # start the GUI
    gui.mainloop()
