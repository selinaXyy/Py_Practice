from tkinter import *
from tkinter import messagebox #not a class
from random import *
import pyperclip
import json

DEFAULT_EMAIL = "yiyangxue.xyy@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#referenced from the password generator project
def generate_password():
    #clears previous entry
    entry_password.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #list comprehension
    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list) #used on strings

    #insert into password entry
    entry_password.insert(0, password)
    #copy to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = entry_website.get().title()
    email_username = entry_email_username.get()
    password = entry_password.get()
    #nested dict
    new_data = {
        website:{
        "email/username": email_username,
        "password": password,
        }
    }

    #save data
    valid_info = check_validation(website, email_username, password)
    if valid_info:
        user_response = confirm_info_popup(website, email_username, password)
        if user_response:
            try:
                #read existing data
                with open("./data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError: 
                #create json file (first entry)
                with open("./data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)#write data
            else: #if try block succeed
                #update data in json format
                with open("./data.json", mode="w") as data_file:
                    data.update(new_data) 
                    json.dump(data, data_file, indent=4) #write data

            data_saved_popup()
            clear_entries()

def check_validation(website_par, email_username_par, password_par):
    valid = True
    if website_par == "":
        messagebox.showwarning(title="Invalid Website", message="Your website entry is empty")
        valid = False
    if email_username_par == "":
        messagebox.showwarning(title="Invalid Email/Username", message="Your email/username entry is empty")
        valid = False
    if password_par == "":
        messagebox.showwarning(title="Invalid Password", message="Your password entry is empty")
        valid = False
    return valid


def clear_entries():
    entry_website.delete(0, END) #delete from the 0th index to the END
    entry_password.delete(0, END)

def confirm_info_popup(website_par, email_username_par, password_par):
    user_response = messagebox.askokcancel(
        message=f"Website: {website_par}\n\nEmail/Username: {email_username_par}\n\nPassword: {password_par}\n\nDo you want to save these data?"
        ) #returns True/False

    return user_response

def data_saved_popup():
    messagebox.showinfo(message="Your data has been saved!")

# ---------------------------- SEARCH DATA ------------------------------- #
def search_data():
    website = entry_website.get().title()
    try:
        with open("./data.json", mode="r") as data_file:
            data = json.load(data_file)

        email_username = data[website]["email/username"]
        password = data[website]["password"]

    except FileNotFoundError:
        messagebox.showerror(message="No Data File Found")
    except KeyError:
        messagebox.showerror(message=f"No details for {website} exists")
    else:
        messagebox.showinfo(message=f"Website: {website}\n\nEmail/Username: {email_username}\n\nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#canvas
canvas = Canvas(width=200, height=200) #in px
img_logo = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=img_logo)
canvas.grid(row=0, column=1)

#lbl
lbl_website = Label(text="Website:")
lbl_website.grid(row=1, column=0)

lbl_email_username = Label(text="Email/Username:")
lbl_email_username.grid(row=2, column=0)

lbl_password = Label(text="Password:")
lbl_password.grid(row=3, column=0)

#input
entry_website = Entry(width=21)
entry_website.grid(row=1, column=1) #default column/rowspan == 1
entry_website.focus() #cursor

entry_email_username = Entry(width=38)
entry_email_username.grid(row=2, column=1, columnspan=2)
#add starting value
entry_email_username.insert(0, DEFAULT_EMAIL) #index == the index of characters

entry_password = Entry(width=21)
entry_password.grid(row=3, column=1)

#btn
btn_search = Button(text="Search", width=13, pady=0, command=search_data)
btn_search.grid(row=1, column=2)

btn_generate = Button(text="Generate Password", width=13, pady=0, command=generate_password)
btn_generate.grid(row=3, column=2)

btn_add = Button(text="Add", width=36, command=add_data)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()