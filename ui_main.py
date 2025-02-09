# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(902, 501)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico_file/sourcefile/title.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QLabel{\n"
"    color: rgb(0, 0, 127);\n"
"    font: 12pt \"Microsoft Sans Serif\";\n"
"}\n"
"QComboBox{\n"
"    font: 14pt \"Microsoft Sans Serif\";\n"
"}\n"
"QLineEdit{\n"
"font: 11pt \"Microsoft Sans Serif\";\n"
"}\n"
"QTableView{\n"
"    border-color: rgb(0, 85, 0);\n"
"    \n"
"    alternate-background-color: rgb(230, 201, 255);\n"
"    background-color: rgb(199, 205, 255);\n"
"/*    selection-background-color: rgb(85, 255, 0);*/\n"
"\n"
"}\n"
"QPushButton{\n"
"    /*background-color: rgb(170, 255, 127);*/\n"
"    \n"
"    font: 16pt \"Microsoft Sans Serif\";\n"
"    \n"
"    background-color: rgb(239, 239, 119);\n"
"}\n"
"QCheckBox{\n"
"font: 12pt \"Microsoft Sans Serif\";\n"
"    color: rgb(255, 85, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Language = QtWidgets.QLabel(self.centralwidget)
        self.label_Language.setObjectName("label_Language")
        self.horizontalLayout.addWidget(self.label_Language)
        self.comboBox_Language = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Language.setObjectName("comboBox_Language")
        self.comboBox_Language.addItem("")
        self.comboBox_Language.addItem("")
        self.comboBox_Language.addItem("")
        self.comboBox_Language.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_Language)
        self.horizontalLayout_7.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Amount = QtWidgets.QLabel(self.centralwidget)
        self.label_Amount.setObjectName("label_Amount")
        self.horizontalLayout_3.addWidget(self.label_Amount)
        self.comboBox_Amount = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Amount.setObjectName("comboBox_Amount")
        self.comboBox_Amount.addItem("")
        self.comboBox_Amount.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_Amount)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_Payable_to = QtWidgets.QLabel(self.centralwidget)
        self.label_Payable_to.setObjectName("label_Payable_to")
        self.horizontalLayout_4.addWidget(self.label_Payable_to)
        self.comboBox_Payable_to_type = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Payable_to_type.setObjectName("comboBox_Payable_to_type")
        self.comboBox_Payable_to_type.addItem("")
        self.comboBox_Payable_to_type.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_Payable_to_type)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_Payable_by = QtWidgets.QLabel(self.centralwidget)
        self.label_Payable_by.setObjectName("label_Payable_by")
        self.horizontalLayout_5.addWidget(self.label_Payable_by)
        self.comboBox_Payable_by_type = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Payable_by_type.setObjectName("comboBox_Payable_by_type")
        self.comboBox_Payable_by_type.addItem("")
        self.comboBox_Payable_by_type.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_Payable_by_type)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_Output = QtWidgets.QLabel(self.centralwidget)
        self.label_Output.setObjectName("label_Output")
        self.horizontalLayout_6.addWidget(self.label_Output)
        self.comboBox_Output = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Output.setObjectName("comboBox_Output")
        self.comboBox_Output.addItem("")
        self.comboBox_Output.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_Output)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        spacerItem4 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem5 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Open_Data = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Open_Data.sizePolicy().hasHeightForWidth())
        self.pushButton_Open_Data.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_Open_Data.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/ITProg02/.designer/backup/sourcefile/open2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Open_Data.setIcon(icon1)
        self.pushButton_Open_Data.setObjectName("pushButton_Open_Data")
        self.horizontalLayout_2.addWidget(self.pushButton_Open_Data)
        self.label_file_path = QtWidgets.QLabel(self.centralwidget)
        self.label_file_path.setObjectName("label_file_path")
        self.horizontalLayout_2.addWidget(self.label_file_path)
        self.pushButton_Check = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Check.sizePolicy().hasHeightForWidth())
        self.pushButton_Check.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_Check.setFont(font)
        self.pushButton_Check.setIcon(icon1)
        self.pushButton_Check.setObjectName("pushButton_Check")
        self.horizontalLayout_2.addWidget(self.pushButton_Check)
        spacerItem6 = QtWidgets.QSpacerItem(13, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.pushButton_Process = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Process.sizePolicy().hasHeightForWidth())
        self.pushButton_Process.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_Process.setFont(font)
        self.pushButton_Process.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton_Process.setIcon(icon1)
        self.pushButton_Process.setObjectName("pushButton_Process")
        self.horizontalLayout_2.addWidget(self.pushButton_Process)
        self.label1_check = QtWidgets.QLabel(self.centralwidget)
        self.label1_check.setStyleSheet("")
        self.label1_check.setObjectName("label1_check")
        self.horizontalLayout_2.addWidget(self.label1_check)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 10)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.setStretch(4, 1)
        self.horizontalLayout_2.setStretch(5, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton_sample = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sample.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_sample.setStyleSheet("")
        self.pushButton_sample.setObjectName("pushButton_sample")
        self.verticalLayout.addWidget(self.pushButton_sample)
        self.pushButton_Data = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Data.setObjectName("pushButton_Data")
        self.verticalLayout.addWidget(self.pushButton_Data)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 7)
        self.verticalLayout.setStretch(4, 7)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 902, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.menu.setFont(font)
        self.menu.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menu.setToolTip("")
        self.menu.setWhatsThis("")
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiona = QtWidgets.QAction(MainWindow)
        self.actiona.setObjectName("actiona")
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.comboBox_Language.setCurrentIndex(0)
        self.comboBox_Amount.setCurrentIndex(0)
        self.comboBox_Payable_to_type.setCurrentIndex(0)
        self.comboBox_Payable_by_type.setCurrentIndex(0)
        self.comboBox_Output.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Swiss Payment part"))
        self.label_Language.setText(_translate("MainWindow", "語言"))
        self.comboBox_Language.setItemText(0, _translate("MainWindow", "de"))
        self.comboBox_Language.setItemText(1, _translate("MainWindow", "en"))
        self.comboBox_Language.setItemText(2, _translate("MainWindow", "fr"))
        self.comboBox_Language.setItemText(3, _translate("MainWindow", "it"))
        self.label_Amount.setText(_translate("MainWindow", "Amount "))
        self.comboBox_Amount.setItemText(0, _translate("MainWindow", "沒價錢 None"))
        self.comboBox_Amount.setItemText(1, _translate("MainWindow", "有價錢"))
        self.label_Payable_to.setText(_translate("MainWindow", "Payable to"))
        self.comboBox_Payable_to_type.setItemText(0, _translate("MainWindow", "S"))
        self.comboBox_Payable_to_type.setItemText(1, _translate("MainWindow", "K"))
        self.label_Payable_by.setText(_translate("MainWindow", "Payable by"))
        self.comboBox_Payable_by_type.setItemText(0, _translate("MainWindow", "S"))
        self.comboBox_Payable_by_type.setItemText(1, _translate("MainWindow", "K"))
        self.label_Output.setText(_translate("MainWindow", "輸出"))
        self.comboBox_Output.setItemText(0, _translate("MainWindow", "png"))
        self.comboBox_Output.setItemText(1, _translate("MainWindow", "pdf"))
        self.pushButton_Open_Data.setText(_translate("MainWindow", "打開資料"))
        self.label_file_path.setText(_translate("MainWindow", "文件"))
        self.pushButton_Check.setText(_translate("MainWindow", "檢查"))
        self.pushButton_Process.setText(_translate("MainWindow", "處理"))
        self.label1_check.setText(_translate("MainWindow", "................."))
        self.pushButton_sample.setText(_translate("MainWindow", "Sample payment part"))
        self.pushButton_Data.setText(_translate("MainWindow", "- Data payment part -"))
        self.menu.setTitle(_translate("MainWindow", "功能選項"))
        self.menu_2.setTitle(_translate("MainWindow", "系統"))
        self.actiona.setText(_translate("MainWindow", "設置打開文件路徑"))
import resourcefile_rc
