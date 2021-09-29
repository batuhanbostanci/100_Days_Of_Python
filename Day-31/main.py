from tkinter import *
import pandas as pd
import random
import time


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data = {}
try:
    data = pd.read_csv("data/learned.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    data = pd.DataFrame(data)
    data_dict = data.to_dict(orient="records")
else:
    data = pd.DataFrame(data)
    data_dict = data.to_dict(orient="records")


def is_known():
    data_dict.remove(current_card)
    next_card()

    will_learned_data = pd.DataFrame(data_dict)
    will_learned_data.to_csv("data/learned_words.csv", index=False)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    background_canvas_green.itemconfig(card_title, text="French", fill="black")
    background_canvas_green.itemconfig(card_word, text=current_card["French"], fill="black")
    background_canvas_green.itemconfig(card_color, image=background_image_green)
    flip_timer = window.after(3000, flap_cards)


def flap_cards():
    background_canvas_green.itemconfig(card_color, image=background_image_white)
    background_canvas_green.itemconfig(card_title, text="English", fill="white")
    background_canvas_green.itemconfig(card_word, text=current_card["English"], fill="white")


# Window

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flap_cards)
# Images

background_image_green = PhotoImage(file="images/card_front.png")
background_image_white = PhotoImage(file="images/card_back.png")
wrong_canvas_image = PhotoImage(file="images/wrong.png")
right_canvas_image = PhotoImage(file="images/right.png")


# Canvas

background_canvas_green = Canvas(width=800, height=526, highlightthickness=0)
card_color = background_canvas_green.create_image(400, 268, image=background_image_green)
background_canvas_green.config(bg=BACKGROUND_COLOR)
background_canvas_green.grid(row=0, column=0, columnspan=2)
card_word = background_canvas_green.create_text(400, 250, text="Title", font=("Ariel", 40, "italic"))
card_title = background_canvas_green.create_text(400, 163, text="Word", font=("Ariel", 40, "bold"))

# Buttons
wrong_canvas_button = Button(width=100, height=100, command=next_card, image=wrong_canvas_image, highlightthickness=0)
wrong_canvas_button.grid(row=1, column=0)

right_canvas_button = Button(width=100, height=100, command=is_known, image=right_canvas_image, highlightthickness=0)
right_canvas_button.grid(row=1, column=1)

next_card()
window.mainloop()