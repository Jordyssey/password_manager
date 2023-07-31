from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# choice, shuffle and randint should have random.choice etc. if we only had import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    le = letter_entry.get()
    ce = character_entry.get()
    ne = number_entry.get()

    if le == "":
        password_letters = [choice(letters) for i in range(randint(8, 10))]
    else:
        password_letters = [choice(letters) for i in range(int(le))]
    if ce == "":
        password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    else:
        password_symbols = [choice(symbols) for i in range(int(ce))]
    if ne == "":
        password_numbers = [choice(numbers) for i in range(randint(2, 4))]
    else:
        password_numbers = [choice(numbers) for i in range(int(ne))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    random_password = "".join(password_list)

    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website == "" or password == "" or password == "":
        messagebox.showwarning(title="Error", message="Some fields are empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            letter_entry.delete(0, END)
            character_entry.delete(0, END)
            number_entry.delete(0, END)
            messagebox.showinfo(title="Success", message="Your info has been saved successfully! ")


# ---------------------------- SEARCH ------------------------------- #
def search():
    search_website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data file not found")
    else:
        if search_website in data:
            messagebox.showinfo(title=f"{search_website}",
                                message=f"email: {data[search_website]['email']}"
                                        f"\n"f"password: {data[search_website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {search_website} exist.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=6)

# Entries
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()
# focus allows the user to start typing as soon as the launch the application, from the website entry.

email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "ephemeraljordan@gmail.com")

password_entry = Entry()
password_entry.grid(row=6, column=1, sticky="EW")

letter_label = Label(text="Letters:")
letter_label.grid(column=0, row=3)
letter_entry = Entry(width=10)
letter_entry.grid(column=1, row=3)

number_label = Label(text="Numbers:")
number_label.grid(column=0, row=5)
number_entry = Entry(width=10)
number_entry.grid(column=1, row=5)

character_label = Label(text="Characters:")
character_label.grid(column=0, row=4)
character_entry = Entry(width=10)
character_entry.grid(column=1, row=4)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=6)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, columnspan=2, row=7, sticky="EW")

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky="EW")

# sticky="EW" makes the entries and buttons to align perfectly instead of playing with width numbers
# to get it right
window.mainloop()
