import mysql.connector

class DatabaseManager:
    def __init__(self):
        # Konfigurasi koneksi ke database MySQL
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Ganti dengan nama pengguna Anda
            password=" ",  # Ganti dengan kata sandi Anda
            database="VehiScanner"  # Ganti dengan nama database yang Anda gunakan
        )
        self.cursor = self.connection.cursor()

    def get_all_transportation_data(self):
        # Eksekusi pernyataan SQL untuk mengambil semua data transportasi dari database
        query = """
            SELECT jt.jenisTransportasi, jt.waktu, jt.id_images, jtj.jumlahTransportasi, jtj.waktu
            FROM jenisTransportasi AS jt
            JOIN jumlahTransportasi AS jtj ON jt.id_jenisTransportasi = jtj.id_jenisTransportasi
            ORDER BY jt.waktu DESC
        """
        self.cursor.execute(query)
        transportation_data = self.cursor.fetchall()

        return transportation_data

    def close_connection(self):
        # Menutup koneksi ke database MySQL
        self.connection.close()