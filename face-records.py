import face_recognition

known_image = face_recognition.load_image_file("./img/known/mark.jpg")
unknown_image = face_recognition.load_image_file("./img/unknown/someone.jpg")

known_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([known_encoding], unknown_encoding)

if results[0]:
    print("We have matching!")
else:
    print("We don't have matching!")
