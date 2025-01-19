"""
"""
#################实现自动先把ui 文件转为python 文件#################开始
import qt_ui_to_py
qt_ui_to_py.runMain()
#################实现自动先把ui 文件转为python 文件#################结束
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog,QAbstractItemView,QMessageBox
from PyQt5.QtCore import QModelIndex,Qt,QThread,pyqtSignal
# import configparser
import pandas as pd
import ui_main_epc
import sys
from py_epc_qr.transaction import epc_qr
import os

class BackendThread1(QThread):
    # 通过类成员对象定义信号对象
    update_date = pyqtSignal(str)
    progressBar_setRange=pyqtSignal(int)
    update_status = pyqtSignal(int)
    # 处理要做的业务逻辑
    def run(self):
        print("BackendThread1")
        fun_EPC_Generator1(df1,df1_index)
        self.update_date.emit('完成')
        self.update_status.emit(1)

class BackendThread2(QThread):
    # 通过类成员对象定义信号对象
    update_date = pyqtSignal(str)
    progressBar_setRange=pyqtSignal(int)
    update_status = pyqtSignal(int)
    # 处理要做的业务逻辑

    def run(self):
        print("BackendThread2")
        fun_EPC_Generator2(df2,df2_index)
        self.update_date.emit('完成')
        self.update_status.emit(1)


class mainwindow(QMainWindow):
    """
    主程序窗口
    """
    def __init__(self, Window):
        super().__init__()
        self.ui = ui_main_epc.Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_data()
        self.show()
        self.ui_event()

    def keyPressEvent(self,QKeyEvent):
        if QKeyEvent.modifiers() == Qt.ControlModifier and QKeyEvent.key() == Qt.Key_Q:
            self.quit()
            print('Ctrl+Q')
        if QKeyEvent.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and QKeyEvent.key() == Qt.Key_C:
            print('oooooo')



    def ui_event(self):
        """
        主窗口事件
        :return:
        """
        self.ui.pushButton_Open_Data.clicked.connect(self.fun_Open_Data)  # Open_Data
        # self.ui.pushButton_Check.clicked.connect(lambda: self.QR_thread(True))            #Check
        self.ui.pushButton_Process.clicked.connect(lambda: self.QR_thread(False))        #Process
        self.ui.comboBox_Version.currentTextChanged.connect(self.fun_Version)
        self.ui.comboBox_encoding.currentTextChanged.connect(self.fun_encoding)

    def load_data(self):
        self.Version='001'
        self.encoding = 2

    def quit(self):
        app1 = QApplication.instance()
        # 退出应用程序
        app1.quit()

    def fun_Open_Data(self):
        filelist, _ = QFileDialog.getOpenFileNames(
            self,  # 父窗口对象
            "选择要處理的檔案",  # 标题
            # r"./",  # 起始目录
            './',
            "數據類型 (*.xlsx;*.xls)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.ui.label_file_path.setText(filelist[0])
        self.JobPath = os.path.dirname(filelist[0])
        self.JobName, extension = os.path.splitext(os.path.basename(filelist[0]))
        self.file = filelist[0]
        print(self.JobName)



    def fun_Version(self):
        self.Version = self.ui.comboBox_Version.currentText()

    def fun_encoding(self):
        self.encoding=int(self.ui.comboBox_encoding.currentText())



    def QR_thread(self,check):
        print("QR_thread")
        self.ui.label1_check.setText('.................')
        self.ui.pushButton_Process.setEnabled(False)
        global df,df1,df2,df1_index,df2_index,df_count,check_status
        check_status=0
        if not os.path.isdir('./temp'):
            os.mkdir('./temp')
        if not os.path.isdir(self.JobPath+'/'+self.JobName):
            os.mkdir(self.JobPath+'/'+self.JobName)
        df1_index=0
        # file = pd.read_csv(self.file, dtype=str)  #, encoding="utf-8"
        file = pd.read_excel(self.file, dtype=str, sheet_name=0)
        df = pd.DataFrame(file)
        df = df.fillna('')
        df_count = 2 if (check or len(df) == 1) else len(df)
        df_count1 = int(df_count / 2)
        df2_index=df_count1
        # df1=df[0:df_count1].copy()
        # df2=df[df_count1:df_count+1].copy()

        df1 = df.truncate(before=0, after=df_count1-1, copy=True)
        df2 = df.truncate(before=df_count1, after=df_count-1, copy=True)

        self.backend1 = BackendThread1()
        # self.backend.update_date.connect(self.handle_data)
        # self.backend.progressBar_setRange.connect(self.setRange)
        self.backend1.update_status.connect(self.update_status1)
        self.backend1.start()
        if len(df) !=1:
            self.backend2 = BackendThread2()
            self.backend2.update_status.connect(self.update_status2)
            self.backend2.start()


    def update_status1(self,status1):
        global check_status
        check_status=check_status+status1
        print('update_status1:', check_status)
        if check_status==2 or len(df)==1:
            self.ui.pushButton_Process.setEnabled(True)
            self.ui.label1_check.setText('全部完成1!')



    def update_status2(self,status2):
        global check_status
        check_status=check_status+status2
        print('update_status2:', check_status)
        if check_status==2:
            self.ui.pushButton_Process.setEnabled(True)
            self.ui.label1_check.setText('全部完成2!')


def fun_EPC_Generator1(df,df_index):
    print('fun_EPC_Generator')
    OutputPath1 = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    for i in range(df_index,len(df)+df_index):
        outputpng1 = OutputPath1 + str(i + 1).strip() + ".png"
        epc_qr_bill1 = epc_qr(
            version=ui_mainwindow.Version,
            encoding=ui_mainwindow.encoding,
            bic=df['BIC'][i],
            beneficiary=df['Name'][i],
            iban=df['Iban'][i],
            amount=df['Amount'][i],
            purpose=df['Purpose'][i],
            remittance_structured=df['Reference'][i],
            remittance_unstructured=df['Remittance_Text'][i],
            originator_information=df['Information'][i]
        )
        epc_qr_bill1.to_qr(outputpng1)

def fun_EPC_Generator2(df,df_index):
    print('fun_EPC_Generator')
    OutputPath2 = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    for i in range(df_index,len(df)+df_index):
        outputpng2 = OutputPath2 + str(i + 1).strip() + ".png"
        epc_qr_bill2 = epc_qr(
            version=ui_mainwindow.Version,
            encoding=ui_mainwindow.encoding,
            bic=df['BIC'][i],
            beneficiary=df['Name'][i],
            iban=df['Iban'][i],
            amount=df['Amount'][i],
            purpose=df['Purpose'][i],
            remittance_structured=df['Reference'][i],
            remittance_unstructured=df['Remittance_Text'][i],
            originator_information=df['Information'][i]
        )
        epc_qr_bill2.to_qr(outputpng2)

if __name__ == '__main__':
    app = QApplication([])
    check_status = 0
    ui_mainwindow = mainwindow(QMainWindow())
    sys.exit(app.exec_())







