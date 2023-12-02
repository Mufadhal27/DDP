def duplikat(buah):
    fruits_duplikat = [buah for buah in buah for _ in range(2)]
    return fruits_duplikat

buah = ["pepaya", "mangga", "pisang", "durian", "jambu"]
duplikat_buah = duplikat(buah)
print(duplikat_buah)