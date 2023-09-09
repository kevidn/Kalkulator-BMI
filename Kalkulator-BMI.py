# Meminta input dari User
berat = float(input("Masukkan berat badan anda (kg): "))
tinggi_cm = float(input("Masukkan tinggi badan anda (cm) : "))

# Mengubah centimeter menjadi meter
tinggi_m = tinggi_cm / 100

# Rumus BMI
bmi = round (berat / (tinggi_m * tinggi_m), 2)

# Menghasilkan BMI
print("BMI (Body Mass Index) anda adalah :", bmi)

# Menampilkan Hasil, Kategori, dan Solusi
if bmi < 18.5:
  print("Kurus")
  print("Solusi : Tingkatkan asupan kalori dengan makan makanan bergizi, lakukan latihan kekuatan, dan konsultasikan dengan ahli gizi.")
elif 18.5 <= bmi < 25:
  print("Ideal")
elif 25 <= bmi < 30:
  print("Gemuk")
  print("Solusi : Kurangi makanan berlemak dan gula, tingkatkan aktivitas fisik, pertimbangkan konsultasi dengan ahli gizi.")
else:
  print("Obesitas")
  print("Solusi : Konsultasikan dengan profesional medis, terapkan perubahan gaya hidup sehat, dan ikuti saran dokter.")
