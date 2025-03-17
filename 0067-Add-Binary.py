def addBinary(a: str, b: str) -> str:
    binary1 = a[::-1]
    binary2 = b[::-1]

    sonuc = []

    tasima = 0

    max_uzunluk = max(len(binary1), len(binary2))

    for i in range(max_uzunluk):
        basamak1 = int(binary1[i]) if i < len(binary1) else 0
        basamak2 = int(binary2[i]) if i < len(binary2) else 0

        toplam = basamak1 + basamak2 + tasima

        sonuc_b = toplam % 2
        tasima = toplam // 2

        sonuc.append(str(sonuc_b))

    if tasima:
        sonuc.append("1")

    sonuc.reverse()
    return "".join(sonuc)
