import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
dict_data = {row.letter:row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# p_list = list(dict_data.values())
# print(p_list)
user_input = str(input("Please say your name: ")).upper()
# word = [value for value in user_input ]
# print(word)
list_phonetic = [dict_data[letter] for letter in user_input]
print(list_phonetic)