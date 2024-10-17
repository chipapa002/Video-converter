import customtkinter as ctk 
import moviepy
from moviepy.editor import *
from tkinter.filedialog import *
import os


def name(path):

    count = 0
    line = ""

    for i in path:
        if i == "/" :
            count += 1
        if count == 4 :
            line += i

    line = line[1:]
    name = line[:-4]

    return name


def file_select():
    global path
    global file
    file = askopenfilename()
    path = str(file)
    if path == "":
        opt_label.configure(text= "Nothing was selected :(", text_color = "red")
    else:
        opt_label.configure(text= "the following file " + path + " was selected what would you like to do with it? select from the options below", text_color= "white")
    

def file_delete():
    os.remove(path)
    opt_label.configure(text= path + " Deleted successfully!!", text_color="white")
    
    
    
def file_convert():
    try:
        vid = moviepy.editor.VideoFileClip(file)
    except Exception:
        if path == "":
            opt_label.configure(text="Nothing was selected :(", text_color="red")
        else:
            opt_label.configure(text="the file selected is not convertable to a mp4 file :(", text_color="red")
    audio_name = name(path) + ".mp3"
    audio = vid.audio
    audio.write_audiofile("C:\\Users\\Nndamulele\\Music\\" + audio_name)
    opt_label.configure(text="video converted successfully!!", text_color="white")
    vid.close()
    audio.close()
    


#system settings 
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#setting up the app
parent = ctk.CTk()
parent.geometry("900x400")
parent.title("mp4 to mp3 converter")

#app's UI features
label = ctk.CTkLabel(parent, text="Click the select button below in order to sect the file that you would like to delete or convert into an mp3 file")
label.pack()

#select button
sel_btn = ctk.CTkButton(parent, text="Select", command= file_select)
sel_btn.pack(padx=10, pady=10)

#option label
opt_label = ctk.CTkLabel(parent, text="")
opt_label.pack()

#option buttons
# 1. delete button
delete = ctk.CTkButton(parent, text="Delete", command= file_delete)
delete.pack(padx=10, pady=10)

#2. convert button
convert = ctk.CTkButton(parent, text="mp3 Convert", command=file_convert)
convert.pack(padx=10, pady=10)

#run app
parent.mainloop()

