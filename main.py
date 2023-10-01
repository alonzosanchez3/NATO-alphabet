import pandas

nato_alphabet_data = pandas.read_csv('nato_phonetic_alphabet.csv')
print(nato_alphabet_data)

nato_alphabet_dict = {
  row.letter: row.code for (index, row) in nato_alphabet_data.iterrows()
}

print(nato_alphabet_dict)

word = input("Enter a word: ")
letters = [x.capitalize() for x in word]
code = [nato_alphabet_dict[letter] for letter in letters if letter in nato_alphabet_dict]
print(code)