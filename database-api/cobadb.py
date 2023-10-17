import requests

# URL server Flask
server_url = "http://127.0.0.1:5000"  # Ganti dengan URL server yang sesuai

# Contoh data yang akan dikirim
jenisTransportasi_data = {"jenisTransportasi_name": "jenisTransportasi"}
image_data = {"image": ("1.jpeg", open("1.jpeg", "rb"))}
jumlahTransportasi_data = {
    "id_jumlahTransportasi":1, 
    "jumlahTransportasi": 1,
    "waktu": "2023-10-11 08:00:00",
    "id_images": 1,
    "id_jenisTransportasi": 1
}

# Mengirim data jenisTransportasi
response = requests.post(f"{server_url}/insert_jenisTransportasi", json=jenisTransportasi_data)
print("Response from /insert_jenisTransportasi:", response.json())

# Mengirim data gambar
response = requests.post(f"{server_url}/insert_images", files=image_data)
print("Response from /insert_images:", response.json())

# Mengirim data parking
response = requests.post(f"{server_url}/insert_jumlahTransportasi_data", json=jumlahTransportasi_data)
print("Response from /insert_jumlahTransportasi_data:", response.json())