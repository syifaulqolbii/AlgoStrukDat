# prodi = "Informatika"


# def isiKRS(nim):
#     pesan = "Mahasiswa prodi " + prodi + " dengan NIM : " + nim + " telah mengisi KRS"
#     return pesan


# def cetakKHS(nim):
#     pesan = "Mahasiswa prodi "+prodi+" dengan nim : " + nim + " telah mencetak KHS"
#     return pesan


# print(isiKRS("SQ1912"))
# print(cetakKHS("SQ1912"))

# def luas(p, l):
#     """ menghitung luas persegi panjang """
#     luas = p * l
#     return luas


# print(luas(10, 5))

# def lk(r):
#     """menghitung luas dan keliling lingkaran"""
#     luas = 3.14 * r * r
#     keliling = 2*3.14*r
#     return keliling, luas


# print(lk(4))

# def balok(p, l=2, t=3):
#     """mengembalikan volume dan luas"""
#     vol = p * l*t
#     luas = 2 * p * l + 2 * p * t + 2 * l * t
#     return vol, luas


# print(balok(l=1))


def factorial_recursive(n):
    print(n)
    return n * factorial_recursive(n-1)


print(factorial_recursive(4))
