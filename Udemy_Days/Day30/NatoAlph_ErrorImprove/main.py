import pandas

data = pandas.read_csv("Udemy_Days\\Day30\\NatoAlph_ErrorImprove\\nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def code_word():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:    
        print("Sorry, only letters in the alphabet please.")
        code_word()
    else:
        print(output_list)
        
        
code_word()
