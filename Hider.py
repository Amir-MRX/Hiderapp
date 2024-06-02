import customtkinter as ctk
import os
from PIL import Image
from customtkinter import filedialog
from CTkMessagebox import CTkMessagebox

#error Handler
def show_error(message):
    CTkMessagebox(title="Error", message=message, icon="cancel")

def show_checkmark(message):
    CTkMessagebox(message=message, icon="check", option_1="Thanks", title="Succses")


#setupWindow
root = ctk.CTk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Hider")
root._set_appearance_mode("Dark")
ctk.set_default_color_theme("D:\Python Project\Hider\Hacked\Hacked\hacked.json")

# setup Folder Icon
icon_btn = ctk.CTkImage(light_image=Image.open("Folder.png"), size=(20, 20), dark_image=Image.open("Folder.png"))

#setup Working

folder_var = ctk.StringVar(value="nofolder")
file_show_path = ctk.StringVar()
hide_var = ctk.StringVar(value="show")

def findingfileorfolder():
    if folder_var.get() == "folder":
        hidedirect = file_show_path.set(filedialog.askdirectory())
    elif folder_var.get() != "yes":
        hidesingle = file_show_path.set(filedialog.askopenfilename())
    else:
        pass

def hide():
    hiders = file_show_path.get()
    if hiders != "":
        if hide_var.get() == "show":  
            if os.path.exists(hiders):
                os.system(f'attrib -h -s -r "{hiders}"')
                show_checkmark("Succses OnHide")
            else:
                show_error("Incorect File Path")
        elif hide_var.get() == "hide":
            if os.path.exists(hiders):
                os.system(f'attrib +h +s +r "{hiders}"')
                show_checkmark("Succses Hide")
            else:
                show_error("Incorect File Path")
    else:
        show_error("No Set Path!")

#Setup GUI
name_app = ctk.CTkLabel(root,text="Hider App", font=("Arial", 20))
name_app.place(relx=.43, rely=.05)

frame_switchs = ctk.CTkFrame(master=root, width=200, height=200, corner_radius=5, fg_color="#78b600", border_color="#456900", border_width=4)
frame_switchs.place(relx=.12, rely=.35)

file_name_input = ctk.CTkEntry(root, placeholder_text="Enter Your File Name",width=300, height=35, corner_radius=5, textvariable=file_show_path)
file_name_input.place(relx=0.12, rely=0.2)

Folder_hider_btn = ctk.CTkButton(root, width=20, height=35, text=" ",image=icon_btn, anchor='c', command=findingfileorfolder)
Folder_hider_btn.place(relx=0.88, rely=.2)

switch_hide_unhide = ctk.CTkSwitch(frame_switchs, width=30, text="Hide", height=30, offvalue="show", onvalue="hide", variable=hide_var)
switch_hide_unhide.place(relx=.15, rely=0.35)

switch_group_single = ctk.CTkSwitch(frame_switchs, width=30, text="Folder", height=30, onvalue="folder", offvalue="nofolder", variable=folder_var)
switch_group_single.place(relx=.15, rely=0.6)

Hide_btn = ctk.CTkButton(root, text="Hide",width=150, height=40, corner_radius=3, font=("Arial", 12), command=hide)
Hide_btn.place(relx=.35, rely=.87)

root.iconbitmap("Hide.ico")
root.mainloop()

