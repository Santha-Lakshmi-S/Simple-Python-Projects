import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text="Generated Password: " + password)

# Function to save the username and password to a text file
def save_credentials():
    username = username_entry.get()
    password = password_label.cget("text").replace("Generated Password: ", "")
    with open("credentials.txt", "a") as file:
        file.write(f"Username: {username}, Password: {password}\n")
    username_entry.delete(0, "end")  # Clear the username field

# Create the main window
window = tk.Tk()
window.title("Password Generator and Saver")
window.geometry("400x300")
window.configure(bg='lightblue')

# Username Entry
username_label = tk.Label (window, text="Username:", bg='lightblue')
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

#Password Length Entry
length_label = tk.Label (window, text="Password Length:", bg='lightblue')
length_label.pack()
length_entry = tk.Entry (window)
length_entry.pack()

# Generate Password Button
generate_button= tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

#Display Generated Password
password_label = tk.Label (window, text=" ", bg='lightblue')
password_label.pack()

# Save Button
save_button = tk.Button(window, text="Click to Save", command=save_credentials)
save_button.pack()
window.mainloop()
