import pandas as pd

nato_alphabet_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_data_frame.iterrows()}

user_input = input("Write your word\n").upper()

result_list = [nato_alphabet_dict[letter] for letter in user_input]

print(result_list)
