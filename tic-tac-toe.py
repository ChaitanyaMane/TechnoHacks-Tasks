import tkinter as tk
import random


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

        self.buttons = [[None]*3 for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(root, text=" ", font=("Helvetica", 24), height=2, width=5,
                                                   command=lambda r=row, c=col: self.make_move(r, c))
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner(self.current_player):
                self.display_winner(self.current_player)
            elif self.is_board_full():
                self.display_draw()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.computer_move()

    def computer_move(self):
        empty_cells = self.get_empty_cells()
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_move(row, col)

    def get_empty_cells(self):
        return [(row, col) for row in range(3) for col in range(3) if self.board[row][col] == " "]

    def check_winner(self, player):
        for row in self.board:
            if all([cell == player for cell in row]):
                return True
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True
        if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2 - i] == player for i in range(3)]):
            return True
        return False

    def is_board_full(self):
        return all([cell != " " for row in self.board for cell in row])

    def display_winner(self, player):
        winner_label = tk.Label(
            self.root, text=f"{player} wins!", font=("Helvetica", 16))
        winner_label.grid(row=3, columnspan=3)
        self.disable_buttons()
        self.add_restart_button()

    def display_draw(self):
        draw_label = tk.Label(
            self.root, text="It's a draw!", font=("Helvetica", 16))
        draw_label.grid(row=3, columnspan=3)
        self.disable_buttons()
        self.add_restart_button()

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

    def add_restart_button(self):
        restart_button = tk.Button(self.root, text="Restart", font=(
            "Helvetica", 14), command=self.restart_game)
        restart_button.grid(row=4, columnspan=3)

    def restart_game(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = " "
                self.buttons[row][col].config(text=" ", state="normal")
        self.current_player = "X"
        self.clear_labels()

    def clear_labels(self):
        for child in self.root.winfo_children():
            if isinstance(child, tk.Label):
                child.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
    
