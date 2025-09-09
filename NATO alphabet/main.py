import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter : row.code for (idx, row) in data.iterrows()}

end = False

while not end:
    word = list(input("Enter a word: "))
    output = [data_dict[c.upper()] for c in word]
    print(output)
    repeat = input("Type in new word? (y/n): ")
    if repeat == "n":
        end = True
