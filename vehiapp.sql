--DATABASE DESKTOP
CREATE DATABASE IF NOT EXISTS vehiapp;
USE vehiapp;

--Tabel 'jenis'
CREATE TABLE IF NOT EXISTS jenis(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    jenistransportasi VARCHAR(20),
    jumlahtransportasi INT(10),
    panjang_jenistransportasi VARCHAR(20),
    lebar_jenistransportasi VARCHAR(20)
);