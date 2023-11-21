import tkinter as tk
import sqlite3

# Fungsi untuk mendapatkan hasil prediksi
def hasil_prediksi():
    nama_siswa = entry_nama.get()
    nilai_biologi = int(entry_biologi.get())
    nilai_fisika = int(entry_fisika.get())
    nilai_inggris = int(entry_inggris.get())

    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prediksi = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prediksi = "Teknik"
    else:
        prediksi = "Bahasa"

    hasil.config(text=f"Prodi yang direkomendasikan: {prediksi}")

    simpan_ke_database(nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi)

# Fungsi untuk menyimpan data ke SQLite
def simpan_ke_database(nama_siswa, biologi, fisika, inggris, prediksi):
    connection = sqlite3.connect("latihanDB.db")
    cursor = connection.cursor()

    # Membuat table jika belum ada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
    ''')

    # Menyimpan data ke database
    cursor.execute("INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas) VALUES (?, ?, ?, ?, ?)",
                   (nama_siswa, biologi, fisika, inggris, prediksi))

    connection.commit()
    connection.close()

# Membuat Canvas
uiApp = tk.Tk()
uiApp.geometry("500x500")
uiApp.resizable(False,False)
uiApp.title("Input Nilai Mahsiswa")

# Membuat label judul
judul = tk.Label(uiApp, text="Aplikasi Prediksi Prodi Pilihan")
judul.pack()

# Membuat entry untuk nama siswa
label_nama = tk.Label(uiApp, text="Nama Siswa:")
label_nama.pack()
entry_nama = tk.Entry(uiApp)
entry_nama.pack()

# Membuat entry untuk nilai Biologi
label_biologi = tk.Label(uiApp, text="Nilai Biologi:")
label_biologi.pack()
entry_biologi = tk.Entry(uiApp)
entry_biologi.pack()

# Membuat entry untuk nilai Fisika
label_fisika = tk.Label(uiApp, text="Nilai Fisika:")
label_fisika.pack()
entry_fisika = tk.Entry(uiApp)
entry_fisika.pack()

# Membuat entry untuk nilai Inggris
label_inggris = tk.Label(uiApp, text="Nilai Inggris:")
label_inggris.pack()
entry_inggris = tk.Entry(uiApp)
entry_inggris.pack()

# Membuat tombol Hasil Prediksi
buttonSubmit = tk.Button(uiApp, text="Submit", command=hasil_prediksi)
buttonSubmit.pack()

# Membuat label luaran hasil produksi
hasil = tk.Label(uiApp, text="")
hasil.pack()

# Menjalankan aplikasi
uiApp.mainloop()
