from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import os
import logging

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'example'
app.config['MYSQL_DB'] = 'VehiApp'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route("/", methods=['GET'])
def hello():
    return jsonify(status= "running")

@app.route('/add_jenisTransportasi', methods=['POST'])
def add_jenisTransportasi():
    try:
        id_jenisTransportasi= request.form['id_jenisTransportasi']
        jenisTransportasi = request.form['jenisTransportasi']
        waktu_jenis = request.form['waktu_jenis']

        cursor = mysql.connection.cursor()
        cursor.execute('''
            INSERT INTO recordings (id_jenisTransportasi, jenisTransportasi, waktu_jenis)
            VALUES (%s, %s, %s)''', 
            (id_jenisTransportasi, jenisTransportasi, waktu_jenis)
        )
        mysql.connection.commit()
        logging.info(f"Data successfully added with  id_jenisTransportasi: { id_jenisTransportasi}")
        return jsonify(status='success', message='Data successfully added.', data={"id_jenisTransportasi": id_jenisTransportasi})
    except Exception as e:
        logging.error(f"Error adding data: {str(e)}")
        return jsonify(status='error', message=str(e))

def add_jumlahTransportasi():
    try:
        id_jumlahTransportasi = request.form['id_jumlahTransportasi']
        jumlahTransportasi = request.form['jumlahTransportasi']
        waktu_jumlah = request.form['waktu_jumlah']

        cursor = mysql.connection.cursor()
        cursor.execute('''
            INSERT INTO recordings (id_jumlahTransportasi, jumlahTransportasi, waktu_jumlah)
            VALUES (%s, %s, %s)''', 
            (id_jumlahTransportasi, jumlahTransportasi, waktu_jumlah)
        )

        mysql.connection.commit()
        logging.info(f"Data successfully added with  id_jenisTransportasi: { id_jumlahTransportasi}")
        return jsonify(status='success', message='Data successfully added.', data={"id_jumlahTransportasi": id_jumlahTransportasi})
    except Exception as e:
        logging.error(f"Error adding data: {str(e)}")
        return jsonify(status='error', message=str(e))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')