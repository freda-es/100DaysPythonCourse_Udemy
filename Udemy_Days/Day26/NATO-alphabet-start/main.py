#how to create a list that code the name inputed from the user with the NATO CODE

import pandas

data_alph = pandas.read_csv("Udemy_Days\\Day26\\NATO-alphabet-start\\nato_phonetic_alphabet.csv")
code_dic = {row.letter:row.code for (index, row) in data_alph.iterrows()}

name_input = input("insert the word to nato code it:").upper()
# my_list=[]
# for lett in name_input:
#     new_list = [value for (key,value) in code_dic.items() if key == lett.upper()]
#     my_list.append(new_list[0])

new_list = [code_dic[letter] for  letter in name_input]
print(new_list)
    
