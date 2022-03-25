#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
real_names = []

with open("Mail Merge Project Start\\Input\\Letters\\starting_letter.txt") as letter:
    model_letter = letter.read()
    
with open ("Mail Merge Project Start\\Input\\Names\\invited_names.txt") as names:
    all_names = names.readlines()
    for i in all_names:
        real_names.append(i.replace("\n",""))
    for names in real_names:
        with open(f"Mail Merge Project Start\\Output\\ReadyToSend\\{names}.txt", 'x') as my_letters:
            my_letter = model_letter.replace("[name]", names)
            my_letters.write(my_letter)