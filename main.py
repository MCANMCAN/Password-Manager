from email import message
import email
import json
from password_gen import passwd
from tkinter import *
from tkinter import messagebox
#  PASSWORD GENERATOR  #
def generate_but(): 
    new_pass = passwd()  
    password.insert(0,new_pass)
# SAVE PASSWORD #
def save_data():
    website = website_input.get()
    usname = username_input.get()
    passwd = password.get()
    new_data ={
        website: {
            "email" : usname,
            "password": passwd 
        }
    }
    if website != "" and username_input != "" and password != "" : 
        try:   
         with open("records.json",'r') as f:
            data = json.load(f) 
            data.update(new_data) 
        except FileNotFoundError : 
          data=new_data
          with open("records.json",'w') as f:
              json.dump(data,f)
              json.dump(data , f,indent=5)
        with open("records.json",'w') as f:
            json.dump(data , f,indent=5) 

        website_input.delete(0,'end')
        username_input.delete(0,'end')
        password.delete(0,'end')
        succesful()
    else : 
        error()
def search(): 
    website = website_input.get().strip()
    print(website)
    try:
     with open("records.json",'r') as f:
        data = json.load(f) 
    
    except FileNotFoundError: 
        messagebox.showinfo(title="Error" ,message=f"No records saved.File not found! Please store some data in program first")
    else : 
        if website in data.keys() : 
            messagebox.showinfo(title="Recorded" ,message=f"USERNAME : {data[website]['email']} \nPASSWORD : {data[website]['password']} ")
        else: 
            if website == "" : 
                messagebox.showinfo(title="Warning" ,message=f"Website could not be empty. Please enter for website")
            else : 
                messagebox.showinfo(title="Warning" ,message=f"No records for '{website}'. Please check and try again for spelling.") 

    
    
def succesful() : 
    status.config(text="Succesfully added... ", fg="green")
def error() : 
    status.config(text="cannot be empty... ", fg="red")
    messagebox.showinfo(title="warning" ,message="Please fill all necessary areas!")
# UI SETUP #
window = Tk()
window.config(padx=20,pady=20 ,bg="white")
# CANVAS # 
canvas = Canvas(width=200,height=200,bg='white',bd=0,highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(50,100, image=logo)
canvas.grid(column=1,row=0,columnspan=3)
### GUI ### 
# Row Title Labels
website_label = Label(text="Website:",bg="white")
website_label.grid(row=1 , column=0)
email_username_label = Label(text="Email/Username:",bg="white")
email_username_label.grid(row=2 , column=0)
password_label = Label(text="Password:",bg="white",)
password_label.grid(row=3 , column=0)
status = Label(bg="white" , fg="green")
status.grid(row=4 , column=0)
# Entry Boxes 
website_input = Entry(width=17,bg="white") 
website_input.grid(row=1 ,column=1)
username_input = Entry(width=35,bg="white") 
username_input.grid(row=2 ,column=1 , columnspan=2)
password = Entry(width=17,bg="white") 
password.grid(row=3 ,column=1)
# Action Buttons 
gen_pass_button = Button(text="Generate" , width=13,bg="white",command=generate_but)
gen_pass_button.grid(row=3 ,column=2)
save_pass_button = Button(text="Add" ,bg="white",highlightcolor="white", width=30 ,highlightthickness=0, command=save_data)
save_pass_button.grid(row=4 ,column=1 ,columnspan=2)
search_button = Button(text="Search" , width=13,bg="white",command=search)
search_button.grid(row=1 ,column=2)
window.mainloop() 
