from tkinter  import *
from random import randint, choice, shuffle
from tkinter import messagebox
import pyperclip
import json

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
    #create a dict to format the data entries in a json file
    new_data = {
        web: {
            "email":email,
             "passw":passw,           
        }
    }
    #it gives us a boolean value
    if len(web)==0 or len(passw)==0: #if the entries are empty
        messagebox.showwarning(title="Oops!",message="Don't leave any of the fields empty!")
    else: 
        try:
            with open("Udemy_Days\\Day30\\PasswGenerator_Json\\passw_file.json", "r") as passw_file:
                #Read old data
                data_file = json.load(passw_file)#it takes the data and convert it in a normal python Dict, data_file is a dict
                
        except FileNotFoundError:
            with open("Udemy_Days\\Day30\\PasswGenerator_Json\\passw_file.json", "w") as passw_file:
                #Saving update data
                json.dump(new_data,passw_file, indent=4)#take the data_file where we saved the new_data and write it in passw_file.json, indent to make it more understable
        else:
            # update old data with the new data we enter
            data_file.update(new_data)
            with open("Udemy_Days\\Day30\\PasswGenerator_Json\\passw_file.json", "w") as passw_file:
                json.dump(data_file,passw_file, indent=4)
        
        finally:           
            website_entry.delete(0,END)
            passw_entry.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    web = website_entry.get()
    try:
        with open("Udemy_Days\\Day30\\PasswGenerator_Json\\passw_file.json", "r") as passw_file:
            data_file = json.load(passw_file) 
    except FileNotFoundError:
        messagebox.showerror (title="Error",message="No Data File Found!")
    else:
        for key in data_file:
            if key == web:
                messagebox.showinfo (title=f"{key}",message=f"Email: {data_file[key]['email']} \nPassword: {data_file[key]['passw']}")
            else:
                messagebox.showerror (title=f"{key}",message=f"No details for the website exists!")
       
        
                
        


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
website_entry = Entry(width=31)
website_entry.grid(row=1,column=1, columnspan=2, sticky='w')
website_entry.focus() #focus the cursor when the program lunches
email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2, sticky='w')
email_entry.insert(0, "fredadyrkaj@gmail.com")
passw_entry = Entry(width=31)
passw_entry.grid(row=3, column=1,sticky='w')

#Buttons
genpassw_butt = Button(text = "Generate Password", width = 15,command = generate_passw)
genpassw_butt.grid(row=3, column=2, sticky='w')
add_butt = Button(text = "Add", width=44, command=save_password)
add_butt.grid(row=4, column=1, columnspan=2, sticky='w')
search_butt = Button(text = "Search", width = 15, command=find_password)
search_butt.grid(row=1, column=2, sticky='w')


window.mainloop()
