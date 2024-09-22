import tkinter as tk
from tkinter import Toplevel
import random

# Function to create a new popup window
def open_popup():
    # Create a new top-level window
    popup = Toplevel()
    popup.title("Congratulations")
    
    # Set the size of the new window
    popup.geometry("250x150")
    
    # Add a label to the popup window
    label = tk.Label(popup, text="Thank You So much...")
    label.pack(pady=20)
    
    # Add a button to close the popup window
    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack()

def move_button(event):
    # Get the dimensions of the window
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    
    # Define the button size
    button_width = negative_btn.winfo_width()
    button_height = negative_btn.winfo_height()
    
    # Calculate random position within the window bounds
    x = random.randint(0, window_width - button_width)
    y = random.randint(0, window_height - button_height)
    
    # Move the button to the new position
    negative_btn.place(x=x, y=y)

# Create the main window
root = tk.Tk()
root.title("Love me plzz")
root.geometry("500x400")  # Set the window size

# Create a label
label = tk.Label(root, text="I Like You, Do You Like Me!?!")
label.pack(pady=10)

# Create a button that will move
negative_btn = tk.Button(root, text="No")
negative_btn.place(x=50, y=50)  # Initial position

# Bind the hover event to the move_button function
negative_btn.bind("<Enter>", move_button)

# Create a stationary button
positive_btn = tk.Button(root, text="Yes", command=open_popup)
positive_btn.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
