from tkinter  import *
from random import randint, choice, shuffle
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passw():    
    passw_entry.delete(0,END)
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [(choice(letters)) for _ in range(randint(8, 10))] #takes 8-10 letters from the letters list
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    
    shuffle(password_list)

    password = "".join(password_list)#join the letters of the list created:password_list
    passw_entry.insert(0,password) # put the pasword to the entry box in the UI
    pyperclip.copy(password) # the command that copy the passw in the clipboard and we can paste it anywhere we want
        

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    #get the text from the entry widgets
    web = website_entry.get()
    email = email_entry.get()
    passw = passw_entry.get()
    #it gives us a boolean value
    if len(web)==0 or len(passw)==0: #if the entries are empty
        messagebox.showwarning(title="Oops!",message="Don't leave any of the fields empty!")
    else:   
        is_ok = messagebox.askokcancel(title = web, message=f"This are the details entered:\n Email:{email}\nPassword:{passw}\nIs it ok to save?")
        if is_ok:        
            with open("Udemy_Days\\Day29\\passw_file.txt", "a") as passw_file:
                passw_file.write(f"{web} | {email} | {passw} \n")
                website_entry.delete(0,END)
                passw_entry.delete(0,END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Udemy_Days\\Day29\\logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row = 0, column=1)

#Labels
web_text = Label(text="Website:")
web_text.grid(row=1, column=0)
email_text = Label(text="Email/Username:")
email_text.grid(row=2, column=0)
pass_text = Label(text="Password:")
pass_text.grid(row=3, column=0)


#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus() #focus the cursor when the program lunches
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "fredadyrkaj@gmail.com")
passw_entry = Entry(width=21)
passw_entry.grid(row=3, column=1)

#Buttons
genpassw_butt = Button(text = "Generate Password", command = generate_passw)
genpassw_butt.grid(row=3, column=2)
add_butt = Button(text = "Add", width=36, command=save_password)
add_butt.grid(row=4, column=1, columnspan=2)


window.mainloop()
