import random
import tkinter as tk
from PIL import Image, ImageTk

# Global variables
USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""
GAME_ACTIVE = True

# Function to convert choice to a number
def choice_to_number(choice):
    rps = {'scissor': 0, 'paper': 1, 'rock': 2}
    return rps[choice]

# Function to generate a random computer choice
def random_computer_choice():
    return random.choice(['scissor', 'paper', 'rock'])

# Function to determine the result
def result(human_choice, comp_choice):
    global USER_SCORE, COMP_SCORE, GAME_ACTIVE

    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)

    if user == comp:
        result_text = "It's a tie!"
    elif (user - comp) % 3 == 1:
        result_text = "You win!"
        USER_SCORE += 1
    else:
        result_text = "Computer wins!"
        COMP_SCORE += 1

    result_label.config(text=result_text)
    GAME_ACTIVE = False
    restart_button.config(state=tk.NORMAL)

# Create the main window
window = tk.Tk()
window.geometry("300x600")
window.title("Rock Paper Scissor ")

# Function to handle button clicks
def play(choice):
    global USER_CHOICE, COMP_CHOICE, GAME_ACTIVE
    if GAME_ACTIVE:
        USER_CHOICE = choice
        COMP_CHOICE = random_computer_choice()
        result(USER_CHOICE, COMP_CHOICE)

# Set up the UI elements
label_font = ('arial', 18, 'bold')
text_font = ('arial', 14)

label = tk.Label(text="Rock Paper Scissor", font=label_font, bg="lightgray")
label.pack(fill=tk.X, pady=10)

# Load and display an image
image = Image.open('img.jpg')
image = image.resize((160, 160))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(image=photo)
image_label.pack()

# Set background color
window.configure(bg="gray")

# Create buttons
choices = [ 'rock','paper','scissor']
buttons = []
for idx, choice in enumerate(choices):
    button = tk.Button(text=choice.capitalize(), bg="yellow", fg="black",
                       command=lambda c=choice: play(c), font=('arial', 15, 'bold'))
    buttons.append(button)
    button.pack(fill=tk.X, padx=20, pady=5)

# Create a result label
result_label = tk.Label(window, text="", font=text_font)
result_label.pack(fill=tk.X, padx=20, pady=10)

# Function to restart the game
def restart_game():
    global USER_SCORE, COMP_SCORE, GAME_ACTIVE
    USER_SCORE = 0
    COMP_SCORE = 0
    result_label.config(text="")
    restart_button.config(state=tk.DISABLED)
    GAME_ACTIVE = True

# Create the restart button
restart_button = tk.Button(text="Restart", bg="red", fg="yellow",
                           command=restart_game, font=('arial', 15, 'bold'))
restart_button.pack(fill=tk.X, padx=20, pady=10)
restart_button.config(state=tk.DISABLED)

# Run the main loop
window.mainloop()
