def klasifikasi_suhu(suhu):
    if suhu < 0:
        print("Membeku")
    elif suhu < 10:
        print("Sangat Dingin")
    elif suhu < 20:
        print("Sejuk")
    elif suhu < 30:
        print("Hangat")
    elif suhu < 40:
        print("Panas")
    else:
        print("Sangat Panas")

# Loop utama
while True:
    # Meminta input nilai suhu dari pengguna
    suhu = float(input("Masukkan nilai suhu (Celcius): "))

    # Menjalankan fungsi klasifikasi suhu
    klasifikasi_suhu(suhu)
    