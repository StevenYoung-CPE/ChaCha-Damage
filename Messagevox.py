import tkinter as tk
from tkinter import messagebox, simpledialog
class Calculator:
    def __init__(self):
        self.PS = ''
        self.dice = 0
        self.Smult = 1
        self.Emult = 1
        self.cmult = 1
        self.mmult = 1
        self.Aup = 0
        self.Dup = 0

# Function to input a variable and display it
def input_variable():
    # Prompt the user for input
    user_input = simpledialog.askstring("Input Required", "Enter a value:")
    if user_input:  # Check if the user entered something
        messagebox.showinfo("Input Received", f"You entered: {user_input}")
    else:
        messagebox.showinfo("Input Received", "No input was provided.")

# Exit function
def exit_program():
    root.destroy()

# Create the main menu template
def create_menu():
    Calculator()
    global root
    root = tk.Tk()
    root.title("Mouse Navigable Menu with Input")
    root.geometry("400x300")  # Set the size of the window

    # Create a label for the title
    title_label = tk.Label(root, text="Main Menu", font=("Arial", 16, "bold"))
    title_label.pack(pady=20)

    # Add buttons to the menu
    input_button = tk.Button(root, text="Enter a Variable", font=("Arial", 12), command=input_variable)
    input_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=exit_program)
    exit_button.pack(pady=10)

    # Start the main event loop
    root.mainloop()

# Run the menu
if __name__ == "__main__":
    create_menu()
