# from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton, QWidget

app = QApplication()

pencere = QWidget()
pencere.setWindowTitle("İlk Arayüz")
pencere.setStyleSheet("background-color: yellow")
# pencere.setWindowFlag(Qt.FramelessWindowHint)
pencere.setFixedSize(300, 400)

pencere_listesi = []


def pencere_ac():
    pencere2 = QWidget()
    pencere2.setWindowTitle("İkinci Arayüz")
    pencere_listesi.append(pencere2)
    pencere2.show()


button1 = QPushButton("2. Pencereyi Ac", pencere)
button1.move(10, 10)
button1.setStyleSheet("font-size:20px;")
button1.clicked.connect(pencere_ac)


def ekrana_yaz():
    print("Merhaba Dünya")


button2 = QPushButton("Cikis", pencere)
button2.move(200, 10)
button2.setStyleSheet("font-size:20px;")
button2.clicked.connect(ekrana_yaz)


pencere.show()

app.exec()
