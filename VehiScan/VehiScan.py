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


    def save_video(self,id_video,path_video): 
        try: 
            self.cursor.execute("INSERT INTO video (id_video,path_video) VALUES (?, ?)", (id_video,path_video))
            self.conn.commit()
            return True
        except Exception as e : 
            print("Error:", str(e))
            return False

    def save_jenisTransportasi(self, id_jenisTransportasi,jenisTransportasi,panjang_jenisTransportasi,lebar_jenisTransportasi): 
        try: 
            self.cursor.execute("INSERT INTO jenisTransportasi (id_jenisTransportasi,jenisTransportasi, panjang_jenisTransportasi,lebar_jenisTransportasi) VALUES (?, ?, ?, ?)", (id_jenisTransportasi,jenisTransportasi,panjang_jenisTransportasi,lebar_jenisTransportasi))
            self.conn.commit()
            return True
        except Exception as e : 
            print("Error:", str(e))
            return False

    def save_jumlahTransportasi(self,id_jumlahTransportasi,jumlahTransportasi,id_video,id_jenisTransportasi): 
        try: 
            self.cursor.execute("INSERT INTO jumlahTransportasi (id_jumlahTransportasi,jumlahTransportasi,id_video,id_jenisTransportasi) VALUES (?, ?, ?, ?)", (id_jumlahTransportasi,jumlahTransportasi,id_video,id_jenisTransportasi))
            self.conn.commit()
            return True
        except Exception as e : 
            print("Error:", str(e))
            return False