import face_recognition
import os
import re

directory = "./img/known"

unknown_image = face_recognition.load_image_file("./img/unknown/someone.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        known_image = face_recognition.load_image_file(
            "./img/known/" + filename)
        known_encoding = face_recognition.face_encodings(known_image)[0]
        result = face_recognition.compare_faces(
            [known_encoding], unknown_encoding)
        if result[0]:
            f = open("./img/known/" + re.split(r"\.", filename)[0]+".txt", "r")
            print(f.read())
            f.close()
