import tkinter as tk
import random

def move_button(event):
    # Get the dimensions of the window
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    
    # Define the button size
    button_width = moving_button.winfo_width()
    button_height = moving_button.winfo_height()
    
    # Calculate random position within the window bounds
    x = random.randint(0, window_width - button_width)
    y = random.randint(0, window_height - button_height)
    
    # Move the button to the new position
    moving_button.place(x=x, y=y)

# Create the main window
root = tk.Tk()
root.title("Gay Test")
root.geometry("500x400")  # Set the window size

# Create a label
label = tk.Label(root, text="Are you GAY !?")
label.pack(pady=10)

# Create a button that will move
moving_button = tk.Button(root, text="No")
moving_button.place(x=50, y=50)  # Initial position

# Bind the hover event to the move_button function
moving_button.bind("<Enter>", move_button)

# Create a stationary button
stationary_button = tk.Button(root, text="Yes")
stationary_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()