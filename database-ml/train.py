import cv2
import numpy as np
from keras.models import load_model

# Load model machine learning yang sudah dilatih
model = load_model('keras_model.h5')  # Gantilah 'model_kendaraan.h5' dengan nama file model Anda

# Daftar kelas atau label yang digunakan
kelas = {0: 'sepeda', 1: 'mobil', 2: 'motor'}

# Fungsi untuk mengklasifikasikan gambar dari webcam
def klasifikasikan_kendaraan(frame):
    # Praproses gambar (misalnya, resize, normalisasi)
    frame = cv2.resize(frame, (224, 224))
    frame = frame / 255.0  # Normalisasi pixel ke rentang [0, 1]
    frame = np.expand_dims(frame, axis=0)  # Tambahkan dimensi batch

    # Lakukan prediksi menggunakan model
    hasil_prediksi = model.predict(frame)
    kelas_prediksi = np.argmax(hasil_prediksi)

    # Dapatkan label prediksi
    label = kelas[kelas_prediksi]

    return label

# Mulai webcam
cap = cv2.VideoCapture(0)  # Angka 0 mengacu pada webcam bawaan, ganti sesuai dengan perangkat yang Anda gunakan

while True:
    ret, frame = cap.read()

    # Deteksi kendaraan dan klasifikasikan
    hasil_klasifikasi = klasifikasikan_kendaraan(frame)

    # Tampilkan hasil klasifikasi pada layar
    cv2.putText(frame, hasil_klasifikasi, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Deteksi Kendaraan', frame)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup webcam dan jendela
cap.release()
cv2.destroyAllWindows()
































# from keras.models import load_model
# import cv2
# import numpy as np

# np.set_printoptions(suppress=True)

# class WebcamClassifier:
#     def __init__(self, model_path, labels_path, camera_index=0):
#         self.model_path = model_path
#         self.labels_path = labels_path
#         self.camera_index = camera_index
#         self.model = None
#         self.class_names = None
#         self.camera = None

#     def load_model(self):
#         self.model = load_model(self.model_path, compile=False)

#     def load_labels(self):
#         with open(self.labels_path, "r") as f:
#             self.class_names = f.readlines()

#     def open_camera(self):
#         self.camera = cv2.VideoCapture(self.camera_index)

#     def predict_image(self, image):
#         # Resize the raw image into (224-height,224-width) pixels
#         image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

#         # Show the image in a window
#         cv2.imshow("Webcam Image", image)

#         # Make the image a numpy array and reshape it to the models input shape.
#         image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

#         # Normalize the image array
#         image = (image / 127.5) - 1

#         # Predict the model
#         prediction = self.model.predict(image)
#         index = np.argmax(prediction)
#         class_name = self.class_names[index]
#         confidence_score = prediction[0][index]

#         # Print prediction and confidence score
#         print("Class:", class_name[2:], end="")
#         print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

#     def run(self):
#         self.load_model()
#         self.load_labels()
#         self.open_camera()

#         while True:
#             # Grab the webcamera's image.
#             ret, image = self.camera.read()

#             self.predict_image(image)

#             # Listen to the keyboard for presses.
#             keyboard_input = cv2.waitKey(1)

#             # 27 is the ASCII for the esc key on your keyboard.
#             if keyboard_input == 27:
#                 break

#         self.camera.release()
#         cv2.destroyAllWindows()


# # Usage
# model_path = "keras_Model.h5"
# labels_path = "labels.txt"
# camera_index = 0

# webcam_classifier = WebcamClassifier(model_path, labels_path, camera_index)
# webcam_classifier.run()