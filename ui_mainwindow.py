# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(497, 447)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 481, 371))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 12, 0, 1, 2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.id_lineEdit = QLineEdit(self.groupBox)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout.addWidget(self.id_lineEdit, 0, 1, 1, 1)

        self.agregar_final_pushButton = QPushButton(self.groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout.addWidget(self.agregar_final_pushButton, 10, 0, 1, 2)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)

        self.agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout.addWidget(self.agregar_inicio_pushButton, 11, 0, 1, 2)

        self.salida = QPlainTextEdit(self.groupBox)
        self.salida.setObjectName(u"salida")

        self.gridLayout.addWidget(self.salida, 0, 2, 13, 1)

        self.origen_x_spinBox = QSpinBox(self.groupBox)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")

        self.gridLayout.addWidget(self.origen_x_spinBox, 1, 1, 1, 1)

        self.origen_y_spinBox = QSpinBox(self.groupBox)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")

        self.gridLayout.addWidget(self.origen_y_spinBox, 2, 1, 1, 1)

        self.destino_x_spinBox = QSpinBox(self.groupBox)
        self.destino_x_spinBox.setObjectName(u"destino_x_spinBox")

        self.gridLayout.addWidget(self.destino_x_spinBox, 3, 1, 1, 1)

        self.destino_y_spinBox = QSpinBox(self.groupBox)
        self.destino_y_spinBox.setObjectName(u"destino_y_spinBox")

        self.gridLayout.addWidget(self.destino_y_spinBox, 4, 1, 1, 1)

        self.velocidad_spinBox = QSpinBox(self.groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")

        self.gridLayout.addWidget(self.velocidad_spinBox, 5, 1, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")

        self.gridLayout.addWidget(self.red_spinBox, 7, 1, 1, 1)

        self.green_spinBox = QSpinBox(self.groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")

        self.gridLayout.addWidget(self.green_spinBox, 8, 1, 1, 1)

        self.blue_spinBox = QSpinBox(self.groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")

        self.gridLayout.addWidget(self.blue_spinBox, 9, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 497, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Capturar particulas", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen en y", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en x", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Color (rgb)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino en x", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar final", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Green ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino en y", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
    # retranslateUi

