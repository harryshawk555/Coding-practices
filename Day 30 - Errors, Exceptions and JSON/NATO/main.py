# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
PATH = f"./Day 30 - Errors, Exceptions and JSON/NATO/nato_phonetic_alphabet.csv"
import pandas

data = pandas.read_csv(PATH)

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def gen_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only characters in the alphabet please")
        gen_phonetic()
    else:
        print(output_list)

gen_phonetic()
