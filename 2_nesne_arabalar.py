# class Araba:
#     def korna_cal(self):
#         arabanin_adi = self.adi
#         print(f"{arabanin_adi} kornası çalıyor...")


# bmw = Araba()
# bmw.adi = "BMW"
# bmw.korna_cal()

# mercedes = Araba()
# mercedes.adi = "Mercedes"
# mercedes.korna_cal()

# liste = [1, 2, 3]

# liste.append(4)
# list.append(liste, 4)


class Araba:
    def __init__(self, ad):
        self.adi = ad

    def korna_cal(self):
        arabanin_adi = self.adi
        print(f"{arabanin_adi} kornası çalıyor...")


bmw = Araba("BMW")
bmw.korna_cal()

mercedes = Araba("Mercedes")
mercedes.korna_cal()
