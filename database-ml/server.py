from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import response as responses

app = Flask(__name__)
res = responses.Responses()

# Konfigurasi database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/VehiScanner'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definisi model tabel
class Images(db.Model):
    id_images = db.Column(db.Integer, primary_key=True, autoincrement=True)
    path_images = db.Column(db.String(255))
    uploaded_date = db.Column(db.TIMESTAMP(6))

class JenisTransportasi(db.Model):
    id_jenisTransportasi = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jenisTransportasi = db.Column(db.String(20))
    waktu = db.Column(db.TIMESTAMP(6))

class JumlahTransportasi(db.Model):
    id_jumlahTransportasi = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jumlahTransportasi = db.Column(db.Integer)
    waktu = db.Column(db.TIMESTAMP(6))
    id_images = db.Column(db.Integer, db.ForeignKey('images.id_images'))
    id_jenisTransportasi = db.Column(db.Integer, db.ForeignKey('jenisTransportasi.id_jenisTransportasi'))

# Membuat tabel dalam database jika belum ada
db.create_all()

# API endpoint untuk menambahkan data ke tabel images
@app.route('/add_image', methods=['POST'])
def add_image():
    data = request.json
    new_image = Images(path_images=data['path_images'], uploaded_date=data['uploaded_date'])
    db.session.add(new_image)
    db.session.commit()
    return jsonify({'message': 'Gambar berhasil ditambahkan'}), 201

# API endpoint untuk menambahkan data ke tabel jenisTransportasi
@app.route('/add_jenis_transportasi', methods=['POST'])
def add_jenis_transportasi():
    data = request.json
    new_jenis_transportasi = JenisTransportasi(jenisTransportasi=data['jenisTransportasi'], waktu=data['waktu'])
    db.session.add(new_jenis_transportasi)
    db.session.commit()
    return jsonify({'message': 'Jenis transportasi berhasil ditambahkan'}), 201

# API endpoint untuk menambahkan data ke tabel jumlahTransportasi
@app.route('/add_jumlah_transportasi', methods=['POST'])
def add_jumlah_transportasi():
    data = request.json
    new_jumlah_transportasi = JumlahTransportasi(
        jumlahTransportasi=data['jumlahTransportasi'],
        waktu=data['waktu'],
        id_images=data['id_images'],
        id_jenisTransportasi=data['id_jenisTransportasi']
    )
    db.session.add(new_jumlah_transportasi)
    db.session.commit()
    return jsonify({'message': 'Jumlah transportasi berhasil ditambahkan'}), 201

if __name__ == '__main__':
    app.run(debug=True)
