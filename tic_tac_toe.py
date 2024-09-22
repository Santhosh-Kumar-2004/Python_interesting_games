import tkinter as tk
from tkinter import messagebox

# Initialize the global variables
turn = "X"
winner = None

def check_winner():
    global winner
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if buttons[i*3].cget("text") == buttons[i*3+1].cget("text") == buttons[i*3+2].cget("text") != "":
            winner = buttons[i*3].cget("text")
            return winner
        if buttons[i].cget("text") == buttons[i+3].cget("text") == buttons[i+6].cget("text") != "":
            winner = buttons[i].cget("text")
            return winner
    if buttons[0].cget("text") == buttons[4].cget("text") == buttons[8].cget("text") != "":
        winner = buttons[0].cget("text")
        return winner
    if buttons[2].cget("text") == buttons[4].cget("text") == buttons[6].cget("text") != "":
        winner = buttons[2].cget("text")
        return winner
    return None

def button_click(i):
    global turn, winner
    if buttons[i].cget("text") == "" and winner is None:
        buttons[i].config(text=turn)
        winner = check_winner()
        if winner:
            messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
        elif all(button.cget("text") != "" for button in buttons):
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        else:
            turn = "O" if turn == "X" else "X"

def reset_game():
    global turn, winner
    turn = "X"
    winner = None
    for button in buttons:
        button.config(text="")

# Set up the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons
buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=('Arial', 40), width=5, height=2,
                       command=lambda i=i: button_click(i))
    row = i // 3
    col = i % 3
    button.grid(row=row, column=col, padx=5, pady=5)
    buttons.append(button)

# Create Reset button
reset_button = tk.Button(root, text="Reset", font=('Arial', 20), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
