def string_to_int(s: str):
    negatif = False
    if s[0] == '-':
        negatif = True
        s = s[1:]

    sonuc = 0

    for karakter in s:
        basamak = ord(karakter) - ord('0')
        sonuc = sonuc * 10 + basamak

    if negatif:
        sonuc = -sonuc

    return sonuc

def int_to_string(num: int):
    negatif = False
    if num < 0:
        negatif = True
        num = -num

    sonuc = []

    while num > 0:
        basamak = num % 10
        sonuc.append(chr(basamak + ord('0')))
        num //= 10
    
    if not sonuc:
        sonuc.append('0')

    if negatif:
        sonuc.append('-')

    return ''.join(reversed(sonuc))

def multiply(num1: str, num2: str) -> str:
    num1 = string_to_int(num1)
    num2 = string_to_int(num2)
    res = int_to_string(num1 * num2)
    return res
