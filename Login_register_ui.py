import tkinter as tk
import customtkinter as ctk

from customtkinter import *



ctk.set_appearance_mode("system")

root = ctk.CTk()


label = CTkLabel(root, text="main UI page")
label.pack(pady=20, padx= 40, fill='both', expand=False)
root.geometry("500x500")
root.title("Login/ Register UI using Customtkinter")


#switching inteface
def switch_ui(switch_to):
    if switch_to == 'login':
        login_page_option.configure(fg_color='#1F6AA5', text_color='white')
        register_page_option.configure(fg_color='white', text_color='black')

        for widgets in loginframe.winfo_children():
            widgets.destroy()
        
        login_page()


    else:
        login_page_option.configure(fg_color='white', text_color='black')
        register_page_option.configure(fg_color='#1F6AA5', text_color='white')
        register_page()
        
        for widgets in loginframe.winfo_children():
            widgets.destroy()

        register_page()

#buttons for login and register page
login_page_option = ctk.CTkButton(master=root, text='login',
                                    font=('Bold', 20), text_color = 'white',
                                    width=120,height=40, corner_radius=10,
                                    border_width=2, command=lambda: switch_ui(switch_to='login') )
login_page_option.place(x=65, y=40)


register_page_option = ctk.CTkButton(master=root, text='register',
                                    font=('Bold', 20),text_color = 'white',
                                    width=120,height=40, corner_radius=10,
                                    border_width=2, command=lambda: switch_ui(switch_to='register'))
register_page_option.place(x=315, y=40)


#create a frame
loginframe = ctk.CTkFrame(master=root, width=250, height=250, corner_radius=15)
loginframe.pack(pady=30,padx=40, fill='both', expand=True)




def login_page():

    #label
    heading_lb = ctk.CTkLabel(master=loginframe, text='Login Page', font=('Bold', 25))
    heading_lb.pack(pady=20, padx=20)

    #text box for inputs
    #username ui
    user_uname = ctk.CTkEntry(master=loginframe, placeholder_text="Username")
    user_uname.pack(pady=12, padx=20)

    #password ui
    user_pass = ctk.CTkEntry(master=loginframe, placeholder_text="Password", show="*")
    user_pass.pack(pady=12, padx=20)

    #login button
    button = ctk.CTkButton(master=loginframe, text='Login')
    button.pack(pady=12, padx=20)

    checkbox = ctk.CTkCheckBox(master=loginframe,text='Remember Me') 
    checkbox.pack(pady=12,padx=20)

    #test button
    #testbutton = ctk.CTkButton(master=loginframe, text='to landingp')
    #testbutton.pack(pady=12, padx=10)





def register_page():

    #label
    heading_lb = ctk.CTkLabel(master=loginframe, text='Sign up Page', font=('Bold', 25))
    heading_lb.pack(pady=20, padx=20)

    #for registration page
    #text box for inputs
    #username ui
    user_usname = ctk.CTkEntry(master=loginframe, placeholder_text="Username")
    user_usname.pack(pady=12, padx=10)

    #email ui
    user_uemail = ctk.CTkEntry(master=loginframe, placeholder_text="email")
    user_uemail.pack(pady=12, padx=10)

    #password ui
    user_upass = ctk.CTkEntry(master=loginframe, placeholder_text="Password", show="*")
    user_upass.pack(pady=12, padx=10)

    user_upass2 = ctk.CTkEntry(master=loginframe, placeholder_text="confirm password", show="*")
    user_upass2.pack(pady=12, padx=10)

    #register button
    button2 = ctk.CTkButton(master=loginframe, text='Register')
    button2.pack(pady=12, padx=10)





root.mainloop()