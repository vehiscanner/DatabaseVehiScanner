--DATABASE ML
CREATE DATABASE IF NOT EXISTS vehiscanner;
USE vehiscanner;

--Tabel 'video'
CREATE TABLE IF NOT EXISTS video (
  id_video INT AUTO_INCREMENT PRIMARY KEY,
  path_video VARCHAR(255)
);

--Tabel 'jenistransportasi'
CREATE TABLE jenistransportasi (
    id_jenistransportasi INT AUTO_INCREMENT PRIMARY KEY,
    jenistransportasi VARCHAR(20),
    panjang_jenistransportasi VARCHAR(20),
    lebar_jenistransportasi VARCHAR(20)
);

--Tabel 'jumlahtransportasi'
CREATE TABLE jumlahtransportasi (
    id_jumlahtransportasi INT AUTO_INCREMENT PRIMARY KEY,
    jumlahtransportasi INT(10),
    id_video INT,
    id_jenistransportasi INT, 
    FOREIGN KEY (id_video) REFERENCES video(id_video),
    FOREIGN KEY (id_jenistransportasi) REFERENCES jenistransportasi(id_jenistransportasi)
);