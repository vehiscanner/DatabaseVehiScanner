CREATE DATABASE IF NOT EXISTS VehiScanner;
USE VehiScanner;

CREATE TABLE IF NOT EXISTS video (
  id_video INT AUTO_INCREMENT PRIMARY KEY,
  path_video VARCHAR(255)
);

CREATE TABLE jenisTransportasi (
    id_jenisTransportasi INT AUTO_INCREMENT PRIMARY KEY,
    jenisTransportasi VARCHAR(20),
    panjang_jenisTransportasi VARCHAR(20),
    lebar_jenisTransportasi VARCHAR(20)
);

CREATE TABLE jumlahTransportasi (
    id_jumlahTransportasi INT AUTO_INCREMENT PRIMARY KEY,
    jumlahTransportasi INT(10),
    id_video INT,
    id_jenisTransportasi INT, 
    FOREIGN KEY (id_video) REFERENCES video(id_video),
    FOREIGN KEY (id_jenisTransportasi) REFERENCES jenisTransportasi(id_jenisTransportasi)
);