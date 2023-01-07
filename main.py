import tkinter
import random

FONT_NAME = "Courier"
ALP_FOR_GEN = ["a","b","c","d","e","f","j","h","i","g","k","l","m","n","o","p","q","r","s","t","w","x","y","z",1,2,3,4,5,6,7,8,9,0,'!','@','#','$','%','^','&','*','(',')','<','>','?','+','-','*','/']
password_array = []
password = ""
search_result_mail = ""
search_result_web = ""
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
    
    pass_input.insert(0, password)
    
    



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_add_data():
    web_name = web_input.get()
    mail_name = mail_input.get()
    pass_name = password

    # print(web_name)
    # print(mail_name)
    # print(pass_name)

    with open('password.txt', mode="a") as file:
        file.writelines("\n" + web_name + " " + mail_name + " " + pass_name)


#----------------------------- Search Password ------------------------ #
def search_data():
    global search_web_input,search_mail_input, search_result_web_show
    search_result_web = search_web_input.get()
    low_search_result_web = search_result_web.lower()
    result_pass_input.delete(0,'end')
    search_mail_input.delete(0,'end')
    search_result_web_show.delete(0,'end')
    with open("password.txt", mode="r") as data:
        data_text = data.read()
        low_data = data_text.lower()
        low_data_split = low_data.split()
        for i in low_data_split:
            if i == low_search_result_web:
                index_i = low_data_split.index(i)
                result_pass_input.insert(0,"Pass: " + low_data_split[index_i + 2])
                search_mail_input.insert(0,"Email: " + low_data_split[index_i + 1])
                search_result_web_show.insert(0,"web: " + low_data_split[index_i])

    

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Passwor Generator")
window.config(padx=20,pady=20)

# canvas = tkinter.Canvas(height=200, width=200)
# logo = tkinter.PhotoImage(file="logo.png")
# canvas.create_image(100,100, image=logo)
canvas = tkinter.Label(text="🗝", font=(FONT_NAME,100,'bold'))
canvas.grid(column=1,row=0)

#labels
search_label_icon = tkinter.Label(text="🕵🏻‍♂️", font=(FONT_NAME,100,"bold"))
web_label = tkinter.Label(text="Website:")
mail_label = tkinter.Label(text="Email/Username:")
pass_label = tkinter.Label(text="Password:")
len_label = tkinter.Label(text="Length:")

search_label_icon.grid(column=3,row=0)
web_label.grid(column=0,row=1)
mail_label.grid(column=0,row=2)
pass_label.grid(column=0,row=3)
len_label.grid(column=0,row=4)

#buttons

gen_button = tkinter.Button(text="Generation", command=gen_passwoed)
add_button = tkinter.Button(text="Add", width=31, command=save_add_data)
search_add_button = tkinter.Button(text="Search", width=16, command=search_data)

gen_button.grid(column=2,row=3)
add_button.grid(column=1,row=5,columnspan=2)
search_add_button.grid(column=3,row=5,columnspan=2)
#inputs

web_input = tkinter.Entry(width=30)
web_input.focus()
mail_input = tkinter.Entry(width=30)
mail_input.insert(0, "test@mail.com")
pass_input = tkinter.Entry(width=18)

search_web_input = tkinter.Entry(width=30)
search_web_input.insert(0,"Type Web name for searching")
search_result_web_show= tkinter.Entry(width=30)
search_result_web_show.insert(0,"Searched Website Name")
search_mail_input = tkinter.Entry(width=30)
search_mail_input.insert(0, "Your Email/Username for Website login")
result_pass_input = tkinter.Entry(width=30)
result_pass_input.insert(0, "Your Password/Don't show it to anyone")

len_input = tkinter.Spinbox(from_= 8, to=16, width=2, command=get_leng)
len_input.grid(column=0,row=5)

web_input.grid(column=1,row=1, columnspan=2)
mail_input.grid(column=1,row=2, columnspan=2)
pass_input.grid(column=1,row=3, columnspan=1)

search_web_input.grid(column=3,row=1, columnspan=2)
search_result_web_show.grid(column=3,row=2, columnspan=2)
search_mail_input.grid(column=3,row=3, columnspan=2)
result_pass_input.grid(column=3,row=4, columnspan=1)
window.mainloop()