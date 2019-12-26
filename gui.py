from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import face_recognition
import os
import sys
import re
from PIL import Image
import PIL
from tkinter import messagebox

window = Tk()
window.title("Face Records App")
window.geometry('350x200')
lbl = Label(window, text="Upload photo of unknown person",
            foreground="red", font=("Helvetica", 16))
lbl.grid(column=0, row=0)


def OpenFile():
    name = askopenfilename(initialdir="/home/zeljko/Workspace/met/Skripting jezici/face_records/photos",
                           filetypes=(("Text File", "*.jpg"),
                                      ("All Files", "*.*")),
                           title="Choose a file."
                           )
    print(name)
    unknown_image = face_recognition.load_image_file(name)
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    data = "./data"
    for filename in os.listdir(data):
        if filename.endswith(".jpg"):
            known_image = face_recognition.load_image_file(data+"/"+filename)
            known_encoding = face_recognition.face_encodings(known_image)[0]
            result = face_recognition.compare_faces(
                [known_encoding], unknown_encoding)
        if result[0]:
            print("We have a matching!\n\n")
            f = open(data+"/"+re.split(r"\.", filename)[0]+".txt", "r")
            info = f.read()
            print(info)
            messagebox.showinfo("We have a matching!", info)
            f.close()
            sys.exit(0)
    MsgBox = messagebox.askquestion(
        'Unknown person', 'Do you want to register this person?', icon='warning')
    if MsgBox == 'yes':
        register_new_person()

    else:
        messagebox.showinfo(
            'END', 'END')


def register_new_person():
    window1 = Tk()
    window1.title("New window for data update")
    window1.geometry('400x450')
    Label(window1, text="First Name: ").grid(row=0)
    Label(window1, text="Last Name: ").grid(row=2)
    Label(window1, text="Title: ").grid(row=4)
    Label(window1, text="Email: ").grid(row=6)
    Label(window1, text="Phone: ").grid(row=8)
    Label(window1, text="Adress: ").grid(row=10)
    Label(window1, text="Note: ").grid(row=12)
    Label(window1, text="File Name: ").grid(row=14)

    e1 = Entry(window1)
    e1.grid(row=1)
    e2 = Entry(window1)
    e2.grid(row=3)
    e3 = Entry(window1)
    e3.grid(row=5)
    e4 = Entry(window1)
    e4.grid(row=7)
    e5 = Entry(window1)
    e5.grid(row=9)
    e6 = Entry(window1)
    e6.grid(row=11)
    e7 = Entry(window1)
    e7.grid(row=13)
    file_name = Entry(window1)
    file_name.grid(row=15)

    def save_person():
        f_name = file_name.get()
        f = open(
            "/home/zeljko/Workspace/met/Skripting jezici/face_records/data/"+f_name+".txt", "a")
        f.write(e1.get()+"\n")
        f.write(e2.get()+"\n")
        f.write(e3.get()+"\n")
        f.write(e4.get()+"\n")
        f.write(e5.get()+"\n")
        f.write(e6.get()+"\n")
        f.write(e7.get()+"\n")
        f.close()
    button_calc = Button(window1, text="Save", command=save_person)
    button_calc.grid(row=16)


btn = Button(window, text="Upload photo", command=OpenFile)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
window.mainloop()
