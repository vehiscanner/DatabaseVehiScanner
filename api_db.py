import pandas as pd
from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Routes for the database
@app.route('/ambildata', methods=['GET'])
def ambil_data():
    conn = sqlite3.connect('vehiapp_dummy.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM jenis')
    rows = cursor.fetchall()
    conn.close()

    jenis_data = []
    for row in rows:
        jenis_data.append({
            'id': row[0],
            'jenistransportasi': row[1],
            'jumlahtransportasi': row[2],
            'panjang_jenistransportasi': row[3],
            'lebar_jenistransportasi': row[4]
        })

    # Processing data retrieved from the database
    df = pd.DataFrame(jenis_data)
    return df.to_json

@app.route('/store', methods=['POST'])
def store_data():
    # Connect to the database
    conn = sqlite3.connect('vehiapp_dummy.db')
    cursor = conn.cursor()

    # Get the data from the request
    id = request.form.get('id')
    jenistransportasi = request.form.get('jenistransportasi')
    jumlahtransportasi = request.form.get('jumlahtransportasi')
    panjang_jenistransportasi = request.form.get('panjang_jenistransportasi')
    lebar_jenistransportasi = request.form.get('lebar_jenistransportasi')

    # Check if required fields are present
    if None in (id, jenistransportasi, jumlahtransportasi, panjang_jenistransportasi, lebar_jenistransportasi):
        return 'Missing required fields', 400

    cursor.execute("INSERT INTO jenistransportasi (id, jenistransportasi, jumlahtransportasi, panjang_jenistransportasi, lebar_jenistransportasi) VALUES (?, ?, ?, ?, ?)",
                   (id, jenistransportasi, jumlahtransportasi, panjang_jenistransportasi, lebar_jenistransportasi))

    # Commit the changes to the database
    conn.commit()

    # Close the connection
    conn.close()

    return 'Data stored in the database'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)