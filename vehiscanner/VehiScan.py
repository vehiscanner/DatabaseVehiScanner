import json
import sqlite3

class VehiScanner:
    def __init__(self):
        self.conn = sqlite3.connect("VehiScan.db")
        self.cursor = self.conn.cursor()


    def create_tables(self):
        with open('VehiScan.sql', 'r') as sqlfile:  #nama file dan pathnya harus sesuai
            sqlscript = sqlfile.read()
        self.cursor.executescript(sqlscript)
        self.conn.commit()  # menyimpan perubahan ke database


    def save_images(self,id_images,path_images,uploaded_date): 
        try: 
            self.cursor.execute("INSERT INTO images (id_images,path_images,uploaded_date) VALUES (?, ?, ?)", (id_images,path_images,uploaded_date))
            self.conn.commit()
            return True
        except Exception as e : 
            print("Error:", str(e))
            return False

    def save_jenisTransportasi(self, id_jenisTransportasi,jenisTransportasi,waktu): 
        try: 
            self.cursor.execute("INSERT INTO jenisTransportasi (id_jenisTransportasi,jenisTransportasi, waktu) VALUES (?, ?, ?)", (id_jenisTransportasi,jenisTransportasi,waktu))
            self.conn.commit()
            return True
        except Exception as e : 
            print("Error:", str(e))
            return False

    def save_jumlahTransportasi(self,id_jumlahTransportasi,jumlahTransportasi,waktu,id_images,id_jenisTransportasi): 
        try: 
            self.cursor.execute("INSERT INTO jumlahTransportasi (id_jumlahTransportasi,jumlahTransportasi,waktu,id_images,id_jenisTransportasi) VALUES (?, ?, ?, ?, ?)", (id_jumlahTransportasi,jumlahTransportasi,waktu,id_images,id_jenisTransportasi))
            self.conn.commit()
            return True
        except Exception as e : 
            print("Error:", str(e))
            return False