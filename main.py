# import joblib

# # Membuka model menggunakan joblib
# with open('model.joblib', 'rb') as model_file:
#     loaded_model = joblib.load(model_file)

# # Membuat contoh data uji
# new_data = [[5.1, 3.5, 1.4, 0.2]]  # Isi data uji sesuai dengan jumlah fitur dari model

# # Melakukan prediksi dengan model yang telah dimuat
# prediction = loaded_model.predict(new_data)

# # Menampilkan hasil prediksi
# print(f"Prediksi Kelas: {prediction[0]}")

import pickle

# Membuka model menggunakan pickle
with open('model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Membuat contoh data uji
new_data = [[5.1, 3.5, 1.4, 0.2]]  # Isi data uji sesuai dengan jumlah fitur dari model

# Melakukan prediksi dengan model yang telah dimuat
prediction = loaded_model.predict(new_data)

# Menampilkan hasil prediksi
print(f"Prediksi Kelas: {prediction[0]}")