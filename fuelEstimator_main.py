import sys
import webbrowser

from PyQt5.QtWidgets import *
from PyQt5.QtGui import  QIcon, QKeySequence, QColor, QCursor
from PyQt5 import QtGui, QtCore
from fuelEstimator_python import Ui_MainWindow
from login_python import Ui_Form
from qt_material import apply_stylesheet, QtStyleTools
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QEasingCurve
from predict_model import *
from Efekt import Effects

class login_screen(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.windows = []
        self.ui.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        vertical_layout = QVBoxLayout()
        self.setLayout(vertical_layout)
        self.ui.pushButton.clicked.connect(self.open_newWindow)




        self.ui.pushButton_2.clicked.connect(self.openwebBrowser)
        self.ui.pushButton_3.clicked.connect(self.openwebBrowser)
        self.ui.pushButton_4.clicked.connect(self.openwebBrowser)
        self.ui.pushButton_5.clicked.connect(self.openwebBrowser)

    def open_newWindow(self):
        apply_stylesheet(uygulama, theme='dark_teal.xml')
        window = fuelEstimator()
        self.ui.windows.append(window)
        window.show()
        self.close()

    def openwebBrowser(self):
        webbrowser.open('https://github.com/BerkKilicoglu')


class fuelEstimator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonHesapla.setShortcut(QKeySequence("F5"))
        self.ui.pushButtonHesapla.clicked.connect(self.pushButton_clicked_slot)

        self.ui.textMotorHacmi.setPlaceholderText("inc")
        self.ui.textBeygir.setPlaceholderText("horsepower hp")
        self.ui.textAgirlik.setPlaceholderText("lbs")
        self.ui.textYil.setPlaceholderText("modulo 100")

        self.ui.comboOrigin.addItem(QIcon("icons/abd.png"), "ABD", 1)
        self.ui.comboOrigin.addItem(QIcon("icons/eu.png"), "EU", 2)
        self.ui.comboOrigin.addItem(QIcon("icons/japan.png"), "Japan", 3)

        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Amc", 0)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Audi", 1)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Bmw", 2)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Buick", 3)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Cadillac", 4)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Capri", 5)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Chevrolet", 6)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Chrysler", 7)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Datsun", 8)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Dodge", 9)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Fiat", 10)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Ford", 11)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Harvester", 12)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Honda", 13)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Mazda", 14)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Mercedes", 15)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Mercury", 16)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Nissan", 17)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Oldsmobile", 18)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Opel", 19)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Peugeot", 20)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Plymouth", 21)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Pontiac", 22)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Renault", 23)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Saab", 24)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Subaru", 25)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Toyota", 26)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Triumph", 27)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Volkswagen", 28)
        self.ui.comboMarka.addItem(QIcon("icons/combocar.png"), "Volvo", 29)

        self.ui.labelSonuc.setText("<span style='font-size:12pt;'>Tahmini Fiyat</span>")
        self.ui.labelSonuc.setVisible(False)



    def pushButton_clicked_slot(self):
        #print("tuşa basıldı.")
        #print(PredictPerGalon(8,120,67,1850,14,80,3,4))
        brand = self.ui.comboMarka.currentData()
        origin = self.ui.comboOrigin.currentData()
        cylinders = self.ui.spinSilindir.value()
        acceleration = self.ui.spinIvme.value()
        displacement = self.ui.textMotorHacmi.toPlainText()
        displacement = int(displacement)
        horsepower = self.ui.textBeygir.toPlainText()
        horsepower = int(horsepower)
        weight = self.ui.textAgirlik.toPlainText()
        weight = int(weight)
        modelyear = self.ui.textYil.toPlainText()
        modelyear = int(modelyear)


        sonuc = PredictPerGalon(cylinders, displacement, horsepower, weight, acceleration,
                        modelyear, origin, brand)
        sonuc=round(sonuc,2)
        sonuc = str(sonuc)
        self.ui.labelSonuc.setVisible(True)

        self.ui.labelSonuc.setText("<span style='font-size:18pt; color:#1de9b6'>AI Estimated Value</span><br><span style='font-size:24pt;color:#f59c29;'>"
                                   + sonuc +"<span style='font-size:12pt; color:#f55429'> Miles Per Galon</span><br>")


if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = login_screen()
   # pencere.ui.label_7.hide()
    #Effects().EFEKT_FadeOut(pencere.ui.label_7, SURE=1000)
    Effects().EFEKT_FadeOut(pencere.ui.pushButton, SURE=2000)
   # Effects().EFEKT_Shadow(pencere.ui.pushButton,RENK=QColor(30,30,30)) # rgb 30,30,30 , black 0,0,0


    Effects().EFEKT_Move(pencere.ui.label_7, dX=0, dY=0,startX=-150,startY=-50, EasingCurve=QEasingCurve.InCurve)

    Effects().EFEKT_FadeOut(pencere,SURE=2000)
    pencere.show()
    sys.exit(uygulama.exec())