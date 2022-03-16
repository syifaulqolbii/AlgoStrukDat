class jajargenjang:
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t

    def luas(self):
        l = self.alas*self.tinggi
        return l


jajargenjang1 = jajargenjang(10, 5)

print(jajargenjang1.luas())


class Segitiga():
    def __init__(self, al, tg):
        self.alas = al
        self.tinggi = tg

    def __str__(self):
        return "Segitiga dengan alas {} dan tinggi {}".format(self.alas, self.tinggi)


segitiga1 = Segitiga(20, 10)
print("Alas segitiga 1:", segitiga1.alas)
print("Tinggi segitiga 1:", segitiga1.tinggi)
segitiga2 = Segitiga(3, 5)
print("Segitiga2 adalah", segitiga2)


class Segitigaku(Segitiga):
    def luas(self):
        return 0.5 * self.alas * self.tinggi


segitiga_abc = Segitigaku(10, 6)
print(segitiga_abc)
print("memiliki luas")
print(segitiga_abc.luas())
