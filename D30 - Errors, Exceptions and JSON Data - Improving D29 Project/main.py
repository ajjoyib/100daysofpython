from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import *
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pr_letters = [choice(letters) for _ in range(randint(4, 6))]
    pr_symbols = [choice(symbols) for _ in range(randint(2, 3))]
    pr_numbers = [choice(numbers) for _ in range(randint(2, 3))]

    password_list = pr_letters + pr_symbols + pr_numbers
    shuffle(password_list)

    password = "".join(password_list)
    if len(e_password.get()) == 0:
        e_password.insert(0, password)
    else:
        e_password.delete(0, END)
        e_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = e_website.get()
    email = e_email.get()
    password = e_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"Ok to proceed the data: \n\nEmail: {email} \nPassword: {password}")
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            e_website.delete(0, END)
            e_password.delete(0, END)

# ---------------------------- SEARCH PASSWORD ----------------------------- #
def find_password():
    website = e_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"ID:  {email}\nPW: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for \'{website}\' exists.")

# ------------------------------- UI SETUP --------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# display the logo image
canvas = Canvas(width=200, height=200, highlightthickness=0)
try: 
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
except Exception as e:
    print(f"Error loading logo image: {e}")
canvas.grid(row=1, column=2)

# Labels
l_website = ttk.Label(text="Website: ")
l_website.grid(row=2, column=1)
l_email = ttk.Label(text="Email/ID: ")
l_email.grid(row=3, column=1)
l_password = ttk.Label(text="Password: ")
l_password.grid(row=4, column=1)

# Entries
# e_website = ttk.Entry(width=35)
# e_website.grid(row=2, column=2, columnspan=2)
e_website = ttk.Entry(width=25)
e_website.grid(row=2, column=2, sticky=E)
e_website.focus()
e_email = ttk.Entry(width=43)
e_email.grid(row=3, column=2, columnspan=2, sticky=E)
e_email.insert(0, "hamidullo287@gmail.com")
e_password = ttk.Entry(width=25)
e_password.grid(row=4, column=2, sticky=E)


# Buttons
b_search = ttk.Button(text="Search", width=17, command=find_password)
b_search.grid(row=2, column=3, sticky=E)
b_generate_password = ttk.Button(text="Generate Password", width=17, command=generate_password)
b_generate_password.grid(row=4, column=3, sticky=E)
b_add = ttk.Button(text="Add", width=43, command=save)
b_add.grid(row=5, column=2, columnspan=2, sticky=E)



window.mainloop()
