import mysql.connector
from datetime import datetime

# Inisialisasi koneksi ke database MySQL
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",  # Ganti dengan nama pengguna Anda
    password=" ",  # Ganti dengan kata sandi Anda
    database="VehiScanner"  # Ganti dengan nama database yang Anda gunakan
)
db_cursor = db_connection.cursor()

class BotResponses:
    def _init_(self):
        pass

    def process_image_upload(self, image_path):
        # Simpan gambar yang diunggah oleh pengguna
        uploaded_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")  # Tanggal dan waktu saat ini
        insert_image_query = "INSERT INTO images (path_images, uploaded_date) VALUES (%s, %s)"
        image_data = (image_path, uploaded_date)

        db_cursor.execute(insert_image_query, image_data)
        db_connection.commit()

        return "Gambar kendaraan berhasil diunggah."

    def get_transportation_by_type(self, jenis_transportasi):
        # Query database untuk mendapatkan informasi kendaraan berdasarkan jenis
        select_query = "SELECT jumlahTransportasi, waktu FROM jumlahTransportasi WHERE id_jenisTransportasi = (SELECT id_jenisTransportasi FROM jenisTransportasi WHERE jenisTransportasi = %s)"
        db_cursor.execute(select_query, (jenis_transportasi,))
        result = db_cursor.fetchall()

        if result:
            bot_response = f"Informasi kendaraan jenis {jenis_transportasi}:"
            for row in result:
                bot_response += f"\nJumlah: {row[0]}, Waktu: {row[1]}"
        else:
            bot_response = f"Tidak ada informasi kendaraan untuk jenis {jenis_transportasi}."

        return bot_response

    def get_total_transportation(self):
        # Query database untuk mendapatkan jumlah total kendaraan
        select_query = "SELECT jenisTransportasi, SUM(jumlahTransportasi) FROM jumlahTransportasi GROUP BY jenisTransportasi"
        db_cursor.execute(select_query)
        result = db_cursor.fetchall()

        if result:
            bot_response = "Total jumlah kendaraan:"
            for row in result:
                bot_response += f"\nJenis: {row[0]}, Jumlah: {row[1]}"
        else:
            bot_response = "Tidak ada data jumlah kendaraan."

        return bot_response

# Contoh penggunaan:

# Inisialisasi objek BotResponses
bot = BotResponses()

# Contoh pengunggahan gambar kendaraan
image_path = "path_ke_gambar_kendaraan.jpg"
upload_response = bot.process_image_upload(image_path)
print(upload_response)

# Contoh pengambilan informasi kendaraan berdasarkan jenis
jenis_transportasi = "Mobil"
jenis_response = bot.get_transportation_by_type(jenis_transportasi)
print(jenis_response)

# Contoh pengambilan total jumlah kendaraan
total_response = bot.get_total_transportation()
print(total_response)

# Menutup koneksi ke database MySQL
db_connection.close()