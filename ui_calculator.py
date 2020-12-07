#this code is created with QtDesigner 
#this file generates the UI for the calculator

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(445, 493)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(0, 240, 111, 51))
        self.pushButton_clear.setStyleSheet("")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_mrc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mrc.setGeometry(QtCore.QRect(110, 240, 111, 51))
        self.pushButton_mrc.setObjectName("pushButton_mrc")
        self.pushButton_persent = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_persent.setGeometry(QtCore.QRect(220, 240, 111, 51))
        self.pushButton_persent.setObjectName("pushButton_persent")
        self.pushButton_divd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_divd.setGeometry(QtCore.QRect(330, 240, 111, 51))
        self.pushButton_divd.setObjectName("pushButton_divd")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 290, 111, 51))
        self.pushButton_7.setStyleSheet("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(110, 290, 111, 51))
        self.pushButton_8.setStyleSheet("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(220, 290, 111, 51))
        self.pushButton_9.setStyleSheet("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_mult = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mult.setGeometry(QtCore.QRect(330, 290, 111, 51))
        self.pushButton_mult.setAutoFillBackground(False)
        self.pushButton_mult.setObjectName("pushButton_mult")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 340, 111, 51))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 340, 111, 51))
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 340, 111, 51))
        self.pushButton_6.setStyleSheet("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_sub = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sub.setGeometry(QtCore.QRect(330, 340, 111, 51))
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 431, 231))
        self.label.setStyleSheet("QLabel {\n"
"    qproperty-aligment: \"AlignVCenter | AlignRight\";\n"
"    border: 3px solid gray;\n"
"}\n"
"background-color : white;")
        self.label.setObjectName("label")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 390, 111, 51))
        self.pushButton_1.setStyleSheet("")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 390, 111, 51))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 390, 111, 51))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(330, 390, 111, 51))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(0, 440, 222, 51))
        self.pushButton_0.setStyleSheet("")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_deci = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_deci.setGeometry(QtCore.QRect(220, 440, 111, 51))
        self.pushButton_deci.setObjectName("pushButton_deci")
        self.pushButton_equals = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equals.setGeometry(QtCore.QRect(330, 440, 111, 51))
        self.pushButton_equals.setObjectName("pushButton_equals")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_clear.setText(_translate("MainWindow", "C"))
        self.pushButton_mrc.setText(_translate("MainWindow", "+/-"))
        self.pushButton_persent.setText(_translate("MainWindow", "%"))
        self.pushButton_divd.setText(_translate("MainWindow", "/"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_mult.setText(_translate("MainWindow", "X"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_sub.setText(_translate("MainWindow", "-"))
        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_deci.setText(_translate("MainWindow", "."))
        self.pushButton_equals.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
