from flask import Flask, request, jsonify
import dbsv as db
import os

app = Flask(__name__)

image_directory = "gambar"

db_manager = db.DatabaseManager()

@app.route("/insert_jenisTransportasi", methods=["POST"])
def insert_jenisTransportasi():
    try:
        data = request.get_json()
        jenisTransportasi_name = data["jenisTransportasi_name"]
        db_manager.insert_jenisTransportasi(jenisTransportasi_name)
        return jsonify({"message": "jenisTransportasi inserted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/insert_images", methods=["POST"])
def insert_images():
    try:
        # Menerima file gambar dari permintaan POST
        if 'image' in request.files:
            image = request.files['image']
            
            # Pastikan direktori "gambar" ada
            if not os.path.exists(image_directory):
                os.makedirs(image_directory)
            
            # Simpan file gambar ke direktori "gambar"
            image_path = os.path.join(image_directory, image.filename)
            image.save(image_path)
            
            # Simpan path gambar ke database
            db_manager.insert_images(image_path)
            
            return jsonify({"message": "Image inserted successfully"})
        else:
            return jsonify({"error": "No image file found in the request"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/insert_jumlahTransportasi_data", methods=["POST"])
def insert_jumlahTransportasi_data():
    try:
        data = request.get_json()
        # Parse the JSON data and insert into the database using db_manager
        db_manager.insert_jumlahTransportasi_data(data["id_jumlahTransportasi"], data["jumlahTransportasi"], 
                                                  data["waktu"], data["id_images"], data["id_jenisTransportasi"])
        return jsonify({"message": "Parking data inserted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)