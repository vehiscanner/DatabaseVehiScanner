from flask import Flask, request, jsonify,render_template
import db_server as db

app = Flask(__name__)
db_manager = db.databaseManager()
#mengambil data dari tabel jumlahtransportasi

@app.route("/", methods =['GET'])
def hello():
    return jsonify(status="running")

@app.route('/datavehiscanner', methods=['GET'])
def data_vehiscanner():
    try:
        data_vehiscanner = db_manager.get_jumlahtransportasi()
        if not data_vehiscanner:
            return jsonify(message="Data not found"), 404

        # Menggunakan render_template untuk merender halaman HTML
        return jsonify(data_vehiscanner=data_vehiscanner)
    except Exception as e:
        return jsonify(error=str(e)), 500
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
