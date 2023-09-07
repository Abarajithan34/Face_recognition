import pandas as pd
import numpy as np
import face_recognition

# load data from file
file = pd.read_csv('C:/abarajithan/mini_project/face/photo_database/faces1.csv')
number = file["number"].tolist() 
section = file["section"].tolist()
name = file["name"].tolist()
photo_location = file["photo_location"].tolist()

# create a numpy array to store the encodings
encodings = np.empty((len(photo_location), 128), dtype=np.float64)

# loop through each photo location, load the image and get the encoding
for i in range(len(photo_location)):
    image = face_recognition.load_image_file(photo_location[i])
    encoding = face_recognition.face_encodings(image)
    if len(encoding) > 0:
        encodings[i] = encoding[0]
    else:
        encodings[i] = np.nan

# create a DataFrame to store the encodings
df_encodings = pd.DataFrame({'number': number, 'section': section, 'name': name, 'encoding': encodings})

# save the DataFrame to a CSV file
df_encodings.to_csv('C:/abarajithan/mini_project/face/photo_database/faces6.csv', index=False)
