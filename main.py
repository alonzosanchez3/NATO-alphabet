import pandas

nato_alphabet_data = pandas.read_csv('nato_phonetic_alphabet.csv')
print(nato_alphabet_data)

nato_alphabet_dict = {
  row.letter: row.code for (index, row) in nato_alphabet_data.iterrows()
}

print(nato_alphabet_dict)

def generate_phonetic():

  word = input("Enter a word: ")
  letters = [x.capitalize() for x in word]
  try:
    code = [nato_alphabet_dict[letter] for letter in letters if letter in nato_alphabet_dict]
  except KeyError:
    print('Sorry only letters in the alphabet')
    generate_phonetic()
  else:
    print(code)
generate_phonetic()



# import tkinter

# window = tkinter.Tk()
# my_label = tkinter.Label(text="Hi how are you")
# my_label.pack()
# window.mainloop()