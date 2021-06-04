# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets

class QrGenerator(QtWidgets.QWidget):
    def __init__(self):
        super(QrGenerator, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(537, 376)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 521, 351))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.generate)

    def generate(self):
        import qrcode
        # Create qr code instance
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

        self.qr.add_data(self.lineEdit.text()+"\n")
        self.qr.add_data(self.lineEdit_2.text()+"\n")
        self.qr.add_data(self.lineEdit_3.text()+"\n")
        self.qr.make(fit=True)

        img = self.qr.make_image()

        # Save it somewhere, change the extension as needed:
        # img.save("image.png")
        # img.save("image.bmp")
        # img.save("image.jpeg")
        self.name = self.lineEdit.text() + ".jpg"
        img.save(self.name)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Генератор", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Введите имя сервера", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Введите Ip-адрес", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Выбрерите ОС", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "Сгенерировать  QR Code", None, -1))

def runPage():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    nw = QrGenerator()
    nw.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    runPage()
