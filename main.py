from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password_function():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for items in range(nr_letters)]
    password_symbols = [random.choice(symbols) for items1 in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for items2 in range(nr_numbers)]

    password_list = password_numbers + password_letters + password_symbols

    random.shuffle(password_list)
    safe_password = "".join(password_list)
    password_entry.insert(0, safe_password)
    pyperclip.copy(safe_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0:
        messagebox.showinfo(title="OOOps..!", message="Please don't leave WEBSITE field empty!")
    elif len(password) == 0:
        messagebox.showinfo(title="OOOps..!", message="Please don't leave PASSWORD  field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nemail: {email} "
                                                              f"\npassword: {password}. \nIs it OK to save?")
        if is_ok:
           # with open("dat_psw.txt", "a") as data_psw:
                #data_psw.write(f"\n{website} | {email} | {password}")
           try:
               with open("data.json", "r") as data_file:
                   # reading old data
                   data = json.load(data_file)
           except FileNotFoundError:
                with open("data.json", "w") as data_file:
                   json.dump(new_data, data_file, indent=4)
           else:
                # updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # saving updates
                    json.dump(data, data_file, indent=4)
           finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #
def search_data():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("file not found")
    else:
        if website in data:
            # messagebox.showinfo(title="info found", message=f"website: {website} {data.get(website)}")
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email: {email}\npassword: {password}")
        else:
            messagebox.showinfo(message=f"no details for {website} found")







# ---------------------------- UI SETUP ------------------------------- #

GREY = "#7EB5A6"
PEACH = "#C36839"
ORANGE = "#86340A"
PALE_ROSE = "#E8D0B3"

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=PALE_ROSE)

#title_label = Label(text="Password Manager",fg=ORANGE, bg=PALE_ROSE, font=("Courier", 18, "bold"))
#title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=200,bg=PALE_ROSE, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 80, image=lock_image)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:", fg=ORANGE, bg=PALE_ROSE)
website_label.grid(row=1, column=0)
email_label = Label(text="E-mail/Username:", fg=ORANGE, bg=PALE_ROSE)
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", fg=ORANGE, bg=PALE_ROSE)
password_label.grid(row=3, column=0)

#Buttons
generate_password=Button(text="Generate Password", fg=ORANGE, bg=PALE_ROSE, command=generate_password_function)
generate_password.grid(row=3, column=2)
add_button=Button(text="ADD", fg=ORANGE, bg=PALE_ROSE, font=("Courier", 10), width=38, command=save)
add_button.grid(row=4, column=1,columnspan=2)
search_website=Button(text="Search", fg=ORANGE, bg=PALE_ROSE, width=14, command=search_data)
search_website.grid(row=1, column=2)

#Entries
website_entry = Entry(width=31)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.insert(0, "veronika.vyalikh@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=31)
password_entry.grid(row=3, column=1)

#canvas.pack()

window.mainloop()
