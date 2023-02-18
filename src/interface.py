from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(342, 314)
        self.centralwidget = QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.isClose = False

        # Logo
        self.sdLogo = QLabel(self)
        self.sdLogo.setText("SD")
        self.sdLogo.setObjectName("sdLogo")
        self.sdLogo.move(120, 20)
        self.sdLogo.resize(65, 50)

        # Tel No
        self.number = QLineEdit(self)
        self.number.setPlaceholderText("Ornek: 5555555555")
        self.number.setObjectName("number")
        self.number.move(80, 110)
        self.number.resize(150, 30)

        # adet
        self.adet = QLineEdit(self)
        self.adet.setPlaceholderText("Ornek: 100")
        self.adet.setObjectName("adet")
        self.adet.move(80, 160)
        self.adet.resize(150, 30)

        # Gonder Butonu
        self.gonder = QPushButton(self)
        self.gonder.setText("Bomber")
        self.gonder.setObjectName("gonder")
        self.gonder.move(100, 210)
        self.gonder.resize(110, 30)

        # iptal Butonu
        self.iptalBtn = QPushButton(self)
        self.iptalBtn.setText("Iptal")
        self.iptalBtn.setObjectName("iptal")
        self.iptalBtn.move(100, 250)
        self.iptalBtn.resize(110, 30)
        self.iptalBtn.isEnabled = False

        # Gonderilen Sms
        self.gonderilenSms = QLabel(self)
        self.gonderilenSms.setText("Gonderilen Sms: 0")
        self.gonderilenSms.setObjectName("gonderilenSms")
        self.gonderilenSms.move(90, 300)
        self.gonderilenSms.resize(200, 20)
        self.gonderilenSms.hide()

        # Bitis
        self.bitisLbl = QLabel(self)
        self.bitisLbl.setText("Bomber Bitti")
        self.bitisLbl.setObjectName("bitisLbl")
        self.bitisLbl.move(110, 325)
        self.bitisLbl.resize(200, 20)
        self.bitisLbl.hide()

