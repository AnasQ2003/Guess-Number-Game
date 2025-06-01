import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("400x500")
root.configure(bg="#2C3E50")

number_to_guess = random.randint(1, 100)
attempts_left = 10

def check_guess():
    global attempts_left
    try:
        guess = int(entry.get())
        if guess < 1 or guess > 100:
            messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 100")
            return

        attempts_left -= 1
        if guess == number_to_guess:
            messagebox.showinfo("Congratulations!", "You guessed the correct number!")
            reset_game()
        elif attempts_left == 0:
            messagebox.showerror("Game Over", f"No attempts left! The number was {number_to_guess}")
            reset_game()
        elif guess < number_to_guess:
            status_label.config(text=f"Too low! Attempts left: {attempts_left}")
        else:
            status_label.config(text=f"Too high! Attempts left: {attempts_left}")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number")

def reset_game():
    global number_to_guess, attempts_left
    number_to_guess = random.randint(1, 100)
    attempts_left = 10
    entry.delete(0, tk.END)
    status_label.config(text="Guess a number between 1 and 100")

tk.Label(root, text="Guess the Number!", font=("Arial", 24, "bold"), bg="#2C3E50", fg="white").pack(pady=20)

tk.Label(root, text="Enter a number (1-100):", font=("Arial", 14), bg="#2C3E50", fg="white").pack()
entry = tk.Entry(root, font=("Arial", 14), width=10, justify='center')
entry.pack(pady=10)

check_button = tk.Button(root, text="Check", font=("Arial", 14), bg="#27AE60", fg="white", width=10,
                         command=check_guess)
check_button.pack(pady=10)

status_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14), bg="#2C3E50", fg="white")
status_label.pack(pady=20)

reset_button = tk.Button(root, text="Restart Game", font=("Arial", 14), bg="#E74C3C", fg="white", width=15,
                         command=reset_game)
reset_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", font=("Arial", 14), bg="#3498DB", fg="white", width=10, command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
