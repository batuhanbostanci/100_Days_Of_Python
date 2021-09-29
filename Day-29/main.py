from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_symbols + pass_numbers

    shuffle(password_list)
    password = "".join(password_list)
    input_pass.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = input_website.get()
    try:
        with open("password_data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]

            messagebox.showinfo(title=website, message=f"Email:{email}\n Password:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def write():
    website = input_website.get()
    username = input_email_username.get()
    password = input_pass.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        try:
            with open("password_data.json", "r") as file:
                # Read old data
                data = json.load(file)
        except FileNotFoundError:
            with open("password_data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data
            data.update(new_data)

            with open("password_data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)  # insert the data into json file
        finally:
            input_website.delete(0, END)
            input_pass.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels

label_1 = Label(text="Website")
label_1.grid(column=0, row=1)

label_2 = Label(text="Email/Username:")
label_2.grid(column=0, row=2)

label_3 = Label(text="Password:")
label_3.grid(column=0, row=3)

# Entries

input_website = Entry(width=21)
input_website.grid(row=1, column=1)
input_website.focus()

input_email_username = Entry(width=35)
input_email_username.grid(row=2, column=1, columnspan=2)
input_email_username.insert(0, "batu@hotmail.com")

input_pass = Entry(width=21)
input_pass.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", command=find_password, width=14)
search_button.grid(row=1, column=2)
generate_pass_button = Button(text="Generate Password", command=generate_password, width=14)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=write)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()