from Gempa import Gempa

# Gempa pertama di Banten dengan skala 1.2
gempa_banten = Gempa("Banten", 1.2)

# Gempa kedua di Palu dengan skala 6.1
gempa_palu = Gempa("Palu", 6.1)

# Gempa ketiga di Cianjur dengan skala 5.6
gempa_cianjur = Gempa("Cianjur", 5.6)

# Gempa keempat di Jayapura dengan skala 3.3
gempa_jayapura = Gempa("Jayapura", 3.3)

# Gempa kelima di Garut dengan skala 4.0
gempa_garut = Gempa("Garut", 4.0)

# Panggil fungsi dampak() untuk masing-masing object gempa
gempa_banten.dampak()
gempa_palu.dampak()
gempa_cianjur.dampak()
gempa_jayapura.dampak()
gempa_garut.dampak()