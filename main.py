from password_gen import passwd
from tkinter import *
from tkinter import messagebox
from playsound import playsound 

#  PASSWORD GENERATOR  #
def generate_but(): 
    new_pass = passwd()  
    password.insert(0,new_pass)
# SAVE PASSWORD #
def save_data():
    if website_input.get() != "" and username_input.get() != "" and password.get() != "" : 
        with open("records.txt",'a',encoding = 'utf-8') as f:
            f.write(f"{website_input.get()} | {username_input.get()} | {password.get()} | \n")
        website_input.delete(0,'end')
        username_input.delete(0,'end')
        password.delete(0,'end')
        succesful()
    else : 
        error()
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
website_input = Entry(width=35,bg="white") 
website_input.grid(row=1 ,column=1 , columnspan=2)
username_input = Entry(width=35,bg="white") 
username_input.grid(row=2 ,column=1 , columnspan=2)
password = Entry(width=17,bg="white") 
password.grid(row=3 ,column=1)
# Action Buttons 
gen_pass_button = Button(text="Generate" , width=13,bg="white",command=generate_but)
gen_pass_button.grid(row=3 ,column=2)
save_pass_button = Button(text="Add" ,bg="white",highlightcolor="white", width=30 ,highlightthickness=0, command=save_data)
save_pass_button.grid(row=4 ,column=1 ,columnspan=2)

window.mainloop() 
