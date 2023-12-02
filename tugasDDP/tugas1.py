def balikan(buah):
    buah_balik = []
    for i in range(int(len(buah))-1,-1,-1):
        buah_balik.append(buah[i])
    return buah_balik

buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
buah_balik = balikan(buah)
print(buah_balik)

