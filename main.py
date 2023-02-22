import flash_cards
from tkinter import *

TIMER = 3
FONT = "Ariel"
BG_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BG_COLOR)

flash_card = flash_cards.FlashCards()
lang = flash_card.lang

back_img = PhotoImage(file="images/card_back.png")
front_img = PhotoImage(file="images/card_front.png")


def get_card(img, title, text, fill, state):
    main_screen.itemconfig(card_image, image=img)
    main_screen.itemconfig(card_lang, text=title, fill=fill)
    main_screen.itemconfig(card_word, text=text, fill=fill)
    wrong_button.config(state=state)
    right_button.config(state=state)


def get_next_card():
    flash_card.get_random_words()
    lang_word = flash_card.foreign_lang
    get_card(front_img, lang, lang_word, "black", "disabled")
    window.after(TIMER * 1000, get_english_card)


def get_english_card():
    eng_word = flash_card.english_lang
    get_card(back_img, "English", eng_word, "white", "active")


def right_answer():
    flash_card.remove_words()
    get_next_card()


# Main Screen
main_screen = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
card_image = main_screen.create_image(400, 263)
card_lang = main_screen.create_text(400, 150, font=(FONT, 40, "italic"))
card_word = main_screen.create_text(400, 263, font=(FONT, 60, "bold"))
main_screen.grid(column=0, row=0, columnspan=2)

# Wrong Button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, bg=BG_COLOR, bd=0,
                      activebackground=BG_COLOR, command=get_next_card)
wrong_button.grid(column=0, row=1)

# Right Button
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, bg=BG_COLOR, bd=0,
                      activebackground=BG_COLOR, command=right_answer)
right_button.grid(column=1, row=1)

get_next_card()
window.mainloop()
