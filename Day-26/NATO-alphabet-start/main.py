import pandas as pd

nato_alphabet_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_data_frame.iterrows()}


def nato_alphabet_generator():
    try:
        user_input = input("Write your word\n").upper()
        result_list = [nato_alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Please write only letters!!")
        nato_alphabet_generator()
    else:
        print(result_list)


nato_alphabet_generator()

