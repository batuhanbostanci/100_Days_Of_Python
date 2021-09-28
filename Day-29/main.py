from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
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

# ---------------------------- SAVE PASSWORD ------------------------------- #


def write():
    website = input_website.get()
    username = input_email_username.get()
    password = input_pass.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{username} "
                                                              f"\n Password:{password}")
        if is_ok:
            with open("password_data.txt", "a") as file:
                file.write(f"{website} | {username} | {password} \n")
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

input_website = Entry(width=35)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()

input_email_username = Entry(width=35)
input_email_username.grid(row=2, column=1, columnspan=2)
input_email_username.insert(0, "batu@hotmail.com")

input_pass = Entry(width=21)
input_pass.grid(row=3, column=1)

# Buttons
generate_pass_button = Button(text="Generate Password", command=generate_password, width=14)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=write)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()