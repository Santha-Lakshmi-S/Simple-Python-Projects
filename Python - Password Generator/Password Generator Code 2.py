import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text="Generated Password: " + password)

def save_credentials():
    username = username_entry.get()
    password = password_label.cget("text").replace("Generated Password: ", "")
    with open("credentials.txt", "a") as file:
        file.write(f"Username: {username}, Password: {password}\n")
    username_entry.delete(0, "end")
    messagebox.showinfo("Saved", "Credentials saved successfully!")

# Create a window
window = tk.Tk()

# Create and set up widgets
length_label = tk.Label(window, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(window)
length_entry.pack(pady=10)

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(window, text="Generated Password: ")
password_label.pack(pady=10)

username_label = tk.Label(window, text="Username:")
username_label.pack(pady=10)

username_entry = tk.Entry(window)
username_entry.pack(pady=10)

save_button = tk.Button(window, text="Save Credentials", command=save_credentials)
save_button.pack(pady=10)

# Start the main loop
window.mainloop()
