import tkinter as tk
from tkinter import messagebox

# import package tkinter
from tkinter import *
import ttkbootstrap as ttk

def hitung_tensi_darah():
    try:
        sistolik = int(entry_sistolik.get())
        diastolik = int(entry_diastolik.get())

        if 90 <= sistolik < 120 and 60 <= diastolik < 80:
            status_tensi = "Normal"
            penjelasan_tensi = "Tekanan darah Anda berada dalam rentang normal."
            saran = "Lakukan pola hidup sehat, termasuk diet seimbang dan olahraga teratur. Pantau tekanan darah secara berkala."
        elif 120 <= sistolik < 139 or 80 <= diastolik < 89:
            status_tensi = "Prehipertensi"
            penjelasan_tensi = "Meskipun belum dianggap hipertensi, tekanan darah Anda sedikit tinggi. Pantau secara rutin."
            saran = "Terapkan perubahan gaya hidup sehat, termasuk diet rendah garam, berhenti merokok, dan meningkatkan aktivitas fisik."
        elif 140 <= sistolik < 159 or 90 <= diastolik < 99:
            status_tensi = "Hipertensi Tingkat 1"
            penjelasan_tensi = "Tekanan darah tinggi. Konsultasikan dengan dokter untuk perawatan dan perubahan gaya hidup."
            saran = "Ikuti saran dokter, mungkin termasuk pengaturan diet sehat, obat-obatan, dan perubahan gaya hidup."
        elif 160 <= sistolik < 179 or 100 <= diastolik < 109:
            status_tensi = "Hipertensi Tingkat 2"
            penjelasan_tensi = "Hipertensi tingkat lanjut. Perlukan perawatan medis segera."
            saran = "Konsultasikan segera dengan dokter. Perubahan gaya hidup dan penggunaan obat-obatan mungkin diperlukan."
        elif sistolik >= 180 or diastolik >= 110:
            status_tensi = "Hipertensi Tingkat 3"
            penjelasan_tensi = "Hipertensi darurat. Segera cari bantuan medis darurat."
            saran = "Segera hubungi layanan darurat. Dokter akan memberikan perawatan segera untuk mengurangi risiko komplikasi."
        elif sistolik <= 89 or diastolik <= 59:
            status_tensi = "Hipotensi"
            penjelasan_tensi = "Tekanan darah rendah. Perhatikan gejala dan konsultasikan dengan dokter jika diperlukan."
            saran = "Minum lebih banyak air, konsumsi garam dalam batas normal, bangun perlahan dari posisi duduk atau berbaring."
        else:
            status_tensi = "Tidak valid"
            penjelasan_tensi = ""
            saran = ""
        
        messagebox.showinfo("hasil", f"Tensi Darah: {sistolik}/{diastolik}\n\nStatus: {status_tensi}\n{penjelasan_tensi}\n\nSaran: {saran}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk sistolik dan diastolik.")

# Membuat GUI
app = ttk.Window(themename="morph")   
app.title("Kalkulator Tensi Darah")

# Label dan Entry untuk Sistolik
label_sistolik = tk.Label(app, text="Sistolik:")
label_sistolik.grid(row=0, column=0, padx=10, pady=10)
entry_sistolik = tk.Entry(app)
entry_sistolik.grid(row=0, column=1, padx=10, pady=10)

# Label dan Entry untuk Diastolik
label_diastolik = tk.Label(app, text="Diastolik:")
label_diastolik.grid(row=1, column=0, padx=10, pady=10)
entry_diastolik = tk.Entry(app)
entry_diastolik.grid(row=1, column=1, padx=10, pady=10)

# Tombol Hitung
button_hitung = tk.Button(app, text="Hitung", command=hitung_tensi_darah)
button_hitung.grid(row=2, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
app.mainloop()