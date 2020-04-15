# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import qrc


class AboutForm(object):
    def setupUi(self, AboutForm):
        AboutForm.setObjectName("AboutForm")
        AboutForm.setWindowModality(QtCore.Qt.WindowModal)
        AboutForm.setEnabled(True)
        AboutForm.resize(348, 530)
        AboutForm.aboutCloseButton = QtWidgets.QPushButton(AboutForm)
        AboutForm.aboutCloseButton.setGeometry(QtCore.QRect(250, 490, 85, 27))
        AboutForm.aboutCloseButton.setObjectName("aboutCloseButton")
        AboutForm.layoutWidget = QtWidgets.QWidget(AboutForm)
        AboutForm.layoutWidget.setGeometry(QtCore.QRect(20, 10, 310, 471))
        AboutForm.layoutWidget.setObjectName("layoutWidget")
        AboutForm.verticalLayout = QtWidgets.QVBoxLayout(AboutForm.layoutWidget)
        AboutForm.verticalLayout.setContentsMargins(0, 0, 0, 0)
        AboutForm.verticalLayout.setObjectName("verticalLayout")
        AboutForm.label = QtWidgets.QLabel(AboutForm.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        AboutForm.label.setFont(font)
        AboutForm.label.setObjectName("label")
        AboutForm.verticalLayout.addWidget(AboutForm.label)
        AboutForm.label_2 = QtWidgets.QLabel(AboutForm.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        AboutForm.label_2.setFont(font)
        AboutForm.label_2.setOpenExternalLinks(False)
        AboutForm.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        AboutForm.label_2.setObjectName("label_2")
        AboutForm.verticalLayout.addWidget(AboutForm.label_2)
        AboutForm.label_3 = QtWidgets.QLabel(AboutForm.layoutWidget)
        AboutForm.label_3.setMinimumSize(QtCore.QSize(0, 0))
        AboutForm.label_3.setObjectName("label_3")
        AboutForm.verticalLayout.addWidget(AboutForm.label_3)
        spacerItem = QtWidgets.QSpacerItem(20, 24, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        AboutForm.verticalLayout.addItem(spacerItem)
        AboutForm.label_4 = QtWidgets.QLabel(AboutForm.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        AboutForm.label_4.setFont(font)
        AboutForm.label_4.setTextFormat(QtCore.Qt.RichText)
        AboutForm.label_4.setWordWrap(False)
        AboutForm.label_4.setOpenExternalLinks(True)
        AboutForm.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        AboutForm.label_4.setObjectName("label_4")
        AboutForm.verticalLayout.addWidget(AboutForm.label_4)
        AboutForm.layoutWidget.raise_()
        AboutForm.aboutCloseButton.raise_()

        self.retranslateUi(AboutForm)
        QtCore.QMetaObject.connectSlotsByName(AboutForm)

    def retranslateUi(self, AboutForm):
        _translate = QtCore.QCoreApplication.translate
        AboutForm.setWindowTitle(_translate("AboutForm", "About"))
        AboutForm.aboutCloseButton.setText(_translate("AboutForm", "Close"))
        AboutForm.label.setText(_translate("AboutForm", "<html><head/><body><p align=\"center\"><img src=\":/image/image/tray_icon.png\"/></p></body></html>"))
        AboutForm.label_2.setText(_translate("AboutForm", "<html><head/><body><p align=\"center\">Wallpaper Rotator Plus</p></body></html>"))
        AboutForm.label_3.setText(_translate("AboutForm", "<html><head/><body><p align=\"center\">0.0.1</p></body></html>"))
        AboutForm.label_4.setText(_translate("AboutForm", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Copyright © 2017 Pavel Adrianov</span></p><p align=\"center\"><a href=\"mailto:pavel@adrianov.pro\"><span style=\" font-size:9pt; text-decoration: underline; color:#0000ff;\">pavel@adrianov.pro</span></a></p><p align=\"center\"><a href=\"https://github.com/adrianoff/wallpaper-rotator-plus\"><span style=\" font-size:9pt; text-decoration: underline; color:#0000ff;\">https://github.com/adrianoff/wallpaper-rotator-plus</span></a></p><p align=\"center\"><span style=\" font-size:9pt;\">This program comes with absolutely no warranty.</span></p><p align=\"center\"><span style=\" font-size:9pt;\">See the </span><a href=\"https://opensource.org/licenses/MIT\"><span style=\" font-size:9pt; text-decoration: underline; color:#0000ff;\">MIT License</span></a><span style=\" font-size:9pt;\"> for details.</span></p></body></html>"))
