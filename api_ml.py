from flask import Flask, request
import numpy as np
import sqlite3
import os
import cv2

app = Flask(__name__)

# Load YOLO
net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getUnconnectedOutLayersNames()

# Assign upload folder
UPLOAD_FOLDER = 'hasil'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize the sequence number (counter) outside the function
video_counter = 1

# Define the classes to detect: bike, car, and motorcycle
classes_to_detect = ["bike", "car", "motorcycle"]

@app.route('/upload', methods=['POST'])
def upload_file():
    global video_counter

    # Receives videos from POST requests
    file = request.files['file']

    # Save the predicted video with the file name "video_result.mp4"
    result_folder = 'hasildeteksi'
    os.makedirs(result_folder, exist_ok=True)
    result_video_path = os.path.join(result_folder, 'video.mp4')

    # Inisialisasi VideoCapture
    cap = cv2.VideoCapture(file)
    out = cv2.VideoWriter(result_video_path, cv2.VideoWriter_fourcc(*'mp4v'), 30.0, (int(cap.get(3)), int(cap.get(4))))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Preprocess frame for YOLO
        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)

        # Save frame with bounding boxes
        out.write(frame)
    
    # Release VideoCapture and VideoWriter
    cap.release()
    out.release()

    # Connect to the database
    conn = sqlite3.connect('vehiscanner.db')
    cursor = conn.cursor()

    # Insert data into the "video" table
    video_path = f"{UPLOAD_FOLDER}/{file.filename}"
    cursor.execute("INSERT INTO video (path_video) VALUES (?)", (video_path,))
    conn.commit()  # Commit to get the ID

    # Get the last inserted video ID
    cursor.execute("SELECT last_insert_rowid()")
    current_id_video = cursor.fetchone()[0]

    # Get the last inserted jenistransportasi ID
    cursor.execute("SELECT last_insert_rowid()")
    current_id_jenistransportasi = cursor.fetchone()[0]

     # Get the last inserted jumlahtransportasi ID
    cursor.execute("SELECT last_insert_rowid()")
    current_id_jumlahtransportasi = cursor.fetchone()[0]

    data = {
        'id_jumlahtransportasi' : current_id_jumlahtransportasi,
        'jumlahtransportasi': 8,  # Replace with the desired value
        'id_video' : current_id_video,
        'id_jenistransportasi' : current_id_jenistransportasi
    }

    # Insert data into the "jumlahtransportasi" table
    id_jumlahtransportasi = data['id_jumlahtransportasi']
    jumlahtransportasi = data['jumlahtransportasi']
    id_video = data['id_video']
    id_jenistransportasi = data['id_jenistransportasi']
    cursor.execute("INSERT INTO jumlahtransportasi (id_jumlahtransportasi, jumlahtransportasi, id_video, id_jenistransportasi) VALUES (?, ?, ?, ?)",
                   (id_jumlahtransportasi, jumlahtransportasi, id_video, id_jenistransportasi))
    
    # Commit to get the ID
    conn.commit()  

    # Close the connection
    conn.close()

    # Send data to the database server
    url = 'http://csbnpmnk-5001.asse.devtunnels.ms/store'  # Replace with the correct db API URL

    return "data_saved"

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5000)