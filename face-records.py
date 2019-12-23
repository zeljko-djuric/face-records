import face_recognition
import os
import sys
import re
from PIL import Image
import PIL

data = "./data"
unknown_image = face_recognition.load_image_file("./photos/jobi.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

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
answer = input("Do you want to register this person? yes/no\n")
if(answer == "yes"):
    name = input("Enter person name: ")
    f = open(data+"/"+name+".txt", "a")
    info = input(
        "When you are done with input enter end\nEnter data for a new person:\n")
    while(info != "end"):
        f.write(info+"\n")
        info = input()
    f.close()
    im1 = Image.open(r"./photos/jobi.jpg")
    im1 = im1.save(data+"/"+name+".jpg")
elif (answer == "no"):
    print("END")
else:
    print("Invalid arguments")
