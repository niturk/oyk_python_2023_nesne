class Arac:
    def __init__(self, marka, model, rengi):
        self.marka = marka
        self.model = model
        self.rengi = rengi

    def marka_yaz(self):
        print(self.__class__.__name__, self.marka)


class Motor(Arac):
    pass


class Araba(Arac):
    pass


# ilk_arabam = None
# Araba.__init__(ilk_arabam, "BMW", "X5", "Siyah")

# print(ilk_arabam.marka)

ilk_arabam = Araba("BMW", "X5", "Siyah")
ilk_motor = Motor("Honda", "CBR", "Kırmızı")
# ilk_listem = list(1, 2, 3)

ilk_arabam.marka_yaz()
ilk_motor.marka_yaz()
