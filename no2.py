print("menghitung luas bangun datar")
print("""
1. Menghitung luas persegi
2. Menghitung luas lingkaran
3. Menghitung luas segitiga
""")

luas = int(input("masukkan pilihan anda="))

match luas:
    case 1:
        sisi = int(input("masukkan sisi="))
        hasil = sisi * sisi * sisi
        print("hasil luas persegi=", hasil)
        
    case 2:
        jarijari = int(input("masukkan jari-jari="))
        hasil = 3.14 * jari-jari * jari-jari
        print("hasil luas lingkaran=", hasil)
        
    case 3:
        alas = int(input("masukkan alas="))
        tinggi = int(input("masukkan tinggi="))
        hasil = 1.2 * alas * tinggi
        print("hasil luas segitiga=", hasil)


