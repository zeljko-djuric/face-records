from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import face_recognition
import os
import sys
import re
from PIL import Image
import PIL

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
            print(f.read())
            f.close()
            sys.exit(0)
    print("NO MATCH!\n")


btn = Button(window, text="Upload photo", command=OpenFile)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
window.mainloop()
