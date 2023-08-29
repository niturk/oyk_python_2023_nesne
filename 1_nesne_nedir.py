def bmw_kornasi():
    print("BMW kornası çalıyor...")


def mercedes_kornasi():
    print("Mercedes kornası çalıyor...")


def korna_cal(araba):
    if araba == "BMW":
        bmw_kornasi()
    elif araba == "Mercedes":
        mercedes_kornasi()
    else:
        print("Bu arabanın kornası yok!")


arabalar = ["BMW", "Mercedes", "Opel", "Mazda"]
araba_index = int(input("Araba seçiniz: "))
araba = arabalar[araba_index]


korna_cal(araba)
