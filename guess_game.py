import random
import tkinter as tk
from tkinter import messagebox

def check_guess():
    global attempts, random_number
    try:
        guess = int(entry.get())
        attempts += 1

        if guess < random_number:
            feedback_label.config(text="Too low! Try again.")
        elif guess > random_number:
            feedback_label.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed the number {random_number} in {attempts} attempts.")
            reset_game()
    except ValueError:
        feedback_label.config(text="Invalid input. Please enter an integer.")

def reset_game():
    global attempts, random_number
    attempts = 0
    random_number = random.randint(1, 100)
    feedback_label.config(text="I have generated a new number. Start guessing!")
    entry.delete(0, tk.END)

# Initialize random variables
random_number = random.randint(1, 100)
attempts = 0

# Create the main window
root = tk.Tk()
root.title("Guessing Game")

# Create and place widgets
instructions_label = tk.Label(root, text="I have generated a random number between 1 and 100. Can you guess it?")
instructions_label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit Guess", command=check_guess)
submit_button.pack(pady=5)

feedback_label = tk.Label(root, text="Start guessing!")
feedback_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
