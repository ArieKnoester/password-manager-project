import tkinter as tk
from tkinter import messagebox
import random
import json
import pyperclip
import character_lists

DEFAULT_USERNAME = ""  # Set your default username here.


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.config(padx=50, pady=50)
        self.canvas = tk.Canvas(width=200, height=200)
        self.logo_image = tk.PhotoImage(file="logo.png")
        self.canvas.create_image(120, 100, image=self.logo_image, anchor="center")
        self.canvas.grid(row=0, column=1)

        # Labels
        self.site_label = tk.Label(text="Website:")
        self.site_label.grid(row=1, column=0, pady=5)
        self.username_label = tk.Label(text="Email/Username:")
        self.username_label.grid(row=2, column=0, pady=5)
        self.password_label = tk.Label(text="Password:")
        self.password_label.grid(row=3, column=0, pady=5)

        # Entries
        self.website_entry = tk.Entry(width=31)
        self.website_entry.grid(row=1, column=1, padx=(5, 0), pady=5, sticky="W")
        self.website_entry.focus()
        self.username_entry = tk.Entry()
        self.username_entry.insert(tk.INSERT, DEFAULT_USERNAME)
        self.username_entry.grid(row=2, column=1, padx=(5, 0), pady=5, columnspan=2, sticky="EW")
        self.password_entry = tk.Entry(width=31)
        self.password_entry.grid(row=3, column=1, padx=(5, 0), pady=5, sticky="W")

        # Buttons
        self.search_button = tk.Button(text="Search", width=15, command=self.find_password)
        self.search_button.grid(row=1, column=2)
        self.generate_button = tk.Button(text="Generate Password", width=15, command=self.generate_password)
        self.generate_button.grid(row=3, column=2, sticky="EW")
        self.add_button = tk.Button(text="Add", command=self.add_password)
        self.add_button.grid(row=4, column=1, padx=(5, 0), pady=(5, 0), columnspan=2, sticky="EW")

    def generate_password(self):
        # initialize the field.
        self.password_entry.delete(0, tk.END)

        num_letters = random.randint(8, 10)
        num_symbols = random.randint(2, 4)
        num_numbers = random.randint(2, 4)

        password_list = [random.choice(character_lists.LETTERS) for _ in range(num_letters)]
        password_list += [random.choice(character_lists.NUMBERS) for _ in range(num_numbers)]
        password_list += [random.choice(character_lists.SYMBOLS) for _ in range(num_symbols)]
        random.shuffle(password_list)

        password_string = "".join(password_list)
        self.password_entry.insert(index=0, string=password_string)
        pyperclip.copy(password_string)

    def add_password(self):
        website = self.website_entry.get().lower()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not website or not username or not password:
            messagebox.showerror(
                title="Error",
                message="Please fill in all fields."
            )
        else:
            new_data = {
                website:
                    {
                        "username": username,
                        "password": password
                    }
            }
            try:
                file = open("data.json", mode="r")
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                file_data = json.load(file)
                file_data.update(new_data)
                file.close()

                with open("data.json", mode="w") as file:
                    json.dump(file_data, file, indent=4)

            self.website_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.website_entry.focus()

    def find_password(self):
        website = self.website_entry.get().lower()
        try:
            file = open("data.json", mode="r")
        except FileNotFoundError:
            messagebox.showerror(
                title="Error",
                message="Data file not found or has not been created.\n\n"
                        "You're likely receiving this error if you have not saved"
                        " any credentials yet."
            )
        else:
            file_data = json.load(file)
            file.close()
            credentials = file_data.get(website)
            if not credentials:
                messagebox.showinfo(
                    title="Not found.",
                    message=f"No credentials for '{website}' was found.\n\n"
                            "You may not have saved credentials for this website"
                            " or have misspelled it."
                )
            else:
                website = website.title()
                username = credentials["username"]
                password = credentials["password"]
                pyperclip.copy(password)
                messagebox.showinfo(
                    title=website,
                    message=f"Your password has been copied to your clipboard.\n\n"
                            f"Username: {username}\n"
                            f"Password: {password}"
                )
