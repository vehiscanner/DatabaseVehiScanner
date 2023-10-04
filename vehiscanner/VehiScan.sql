CREATE DATABASE IF NOT EXISTS VehiScanner;
USE VehiScanner;

CREATE TABLE IF NOT EXISTS images (
  id_images INT AUTO_INCREMENT PRIMARY KEY,
  path_images VARCHAR(255),
  uploaded_date TIMESTAMP (6)
);

CREATE TABLE jenisTransportasi (
    id_jenisTransportasi INT AUTO_INCREMENT PRIMARY KEY,
    jenisTransportasi VARCHAR(20),
    waktu TIMESTAMP(6)
);

CREATE TABLE jumlahTransportasi (
    id_jumlahTransportasi INT AUTO_INCREMENT PRIMARY KEY,
    jumlahTransportasi INT(10),
    waktu TIMESTAMP(6),
    id_images INT,
    id_jenisTransportasi INT, 
    FOREIGN KEY (id_images) REFERENCES images(id_images),
    FOREIGN KEY (id_jenisTransportasi) REFERENCES jenisTransportasi(id_jenisTransportasi)
);