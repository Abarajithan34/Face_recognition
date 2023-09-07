import face_recognition
import cv2
from PIL import Image,ImageDraw,ImageFont
import sys
import pandas as pd
import datetime
import os
import time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import csv



#capture face using camera

camera=cv2.VideoCapture(0)

for i in range(10):
    return_value,image=camera.read()
    #print(return_value,image.shape)
    cv2.imwrite('photo'+str(i)+'.png',image)
del(camera)   

unknown_face=face_recognition.load_image_file("photo5.png")

print("1 passed")

#loading data and encoding the data

file=pd.read_csv("C:/abarajithan/mini_project/face/photo_database/faces1.csv")

number=file["number"].tolist() 
section=file["section"].to_list()
name=file["name"].tolist()
photo_location=file["photo_location"].tolist()
#audio_location=file["audio_loaction"].tolist()

no_of_face=len(number)


people=[]
people_encoding=[]


for i in range(no_of_face):
    people.append(face_recognition.load_image_file(photo_location[i]))
    people_encoding.append(face_recognition.face_encodings(people[i])[0])

#print(people_encoding)

print("2 passed")


#face recognition
def identify_people(photo):
    try:
        unknown_face_encode=face_recognition.face_encodings(unknown_face)[0]
    except IndexError as e:
        print(e)
        pygame.mixer.init()
        pygame.mixer.music.load("C:/abarajithan/mini_project/face/photo_database/voice/face not recognized.mp3")
        pygame.mixer.music.play()
        time.sleep(5)
        sys.exit(1)
    found=face_recognition.compare_faces(people_encoding,unknown_face_encode,tolerance=0.5)
    #print(found)

    index=-1
    for i in range(no_of_face):
        if found[i]:
            index=i
            break
    return index          

people_index=identify_people(unknown_face)       
#print(people_index)


print("3 passed")
print("31")
#attendance record in a file
if(people_index!=-1):
    time=str(datetime.datetime.now())
    recognized_number=str(number[people_index])
    recognized_name=name[people_index]
    belong_class=str(section[people_index])
    print("32")
    #text_to_be_entered="\n"+recognized_number+" "+str(section[people_index])+" "+recognized_name+" "+time
    with open("C:/abarajithan/mini_project/face/final/Main_attendance.csv",mode="a",newline="") as csvfile: 

        fieldnames=["Number","Section","Name","Time"]
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow({"Number":recognized_number,"Section":belong_class,"Name":recognized_name,"Time":time})



    if(section[people_index]=="A"):
        with open("C:/abarajithan/mini_project/face/final/attendance_A.csv",mode="a",newline="") as csvfile: 

            fieldnames=["Number","Section","Name","Time"]
            writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow({"Number":recognized_number,"Section":belong_class,"Name":recognized_name,"Time":time})
        

    if(section[people_index]=="B"):
        with open("C:/abarajithan/mini_project/face/final/attendance_B.csv",mode="a",newline="") as csvfile: 

            fieldnames=["Number","Section","Name","Time"]
            writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow({"Number":recognized_number,"Section":belong_class,"Name":recognized_name,"Time":time})

    if(section[people_index]=="C"):
        with open("C:/abarajithan/mini_project/face/final/attendance_C.csv",mode="a",newline="") as csvfile: 

            fieldnames=["Number","Section","Name","Time"]
            writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow({"Number":recognized_number,"Section":belong_class,"Name":recognized_name,"Time":time})


    #print(text_to_be_entered)

print("4 passed")



# display attendance record with photo

pil_unknown_face=Image.fromarray(unknown_face)
draw=ImageDraw.Draw(pil_unknown_face)
font1=ImageFont.truetype("arial.ttf",50)

if(people_index==-1):
    people_name="face not recognized"
else:
    people_name=name[people_index]

x=100
y=unknown_face.shape[0]-100

draw.text((x,y),people_name,font=font1,fill=(0,0,0))
pil_unknown_face.show()


print("5 passed")




'''if(people_index!=-1):
    pygame.mixer.init()
    pygame.mixer.music.load("C:/abarajithan/mini_project/face/photo_database/voice/face recognized.mp3")
    pygame.mixer.music.play()
    time.sleep(5)'''