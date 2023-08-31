from random import randint

from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget

app = QApplication()

pencere = QWidget()
pencere_listesi = []


def pencere_ac():
    pencere2 = QWidget()
    pencere2.setWindowTitle("İkinci Arayüz")
    pencere_listesi.append(pencere2)

    rastgele_sayi = randint(0, 100)
    label = QLabel(str(rastgele_sayi), pencere2)

    pencere2.show()


def pencereleri_kapat():
    pencere_listesi.clear()


button1 = QPushButton("2. Pencereyi Ac", pencere)
button1.move(10, 10)
button1.clicked.connect(pencere_ac)

button_pencereleri_kapat = QPushButton("Pencereleri Kapat", pencere)
button_pencereleri_kapat.move(10, 30)
button_pencereleri_kapat.clicked.connect(pencereleri_kapat)

pencere.show()
app.exec()
