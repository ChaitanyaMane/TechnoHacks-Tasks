import random
import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = ["X", "O"]
        self.current_turn = 0

        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(root, text=" ", font=("Helvetica", 24), height=2, width=5,
                                   command=lambda row=row, col=col: self.on_button_click(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def on_button_click(self, row, col):
        if self.board[row][col] == " " and self.players[self.current_turn] == "X":
            self.board[row][col] = "X"
            self.buttons[row][col].config(text="X", state=tk.DISABLED)
            self.current_turn = 1 - self.current_turn
            self.check_game_status()

            if not self.check_winner("X") and not self.is_board_full():
                self.computer_move()

    def computer_move(self):
        empty_cells = self.get_empty_cells()
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O", state=tk.DISABLED)
            self.current_turn = 1 - self.current_turn
            self.check_game_status()

    def check_winner(self, player):
        for row in self.board:
            if all([cell == player for cell in row]):
                return True
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True
        if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2-i] == player for i in range(3)]):
            return True
        return False

    def is_board_full(self):
        return all([cell != " " for row in self.board for cell in row])

    def get_empty_cells(self):
        empty_cells = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    empty_cells.append((row, col))
        return empty_cells

    def check_game_status(self):
        if self.check_winner("X"):
            self.show_winner_message("X")
        elif self.check_winner("O"):
            self.show_winner_message("O")
        elif self.is_board_full():
            self.show_draw_message()

    def show_winner_message(self, player):
        messagebox.showinfo("Game Over", f"Player {player} wins!")
        self.reset_board()

    def show_draw_message(self):
        messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_board()

    def reset_board(self):
        for row in self.buttons:
            for button in row:
                button.config(text=" ", state=tk.NORMAL)
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_turn = 0

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
