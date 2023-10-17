import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="vehiscanner"
        )
        self.cursor = self.conn.cursor(buffered=True)

    def insert_jenisTransportasi(self, jenisTransportasi_name):
        # Insert data into the "jenisTransportasi" table
        sql = "INSERT INTO jenisTransportasi (jenisTransportasi) VALUES (%s)"
        values = (jenisTransportasi_name,)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def insert_images(self, path):
        # Insert data into the "images" table
        sql = "INSERT INTO images (path_images) VALUES (%s)"
        values = (path,)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def insert_jumlahTransportasi_data(self, id_jumlahTransportasi, jumlahTransportasi, waktu, id_images, id_jenisTransportasi):
        # Insert data into the "jumlahTransportasi" table
        sql = "INSERT INTO jumlahTransportasi (id_jumlahTransportasi, jumlahTransportasi, waktu, id_images, id_jenisTransportasi) VALUES (%s, %s, %s, %s, %s)"
        values = (id_jumlahTransportasi, jumlahTransportasi, waktu, id_images, id_jenisTransportasi)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def get_jenisTransportasi_by_id(self, jenisTransportasi_id):
        # Mengambil data jenisTransportasi berdasarkan ID
        sql = "SELECT * FROM jenisTransportasi WHERE id_jenisTransportasi = %s"
        values = (jenisTransportasi_id,)
        self.cursor.execute(sql, values)
        return self.cursor.fetchone()

    def get_images_by_id(self, image_id):
        # Mengambil data images berdasarkan ID
        sql = "SELECT * FROM images WHERE id_images = %s"
        values = (image_id,)
        self.cursor.execute(sql, values)
        return self.cursor.fetchone()

    def get_jumlahTransportasi_data_by_id(self, jumlahTransportasi_id):
        # Mengambil data jumlahTransportasi berdasarkan ID
        sql = "SELECT * FROM jumlahTransportasi WHERE id_jumlahTransportasi = %s"
        values = (jumlahTransportasi_id,)
        self.cursor.execute(sql, values)
        return self.cursor.fetchone()
    
    def get_jenisTransportasi_all(self):
        # Mengambil data jenisTransportasi berdasarkan ID
        sql = "SELECT * FROM jenisTransportasi"
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_jumlahTransportasi_data_all(self, jumlahTransportasi_id):
        # Mengambil data jumlahTransportasi berdasarkan ID
        sql = "SELECT * FROM jumlahTransportasi"
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()