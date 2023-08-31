import time
from random import randint

from PySide6.QtWidgets import QApplication, QMainWindow

from mainwindow import Ui_MainWindow

app = QApplication()

# self.txtEmail.text() -> email adresini alır

sistem_email = "nikita@qt.io"
sistem_parola = "12345"


class Pencere(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnLogin.clicked.connect(self.parola_kontrol_et)

    def parola_kontrol_et(self):
        email = self.txtEmail.text()
        parola = self.txtPassword.text()

        if email == sistem_email and parola == sistem_parola:
            print("Giriş başarılı")

            self.txtEmail.setVisible(False)
            self.txtPassword.setVisible(False)
            self.btnLogin.setVisible(False)
            self.label_4.setText("Hosgeldin " + email)

        else:
            time.sleep(5)
            print(f"Giriş başarısız {randint(1, 100)})")


pencere = Pencere()
pencere.show()

app.exec()
