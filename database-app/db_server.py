import mysql.connector

# Membuat koneksi ke server MariaDB
class databaseManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            port=3306,
            password="",
            database="vehiscanner"   
        )
        self.cursor = self.conn.cursor() # Membuat objek kursor
    
    def save_data(self, data):
        placeholders = ', '.join(['%s'] * len(data))
        query = """
        INSERT INTO jumlahtransportasi(id_jumlahTransportasi, jumlahTransportasi, waktu, id_images, id_jenisTransportasi)
        VALUES(%s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, data)
        self.conn.commit()
    
    def get_jumlahtransportasi(self):
        try:
            query = "SELECT * FROM jumlahtransportasi"
            self.cursor.execute(query)

            jumlahtransportasi_data = self.cursor.fetchall()
            return jumlahtransportasi_data
        except Exception as e:
            print("Error:", e)
            return []

    def close_connection(self):
        self.connection.close() # Menutup koneksi
    