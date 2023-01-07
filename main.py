import tkinter
import random

FONT_NAME = "Courier"
ALP_FOR_GEN = ["a","b","c","d","e","f","j","h","i","g","k","l","m","n","o","p","q","r","s","t","w","x","y","z",1,2,3,4,5,6,7,8,9,0,'!','@','#','$','%','^','&','*','(',')','<','>','?','+','-','*','/']
password_array = []
password = ""
leng = 8
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_leng():
    global leng
    leng = int(len_input.get())

def gen_passwoed():
    global leng, password
    password_array = []
    pass_input.delete(0, 'end')
    for i in range(0,leng):
        password = ""
        password_array.append(ALP_FOR_GEN[random.randint(0,(len(ALP_FOR_GEN)-1))])
    for i in password_array:
        password = str(password) + str(i)
    
    pass_input.insert(0, f"{password}")
    
    



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_add_data():
    web_name = web_input.get()
    mail_name = mail_input.get()
    pass_name = password

    print(web_name)
    print(mail_name)
    print(pass_name)

    with open('password.txt', mode="a") as file:
        file.writelines(f"\n{web_name} | {mail_name} | {pass_name}")
    
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Passwor Generator")
window.config(padx=20,pady=20)

canvas = tkinter.Canvas(height=200, width=200)
logo = tkinter.PhotoImage(file="/Users/programing/Desktop/programing/262 password-manager-start/logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1,row=0)

#labels

web_label = tkinter.Label(text="Website:")
mail_label = tkinter.Label(text="Email/Username:")
pass_label = tkinter.Label(text="Password:")
len_label = tkinter.Label(text="Length:")

web_label.grid(column=0,row=1)
mail_label.grid(column=0,row=2)
pass_label.grid(column=0,row=3)
len_label.grid(column=0,row=4)

#buttons

gen_button = tkinter.Button(text="Generation", command=gen_passwoed)
add_button = tkinter.Button(text="Add", width=36, command=save_add_data)

gen_button.grid(column=2,row=3)
add_button.grid(column=1,row=4,columnspan=2)

#inputs

web_input = tkinter.Entry(width=35)
web_input.focus()
mail_input = tkinter.Entry(width=35)
mail_input.insert(0, "test@mail.com")
pass_input = tkinter.Entry(width=21)

len_input = tkinter.Spinbox(from_= 8, to=16, width=2, command=get_leng)
len_input.grid(column=0,row=5)

web_input.grid(column=1,row=1, columnspan=2)
mail_input.grid(column=1,row=2, columnspan=2)
pass_input.grid(column=1,row=3, columnspan=1)
window.mainloop()