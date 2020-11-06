# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Pichau\Desktop\projeto\janelaprojeto.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 539)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Pichau\\Desktop\\projeto\\../icones/Subway-Car-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.framefundo = QtWidgets.QFrame(self.centralwidget)
        self.framefundo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.framefundo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framefundo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framefundo.setObjectName("framefundo")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.framefundo)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.framefundo)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)
        self.frameentrada = QtWidgets.QFrame(self.framefundo)
        self.frameentrada.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.frameentrada.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameentrada.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameentrada.setObjectName("frameentrada")
        self.gridLayout = QtWidgets.QGridLayout(self.frameentrada)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.labelOrigem = QtWidgets.QLabel(self.frameentrada)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.labelOrigem.setFont(font)
        self.labelOrigem.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.labelOrigem.setObjectName("labelOrigem")
        self.gridLayout_6.addWidget(self.labelOrigem, 0, 0, 1, 1)
        self.DestinolineEdit = QtWidgets.QLineEdit(self.frameentrada)
        self.DestinolineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DestinolineEdit.setObjectName("DestinolineEdit")
        self.gridLayout_6.addWidget(self.DestinolineEdit, 1, 1, 1, 1)
        self.labelDestino = QtWidgets.QLabel(self.frameentrada)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.labelDestino.setFont(font)
        self.labelDestino.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.labelDestino.setObjectName("labelDestino")
        self.gridLayout_6.addWidget(self.labelDestino, 1, 0, 1, 1)
        self.OrigemlineEdit = QtWidgets.QLineEdit(self.frameentrada)
        self.OrigemlineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OrigemlineEdit.setObjectName("OrigemlineEdit")
        self.gridLayout_6.addWidget(self.OrigemlineEdit, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.BotaoPesquisar = QtWidgets.QPushButton(self.frameentrada)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.BotaoPesquisar.setFont(font)
        self.BotaoPesquisar.setStyleSheet("background-color: rgb(138, 138, 138);\n"
"")
        self.BotaoPesquisar.setObjectName("BotaoPesquisar")
        self.gridLayout.addWidget(self.BotaoPesquisar, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frameentrada, 1, 0, 1, 1)
        self.Respostalabel = QtWidgets.QLabel(self.framefundo)
        self.Respostalabel.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.Respostalabel.setText("")
        self.Respostalabel.setObjectName("Respostalabel")
        self.gridLayout_4.addWidget(self.Respostalabel, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.framefundo, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menor Rota do Metro do Mexico CDMX"))
        self.label.setText(_translate("MainWindow", "Digite a Estação de Origem e Destino para Calcular a menor rota"))
        self.labelOrigem.setText(_translate("MainWindow", "Origem"))
        self.labelDestino.setText(_translate("MainWindow", "Destino"))
        self.BotaoPesquisar.setText(_translate("MainWindow", "Pesquisar Rota"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())