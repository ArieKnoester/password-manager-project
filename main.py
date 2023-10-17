from tkinter import *
DEFAULT_USERNAME = ""


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    with open("data.txt", mode="a") as file:
        file.write(f"{website} | {username} | {password}\n")

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=logo_image, anchor="center")
canvas.grid(row=0, column=1)

# Labels
site_label = Label(text="Website:")
site_label.grid(row=1, column=0, pady=5)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0, pady=5)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, pady=5)

# Entries
website_entry = Entry()
website_entry.grid(row=1, column=1, padx=(5, 0), pady=5, columnspan=2, sticky="EW")
website_entry.focus()
username_entry = Entry()
username_entry.insert(INSERT, DEFAULT_USERNAME)
username_entry.grid(row=2, column=1, padx=(5, 0), pady=5, columnspan=2, sticky="EW")
password_entry = Entry(width=31)
password_entry.grid(row=3, column=1, padx=(5, 0), pady=5, sticky="W")

# Buttons
generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Add", command=add_password)
add_button.grid(row=4, column=1, padx=(5, 0), pady=(5, 0), columnspan=2, sticky="EW")

window.mainloop()
