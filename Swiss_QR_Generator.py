
#################实现自动先把ui 文件转为python 文件#################开始
import qt_ui_to_py
qt_ui_to_py.runMain()
#################实现自动先把ui 文件转为python 文件#################结束
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog,QAbstractItemView,QMessageBox
from PyQt5.QtCore import QModelIndex,Qt,QThread,pyqtSignal
import configparser
import pandas as pd

import ui_main
# import resourcefile
import fitz
import sys
from qrbill import QRBill
import os
# os.environ['path'] += r';./lib'
# import io
# import cairosvg
# from PIL import Image
# import datetime
import shutil

class BackendThread1(QThread):
    # 通过类成员对象定义信号对象
    update_date = pyqtSignal(str)
    progressBar_setRange=pyqtSignal(int)
    update_status = pyqtSignal(int)
    # 处理要做的业务逻辑
    def run(self):
        print("BackendThread1")
        if ui_mainwindow.Payable_to_type == "S" and ui_mainwindow.Payable_by_type == 'S' and ui_mainwindow.Amount == False:
            fun_QRBill_toSbyS_amountNone1(df1, df1_index)

        elif ui_mainwindow.Payable_to_type == "S" and ui_mainwindow.Payable_by_type == 'S' and ui_mainwindow.Amount == True:
            fun_QRBill_toSbyS_amount1(df1, df1_index)

        elif ui_mainwindow.Payable_to_type == "S" and ui_mainwindow.Payable_by_type == 'K' and ui_mainwindow.Amount == False:
            fun_QRBill_toSbyK_amountNone1(df1, df1_index)

        elif ui_mainwindow.Payable_to_type == "S" and ui_mainwindow.Payable_by_type == 'K' and ui_mainwindow.Amount == True:
            fun_QRBill_toSbyK_amount1(df1, df1_index)

        elif ui_mainwindow.Payable_to_type == "K" and ui_mainwindow.Payable_by_type == 'K' and ui_mainwindow.Amount == False:
            fun_QRBill_toKbyK_amountNone1(df1, df1_index)

        elif ui_mainwindow.Payable_to_type == "K" and ui_mainwindow.Payable_by_type == 'K' and ui_mainwindow.Amount == True:
            fun_QRBill_toKbyK_amount1(df1, df1_index)

        elif ui_mainwindow.Payable_to_type == "K" and ui_mainwindow.Payable_by_type == 'S' and ui_mainwindow.Amount == False:
            fun_QRBill_toKbyS_amountNone1(df1, df1_index)

        elif ui_mainwindow.Payable_to_type == "K" and ui_mainwindow.Payable_by_type == 'S' and ui_mainwindow.Amount == True:
            fun_QRBill_toKbyS_amount1(df1, df1_index)

        image_to_pushButton_Data()

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
        if ui_mainwindow.Payable_to_type == "S" and ui_mainwindow.Payable_by_type == 'S' and ui_mainwindow.Amount == False:
            fun_QRBill_toSbyS_amountNone2(df2, df2_index)

        elif ui_mainwindow.Payable_to_type == "S" and ui_mainwindow.Payable_by_type == 'S' and ui_mainwindow.Amount == True:
            fun_QRBill_toSbyS_amount2(df2, df2_index)

        elif ui_mainwindow.Payable_to_type == "S" and ui_mainwindow.Payable_by_type == 'K' and ui_mainwindow.Amount == False:
            fun_QRBill_toSbyK_amountNone2(df2, df2_index)

        elif ui_mainwindow.Payable_to_type == "S" and ui_mainwindow.Payable_by_type == 'K' and ui_mainwindow.Amount == True:
            fun_QRBill_toSbyK_amount2(df2, df2_index)

        elif ui_mainwindow.Payable_to_type == "K" and ui_mainwindow.Payable_by_type == 'K' and ui_mainwindow.Amount == False:
            fun_QRBill_toKbyK_amountNone2(df2, df2_index)

        elif ui_mainwindow.Payable_to_type == "K" and ui_mainwindow.Payable_by_type == 'K' and ui_mainwindow.Amount == True:
            fun_QRBill_toKbyK_amount2(df2, df2_index)

        elif ui_mainwindow.Payable_to_type == "K" and ui_mainwindow.Payable_by_type == 'S' and ui_mainwindow.Amount == False:
            fun_QRBill_toKbyS_amountNone2(df2, df2_index)

        elif ui_mainwindow.Payable_to_type == "K" and ui_mainwindow.Payable_by_type == 'S' and ui_mainwindow.Amount == True:
            fun_QRBill_toKbyS_amount2(df2, df2_index)

        self.update_date.emit('完成')
        self.update_status.emit(1)

class BackendThread3(QThread):
    # 通过类成员对象定义信号对象
    update_date = pyqtSignal(str)

    update_status = pyqtSignal()
    # 处理要做的业务逻辑

    def run(self):
        print("BackendThread3")
        if ui_mainwindow.Output=='png':
            Outputfile_PNG()
        else:
            Outputfile_PDF()
        self.update_date.emit('完成')


class mainwindow(QMainWindow):
    """
    主程序窗口
    """
    def __init__(self, Window):
        super().__init__()
        self.ui = ui_main.Ui_MainWindow()
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
        self.ui.pushButton_Check.clicked.connect(lambda: self.QR_thread(True))            #Check
        self.ui.pushButton_Process.clicked.connect(lambda: self.QR_thread(False))        #Process
        self.ui.comboBox_Language.currentTextChanged.connect(self.fun_Language)
        self.ui.comboBox_Payable_to_type.currentTextChanged.connect(self.fun_Payable_to_type)
        self.ui.comboBox_Output.currentTextChanged.connect(self.fun_Output)
        self.ui.comboBox_Payable_by_type.currentTextChanged.connect(self.fun_Payable_by_type)
        self.ui.comboBox_Amount.currentTextChanged.connect(self.fun_Amount)



    def quit(self):
        app1 = QApplication.instance()
        # 退出应用程序
        app1.quit()

    def fun_Output(self):
        self.Output=self.ui.comboBox_Output.currentText()

    def fun_Open_Data(self):
        filelist, _ = QFileDialog.getOpenFileNames(
            self,  # 父窗口对象
            "选择要處理的PDF檔",  # 标题
            # r"./",  # 起始目录
            self.File_path,
            "數據類型 (*.xlsx;*.xls)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.ui.label_file_path.setText(filelist[0])
        self.JobPath = os.path.dirname(filelist[0])
        self.JobName, extension = os.path.splitext(os.path.basename(filelist[0]))
        self.file = filelist[0]
        print(self.JobName)

    def fun_Language(self):
        if self.ui.comboBox_Language.currentText() == 'de':
            self.Language='de'
            # self.ui.pushButton_sample.setGeometry(0, 0, 710, 330)
            svg_file = "PaymentPart_de.png"
            icon = QIcon(svg_file)
            pixmap = icon.pixmap(QPixmap(svg_file).size())
            self.ui.pushButton_sample.setIcon(icon)
            self.ui.pushButton_sample.setIconSize(pixmap.size())
            self.ui.pushButton_sample.setFlat(True)  # 设置按钮为平面样式，这样它就不会有默认的边框和背景色
        elif self.ui.comboBox_Language.currentText() == 'en':
            self.Language = 'en'
            # self.ui.pushButton_sample.setGeometry(0, 0, 710, 330)
            svg_file = "PaymentPart_en.png"
            icon = QIcon(svg_file)
            pixmap = icon.pixmap(QPixmap(svg_file).size())
            self.ui.pushButton_sample.setIcon(icon)
            self.ui.pushButton_sample.setIconSize(pixmap.size())
            self.ui.pushButton_sample.setFlat(True)  # 设置按钮为平面样式，这样它就不会有默认的边框和背景色
        elif self.ui.comboBox_Language.currentText() == 'fr':
            self.Language = 'fr'
            # self.ui.pushButton_sample.setGeometry(0, 0, 710, 330)
            svg_file = "PaymentPart_fr.png"
            icon = QIcon(svg_file)
            pixmap = icon.pixmap(QPixmap(svg_file).size())
            self.ui.pushButton_sample.setIcon(icon)
            self.ui.pushButton_sample.setIconSize(pixmap.size())
            self.ui.pushButton_sample.setFlat(True)  # 设置按钮为平面样式，这样它就不会有默认的边框和背景色
        elif self.ui.comboBox_Language.currentText() == 'it':
            self.Language = 'it'
            # self.ui.pushButton_sample.setGeometry(0, 0, 710, 330)
            svg_file = "PaymentPart_it.png"
            icon = QIcon(svg_file)
            pixmap = icon.pixmap(QPixmap(svg_file).size())
            self.ui.pushButton_sample.setIcon(icon)
            self.ui.pushButton_sample.setIconSize(pixmap.size())
            self.ui.pushButton_sample.setFlat(True)  # 设置按钮为平面样式，这样它就不会有默认的边框和背景色

    def fun_Payable_to_type(self):
        self.Payable_to_type = self.ui.comboBox_Payable_to_type.currentText()

    def fun_Payable_by_type(self):
        self.Payable_by_type=self.ui.comboBox_Payable_by_type.currentText()

    def fun_Amount(self):
        if self.ui.comboBox_Amount.currentText() == '沒價錢 None':
            self.Amount = False
        else:
            self.Amount = True

    def load_data(self):
        config = configparser.ConfigParser()
        config.read("config.ini", "utf-8-sig")  # utf-8-sig  & UTF-8
        self.Language = config['DEFAULT']['Language']
        self.File_path = config['DEFAULT']['File_path']
        self.Payable_to_type = config['DEFAULT']['payable_to_type']
        self.Payable_by_type = config['DEFAULT']['payable_by_type']
        self.Output = config['DEFAULT']['Output']
        Amount_str = config['DEFAULT']['amount']
        if Amount_str=='沒價錢 None':
            self.Amount = False
        else:
            self.Amount = True
        print('File_path:', self.File_path)
        self.ui.comboBox_Language.setCurrentText(self.Language)
        self.ui.comboBox_Payable_to_type.setCurrentText(self.Payable_to_type)
        self.ui.comboBox_Payable_by_type.setCurrentText(self.Payable_by_type)
        self.ui.comboBox_Amount.setCurrentText(Amount_str)
        self.ui.comboBox_Output.setCurrentText(self.Output)
        iconfile = "PaymentPart_"+self.Language+".png"
        icon = QIcon(iconfile)
        pixmap = icon.pixmap(QPixmap(iconfile).size())
        self.ui.pushButton_sample.setIcon(icon)
        self.ui.pushButton_sample.setIconSize(pixmap.size())
        self.ui.pushButton_sample.setFlat(True)  # 设置按钮为平面样式，这样它就不会有默认的边框和背景色
        iconfile2 = "PaymentPart_blank.png"
        icon2 = QIcon(iconfile2)
        pixmap2 = icon2.pixmap(QPixmap(iconfile2).size())
        self.ui.pushButton_Data.setIcon(icon2)
        self.ui.pushButton_Data.setIconSize(pixmap2.size())
        self.ui.pushButton_Data.setFlat(True)  # 设置按钮为平面样式，这样它就不会有默认的边框和背景色


        # # 檢查是否在DEFAULT 里有Add_Sample項, 如果沒有就增加, 并保存. start
        # if not config.has_option("DEFAULT","Language"):
        #     config.set("DEFAULT","Language","de")
        # if not config.has_option("DEFAULT","Payable_to_type"):
        #     config.set("DEFAULT","Payable_to_type","S")
        # if not config.has_option("DEFAULT","Payable_by_type"):
        #     config.set("DEFAULT","Payable_by_type","K")
        # if not config.has_option("DEFAULT","Amount "):
        #     config.set("DEFAULT","Amount ","None")
        # if not config.has_option("DEFAULT","File_path "):
        #     config.set("DEFAULT","File_path ","D:/xu/Python/QRCodeGenerator")
        # with open('config.ini', 'w', encoding="utf-8-sig") as configfile:
        #     config.write(configfile)


    def image_to_pushButton_Data_bak1(self):
        #將第一張圖放到pushButton_Data里.
        pdfDoc = fitz.open('./temp/1.PDF')
        page = pdfDoc[0]
        mat = fitz.Matrix(1.3, 1.3)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        pix.save('./temp/1.png')  # 将图片写入指定的文件夹内
        # svg_file = "PaymentPart_de.png"
        icon = QIcon('./temp/1.png')
        pixmap = icon.pixmap(QPixmap('./temp/1.png').size())
        self.ui.pushButton_Data.setIcon(icon)
        self.ui.pushButton_Data.setIconSize(pixmap.size())
        self.ui.pushButton_Data.setFlat(True)  # 设置按钮为平面样式，这样它就不会有默认的边框和背景色

    def fun_mergePDF(self):
        print("fun_mergePDF")
        # doc1 = fitz.open('./temp/1.PDF')
        # width_total, height_total = doc1[0].mediabox_size
        # r1 = fitz.Rect(0, 0, width_total, height_total)
        # doc = fitz.open()
        # for d in range(1, df_count + 1):
        #     page = doc.new_page(-1, width=width_total, height=height_total)
        #
        #
        # for l in range(0, df_count):
        #     docc=fitz.open("./temp/"+str(l+1).strip()+".PDF")
        #     pagel = doc.load_page(l)
        #     pagel.show_pdf_page(r1, docc, 0, keep_proportion=1)
        #
        #
        # doc.save("./temp/merge.pdf", garbage=0, deflate=True)
        # print("merge.pdf")

    def fun_Check(self):
        print("fun_Check")
        self.fun_data_process(True)


    def QR_thread(self,check):
        print("QR_thread")
        self.ui.label1_check.setText('.................')
        self.ui.pushButton_Process.setEnabled(False)
        global df,df1,df2,df1_index,df2_index,df_count
        if not os.path.isdir('./temp'):
            os.mkdir('./temp')
        if not os.path.isdir(self.JobPath+'/'+self.JobName):
            os.mkdir(self.JobPath+'/'+self.JobName)
        df1_index=0
        import pandas as pd
        # file = pd.read_csv(self.file, dtype=str)  #, encoding="utf-8"
        file = pd.read_excel(self.file, dtype=str, sheet_name=0)
        df = pd.DataFrame(file)
        df = df.fillna('')
        if df['qr_type'][0]!='SPC' or df['version'][0]!='0200' or df['coding'][0]!='1':
            QMessageBox.information(ui_mainwindow, "異常警告!", "Swiss qr_type, version, coding 欄位內容不正確.")
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
        if len(df) != 1:
            self.backend2 = BackendThread2()
            self.backend2.update_status.connect(self.update_status2)
            self.backend2.start()


        # self.ui.process_tableView2.model().removeRows(0,ui_mainwindow.ui.process_tableView2.model().rowCount())
        # self.ui.open_pushButton1.setStyleSheet("background-color: rgb(239, 239, 119)")
        # self.ui.open_pushButton1.setEnabled(True)
        # self.ui.open_pushButton1.show()
        # self.ui.label_art.setText("no_art")

    def update_status1(self,status1):
        global check_status
        check_status=check_status+status1
        print('update_status1:', check_status)
        if check_status==2 or len(df)==1:
            self.backend3 = BackendThread3()
            self.backend3.start()

            # if os.path.isdir('./svg_'+self.JobName):
            #     shutil.rmtree('./svg_'+self.JobName)
            # os.rename('./temp','./svg_'+self.JobName)
            # self.ui.label1_check.setText('全部完成1!')



    def update_status2(self,status2):
        global check_status
        check_status=check_status+status2
        print('update_status2:', check_status)
        if check_status==2:
            self.backend3 = BackendThread3()
            self.backend3.start()

            # if os.path.isdir('./svg_'+self.JobName):
            #     shutil.rmtree('./svg_'+self.JobName)
            # os.rename('./temp', './svg_' + self.JobName)
            # self.ui.label1_check.setText('全部完成2!')


def Outputfile_PNG():
    print("OutputPNG")
    global df_count
    box = fitz.Rect(188, 47, 323, 182)  # pymupdf 方式
    OutputPath = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    if len(df)==1:
        df_count=1
    for i in range(0, df_count):
        outputsvg='./temp/'+str(i+1)+'.svg'
        outputpng = OutputPath + str(i + 1).strip() + ".png"
        xps = fitz.open(outputsvg)
        pdfbytes = xps.convert_to_pdf()
        imgpdf = fitz.open("pdf", pdfbytes)
        # pdf0 = imgpdf[0]
        pix = imgpdf[0].get_pixmap(clip=box, dpi=300)
        pix.save(outputpng)
    rename_folder()

def Outputfile_PDF():
    print("OutputPDF")
    global df_count
    r1 = fitz.Rect(0, 0, 130, 130)
    box = fitz.Rect(188, 47, 323, 182)  # pymupdf 方式
    OutputPath = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'

    doc = fitz.open()
    if len(df)==1:
        df_count=1
    for k in range(df_count):
        page = doc.new_page(-1, width=130, height=130)

    for i in range(0, df_count):
        outputsvg='./temp/'+str(i+1)+'.svg'
        outputpdf = OutputPath + "merge.pdf"
        xps = fitz.open(outputsvg)
        pdfbytes = xps.convert_to_pdf()
        imgpdf = fitz.open("pdf", pdfbytes)
        pix = imgpdf[0].get_pixmap(clip=box, dpi=300)
        page1 = doc.load_page(i)
        page1.insert_image(rect=r1, pixmap=pix)

    doc.save(outputpdf, garbage=0, deflate=True)
    rename_folder()


def rename_folder():
    global check_status
    if os.path.isdir('./svg_' + ui_mainwindow.JobName):
        shutil.rmtree('./svg_' + ui_mainwindow.JobName)
    os.rename('./temp', './svg_' + ui_mainwindow.JobName)
    ui_mainwindow.ui.pushButton_Process.setEnabled(True)
    check_status = 0
    ui_mainwindow.ui.label1_check.setText('處理完成!')


def image_to_pushButton_Data():
    outputsvg = './temp/1.svg'
    outputpng = './temp/sample.png'
    box = fitz.Rect(188, 47, 323, 182)  # pymupdf 方式
    xps = fitz.open(outputsvg)
    pdfbytes = xps.convert_to_pdf()
    imgpdf = fitz.open("pdf", pdfbytes)
    # pdf0 = imgpdf[0]
    pix = imgpdf[0].get_pixmap(dpi=95)
    pix.save(outputpng)

    icon = QIcon('./temp/sample.png')
    pixmap = icon.pixmap(QPixmap('./temp/sample.png').size())
    ui_mainwindow.ui.pushButton_Data.setIcon(icon)

    ui_mainwindow.ui.pushButton_Data.setIconSize(pixmap.size())
    ui_mainwindow.ui.pushButton_Data.setFlat(True)  # 设置按钮为平面样式，这样它就不会有默认的边框和背景色


def fun_QRBill_toSbyS_amountNone1(df,df_index):
    print('1.1 QRBill Payable to = S, Payable by = S 和沒有價錢的')
    OutputPath = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    box = (780, 195, 1345, 750)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标
    for i in range(df_index,len(df)+df_index):
        Payable_to = {'name': df['Payable_to_Name'][i], 'street': df['Payable_to_street'][i], 'house_num': df['Payable_to_house_num'][i], 'pcode': df['Payable_to_pcode'][i], 'city': df['Payable_to_city'][i], 'country': df['Payable_to_country'][i]}
        Payable_by = {'name': df['Payable_by_Name'][i], 'street': df['Payable_by_street'][i], 'house_num': df['Payable_by_house_num'][i], 'pcode': df['Payable_by_pcode'][i], 'city': df['Payable_by_city'][i], 'country': df['Payable_by_country'][i]}
        my_bill = QRBill(
            account=df['Account'][i],
            creditor=Payable_to,
            currency=df['currency'][i],
            amount=None,
            language=ui_mainwindow.Language,  # 'en', 'de', 'fr' or 'it'
            debtor=Payable_by,
            reference_number=df['Reference'][i],
            additional_information=df['additional_information'][i],
            top_line=False,
            payment_line=False,
            font_factor=1,  # 0 就不輸出文字, 1 輸出字體
        )
        outputsvg = './temp/' + str(i + 1).strip() + ".svg"
        my_bill.as_svg(outputsvg)

        # outputpng = OutputPath + str(i + 1).strip() + ".png"
        # png_data = cairosvg.svg2png(url=outputsvg, dpi=300)
        # image1 = Image.open(io.BytesIO(png_data))
        # cropped_image = image1.crop(box)
        # cropped_image.save(outputpng)

def fun_QRBill_toSbyS_amountNone2(df,df_index):
    print('1.2 QRBill Payable to = S, Payable by = S 和沒有價錢的')
    OutputPath = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    box2 = (780, 195, 1345, 750)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标
    for i in range(df_index,len(df)+df_index):
        Payable_to = {'name': df['Payable_to_Name'][i], 'street': df['Payable_to_street'][i], 'house_num': df['Payable_to_house_num'][i], 'pcode': df['Payable_to_pcode'][i], 'city': df['Payable_to_city'][i], 'country': df['Payable_to_country'][i]}
        Payable_by = {'name': df['Payable_by_Name'][i], 'street': df['Payable_by_street'][i], 'house_num': df['Payable_by_house_num'][i], 'pcode': df['Payable_by_pcode'][i], 'city': df['Payable_by_city'][i], 'country': df['Payable_by_country'][i]}
        my_bill = QRBill(
            account=df['Account'][i],
            creditor=Payable_to,
            currency=df['currency'][i],
            amount=None,
            language=ui_mainwindow.Language,  # 'en', 'de', 'fr' or 'it'
            debtor=Payable_by,
            reference_number=df['Reference'][i],
            additional_information=df['additional_information'][i],
            top_line=False,
            payment_line=False,
            font_factor=1,  # 0 就不輸出文字, 1 輸出字體
        )
        outputsvg = './temp/' + str(i + 1).strip() + ".svg"
        my_bill.as_svg(outputsvg)

        # outputpng = OutputPath + str(i + 1).strip() + ".png"
        # png_data = cairosvg.svg2png(url=outputsvg, dpi=300)
        # image1 = Image.open(io.BytesIO(png_data))
        # cropped_image = image1.crop(box2)
        # cropped_image.save(outputpng)

def fun_QRBill_toSbyS_amount1(df,df_index):
    print('2.1 QRBill Payable to = S, Payable by = S 和有價錢的')
    OutputPath = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    box = (780, 195, 1345, 750)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标
    for i in range(df_index,len(df)+df_index):
        Payable_to = {'name': df['Payable_to_Name'][i], 'street': df['Payable_to_street'][i], 'house_num': df['Payable_to_house_num'][i], 'pcode': df['Payable_to_pcode'][i], 'city': df['Payable_to_city'][i], 'country': df['Payable_to_country'][i]}
        Payable_by = {'name': df['Payable_by_Name'][i], 'street': df['Payable_by_street'][i], 'house_num': df['Payable_by_house_num'][i], 'pcode': df['Payable_by_pcode'][i], 'city': df['Payable_by_city'][i], 'country': df['Payable_by_country'][i]}
        my_bill = QRBill(
            account=df['Account'][i],
            creditor=Payable_to,
            currency=df['currency'][i],
            amount=df['Payable_amount'][i],
            language=ui_mainwindow.Language,  # 'en', 'de', 'fr' or 'it'
            debtor=Payable_by,
            reference_number=df['Reference'][i],
            additional_information=df['additional_information'][i],
            top_line=False,
            payment_line=False,
            font_factor=1,  # 0 就不輸出文字, 1 輸出字體
        )
        outputsvg = './temp/' + str(i + 1).strip() + ".svg"
        my_bill.as_svg(outputsvg)

        # outputpng = OutputPath + str(i + 1).strip() + ".png"
        # png_data = cairosvg.svg2png(url=outputsvg, dpi=300)
        # image1 = Image.open(io.BytesIO(png_data))
        # cropped_image = image1.crop(box)
        # cropped_image.save(outputpng)

def fun_QRBill_toSbyS_amount2(df,df_index):
    print('2.2 QRBill Payable to = S, Payable by = S 和有價錢的')
    OutputPath = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    box2 = (780, 195, 1345, 750)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标
    for i in range(df_index,len(df)+df_index):
        Payable_to = {'name': df['Payable_to_Name'][i], 'street': df['Payable_to_street'][i], 'house_num': df['Payable_to_house_num'][i], 'pcode': df['Payable_to_pcode'][i], 'city': df['Payable_to_city'][i], 'country': df['Payable_to_country'][i]}
        Payable_by = {'name': df['Payable_by_Name'][i], 'street': df['Payable_by_street'][i], 'house_num': df['Payable_by_house_num'][i], 'pcode': df['Payable_by_pcode'][i], 'city': df['Payable_by_city'][i], 'country': df['Payable_by_country'][i]}
        my_bill = QRBill(
            account=df['Account'][i],
            creditor=Payable_to,
            currency=df['currency'][i],
            amount=df['Payable_amount'][i],
            language=ui_mainwindow.Language,  # 'en', 'de', 'fr' or 'it'
            debtor=Payable_by,
            reference_number=df['Reference'][i],
            additional_information=df['additional_information'][i],
            top_line=False,
            payment_line=False,
            font_factor=1,  # 0 就不輸出文字, 1 輸出字體
        )
        outputsvg = './temp/' + str(i + 1).strip() + ".svg"
        my_bill.as_svg(outputsvg)

        # outputpng = OutputPath + str(i + 1).strip() + ".png"
        # png_data = cairosvg.svg2png(url=outputsvg, dpi=300)
        # image1 = Image.open(io.BytesIO(png_data))
        # cropped_image = image1.crop(box2)
        # cropped_image.save(outputpng)

def fun_QRBill_toSbyK_amountNone1(df,df_index):
    print('3.1 QRBill Payable to = S, Payable by = K 和沒有價錢的')
    print('3.1 df_index:', df_index)
    OutputPath = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    print("3.1 Language: ", ui_mainwindow.Language)
    #box = (780, 195, 1345, 750)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标, cairosvg方式
    box = fitz.Rect(188, 47, 323, 182)  #pymupdf 方式
    for i in range(df_index,len(df)+df_index):
        # print('3.1 index: ', i)
        Payable_to = {'name': df['Payable_to_Name'][i], 'street': df['Payable_to_street'][i], 'house_num': df['Payable_to_house_num'][i], 'pcode': df['Payable_to_pcode'][i], 'city': df['Payable_to_city'][i], 'country': df['Payable_to_country'][i]}
        Payable_by = {'name': df['Payable_by_Name'][i], 'line1': df['Payable_by_street'][i], 'line2': df['Payable_by_house_num'][i], 'country': df['Payable_by_country'][i]}
        my_bill = QRBill(
            account=df['Account'][i],
            creditor=Payable_to,
            currency=df['currency'][i],
            amount=None,
            language=ui_mainwindow.Language,  # 'en', 'de', 'fr' or 'it'
            debtor=Payable_by,
            reference_number=df['Reference'][i],
            additional_information=df['additional_information'][i],
            top_line=False,
            payment_line=False,
            font_factor=1  # 0 就不輸出文字, 1 輸出字體
        )
        outputsvg = './temp/'+str(i + 1).strip() + ".svg"
        my_bill.as_svg(outputsvg)
        # my_bill.qr_image('./temp/'+str(i + 1).strip() + ".png")
        #不用cairosvg方式
        # outputpng = OutputPath + str(i + 1).strip() + ".png"
        # png_data = cairosvg.svg2png(url=outputsvg, dpi=300)
        # image1 = Image.open(io.BytesIO(png_data))
        # cropped_image = image1.crop(box)
        # cropped_image.save(outputpng,quality=50)  #, format ='PNG', optimize=True, quality=30
        # 不用cairosvg方式


        # renderPDF.drawToFile(svglib.svg2rlg(outputsvg), outputpdf)

def fun_QRBill_toSbyK_amountNone2(df,df_index):
    print('3.2 QRBill Payable to = S, Payable by = K 和沒有價錢的')
    print('3.2 df_index:',df_index)
    print("3.2 Language: ", ui_mainwindow.Language)
    OutputPath=ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    box2 = (780, 195, 1345, 750)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标. cairosvg方式
    box2 = fitz.Rect(188, 47, 323, 182)  # pymupdf 方式
    for i in range(df_index,len(df)+df_index):
        # print('3.2 index: ',i)
        Payable_to = {'name': df['Payable_to_Name'][i], 'street': df['Payable_to_street'][i], 'house_num': df['Payable_to_house_num'][i], 'pcode': df['Payable_to_pcode'][i], 'city': df['Payable_to_city'][i], 'country': df['Payable_to_country'][i]}
        Payable_by = {'name': df['Payable_by_Name'][i], 'line1': df['Payable_by_street'][i], 'line2': df['Payable_by_house_num'][i], 'country': df['Payable_by_country'][i]}
        my_bill = QRBill(
            account=df['Account'][i],
            creditor=Payable_to,
            currency=df['currency'][i],
            amount=None,
            language=ui_mainwindow.Language,  # 'en', 'de', 'fr' or 'it'
            debtor=Payable_by,
            reference_number=df['Reference'][i],
            additional_information=df['additional_information'][i],
            top_line=False,
            payment_line=False,
            font_factor=1  # 0 就不輸出文字, 1 輸出字體
        )
        outputsvg = './temp/'+str(i + 1).strip() + ".svg"
        my_bill.as_svg(outputsvg)

        # 不用cairosvg方式
        # outputpng = OutputPath + str(i + 1).strip() + ".png"
        # png_data = cairosvg.svg2png(url=outputsvg, dpi=300)
        # image1 = Image.open(io.BytesIO(png_data))
        # cropped_image = image1.crop(box2)
        # cropped_image.save(outputpng)
        # 不用cairosvg方式


        # renderPDF.drawToFile(svglib.svg2rlg(outputsvg), outputpdf)

def fun_QRBill_toSbyK_amount1(df,df_index):
    print('4.1 QRBill Payable to = S, Payable by = K 和有價錢的')
    OutputPath = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    box = (780, 195, 1345, 750)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标
    for i in range(df_index,len(df)+df_index):
        Payable_to = {'name': df['Payable_to_Name'][i], 'street': df['Payable_to_street'][i], 'house_num': df['Payable_to_house_num'][i], 'pcode': df['Payable_to_pcode'][i], 'city': df['Payable_to_city'][i], 'country': df['Payable_to_country'][i]}
        Payable_by = {'name': df['Payable_by_Name'][i], 'line1': df['Payable_by_street'][i], 'line2': df['Payable_by_house_num'][i], 'country': df['Payable_by_country'][i]}
        my_bill = QRBill(
            account=df['Account'][i],
            creditor=Payable_to,
            currency=df['currency'][i],
            amount=df['Payable_amount'][i],
            language=ui_mainwindow.Language,  # 'en', 'de', 'fr' or 'it'
            debtor=Payable_by,
            reference_number=df['Reference'][i],
            additional_information=df['additional_information'][i],
            top_line=False,
            payment_line=False,
            font_factor=1,  # 0 就不輸出文字, 1 輸出字體
        )
        outputsvg = './temp/' + str(i + 1).strip() + ".svg"
        my_bill.as_svg(outputsvg)

        # outputpng = OutputPath + str(i + 1).strip() + ".png"
        # png_data = cairosvg.svg2png(url=outputsvg, dpi=300)
        # image1 = Image.open(io.BytesIO(png_data))
        # cropped_image = image1.crop(box)
        # cropped_image.save(outputpng)

def fun_QRBill_toSbyK_amount2(df,df_index):
    print('4.2 QRBill Payable to = S, Payable by = K 和有價錢的')
    OutputPath = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    box2 = (780, 195, 1345, 750)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标
    for i in range(df_index,len(df)+df_index):
        Payable_to = {'name': df['Payable_to_Name'][i], 'street': df['Payable_to_street'][i], 'house_num': df['Payable_to_house_num'][i], 'pcode': df['Payable_to_pcode'][i], 'city': df['Payable_to_city'][i], 'country': df['Payable_to_country'][i]}
        Payable_by = {'name': df['Payable_by_Name'][i], 'line1': df['Payable_by_street'][i], 'line2': df['Payable_by_house_num'][i], 'country': df['Payable_by_country'][i]}
        my_bill = QRBill(
            account=df['Account'][i],
            creditor=Payable_to,
            currency=df['currency'][i],
            amount=df['Payable_amount'][i],
            language=ui_mainwindow.Language,  # 'en', 'de', 'fr' or 'it'
            debtor=Payable_by,
            reference_number=df['Reference'][i],
            additional_information=df['additional_information'][i],
            top_line=False,
            payment_line=False,
            font_factor=1,  # 0 就不輸出文字, 1 輸出字體
        )
        outputsvg = './temp/' + str(i + 1).strip() + ".svg"
        my_bill.as_svg(outputsvg)

        # outputpng = OutputPath + str(i + 1).strip() + ".png"
        # png_data = cairosvg.svg2png(url=outputsvg, dpi=300)
        # image1 = Image.open(io.BytesIO(png_data))
        # cropped_image = image1.crop(box2)
        # cropped_image.save(outputpng)

def fun_QRBill_toKbyK_amountNone1(df,df_index):
    print('5.1 QRBill Payable to = K, Payable by = K 和沒有價錢的')
    OutputPath = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    box = (780, 195, 1345, 750)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标
    for i in range(df_index,len(df)+df_index):
        Payable_to = {'name': df['Payable_to_Name'][i], 'line1': df['Payable_to_street'][i], 'line2': df['Payable_to_house_num'][i], 'country': df['Payable_to_country'][i]}
        Payable_by = {'name': df['Payable_by_Name'][i], 'line1': df['Payable_by_street'][i], 'line2': df['Payable_by_house_num'][i], 'country': df['Payable_by_country'][i]}
        my_bill = QRBill(
            account=df['Account'][i],
            creditor=Payable_to,
            currency=df['currency'][i],
            amount=None,
            language=ui_mainwindow.Language,  # 'en', 'de', 'fr' or 'it'
            debtor=Payable_by,
            reference_number=df['Reference'][i],
            additional_information=df['additional_information'][i],
            top_line=False,
            payment_line=False,
            font_factor=1,  # 0 就不輸出文字, 1 輸出字體
        )
        outputsvg = './temp/' + str(i + 1).strip() + ".svg"
        my_bill.as_svg(outputsvg)

        # outputpng = OutputPath + str(i + 1).strip() + ".png"
        # png_data = cairosvg.svg2png(url=outputsvg, dpi=300)
        # image1 = Image.open(io.BytesIO(png_data))
        # cropped_image = image1.crop(box)
        # cropped_image.save(outputpng)

def fun_QRBill_toKbyK_amountNone2(df,df_index):
    print('5.2 QRBill Payable to = K, Payable by = K 和沒有價錢的')
    OutputPath = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    box2 = (780, 195, 1345, 750)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标
    for i in range(df_index,len(df)+df_index):
        Payable_to = {'name': df['Payable_to_Name'][i], 'line1': df['Payable_to_street'][i], 'line2': df['Payable_to_house_num'][i], 'country': df['Payable_to_country'][i]}
        Payable_by = {'name': df['Payable_by_Name'][i], 'line1': df['Payable_by_street'][i], 'line2': df['Payable_by_house_num'][i], 'country': df['Payable_by_country'][i]}
        my_bill = QRBill(
            account=df['Account'][i],
            creditor=Payable_to,
            currency=df['currency'][i],
            amount=None,
            language=ui_mainwindow.Language,  # 'en', 'de', 'fr' or 'it'
            debtor=Payable_by,
            reference_number=df['Reference'][i],
            additional_information=df['additional_information'][i],
            top_line=False,
            payment_line=False,
            font_factor=1,  # 0 就不輸出文字, 1 輸出字體
        )
        outputsvg = './temp/' + str(i + 1).strip() + ".svg"
        my_bill.as_svg(outputsvg)

        # outputpng = OutputPath + str(i + 1).strip() + ".png"
        # png_data = cairosvg.svg2png(url=outputsvg, dpi=300)
        # image1 = Image.open(io.BytesIO(png_data))
        # cropped_image = image1.crop(box2)
        # cropped_image.save(outputpng)

def fun_QRBill_toKbyK_amount1(df,df_index):
    print('6.1 QRBill Payable to = K, Payable by = K 和有價錢的')
    OutputPath = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    box = (780, 195, 1345, 750)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标
    for i in range(df_index,len(df)+df_index):
        Payable_to = {'name': df['Payable_to_Name'][i], 'line1': df['Payable_to_street'][i], 'line2': df['Payable_to_house_num'][i], 'country': df['Payable_to_country'][i]}
        Payable_by = {'name': df['Payable_by_Name'][i], 'line1': df['Payable_by_street'][i], 'line2': df['Payable_by_house_num'][i], 'country': df['Payable_by_country'][i]}
        my_bill = QRBill(
            account=df['Account'][i],
            creditor=Payable_to,
            currency=df['currency'][i],
            amount=df['Payable_amount'][i],
            language=ui_mainwindow.Language,  # 'en', 'de', 'fr' or 'it'
            debtor=Payable_by,
            reference_number=df['Reference'][i],
            additional_information=df['additional_information'][i],
            top_line=False,
            payment_line=False,
            font_factor=1,  # 0 就不輸出文字, 1 輸出字體
        )
        outputsvg = './temp/' + str(i + 1).strip() + ".svg"
        my_bill.as_svg(outputsvg)

        # outputpng = OutputPath + str(i + 1).strip() + ".png"
        # png_data = cairosvg.svg2png(url=outputsvg, dpi=300)
        # image1 = Image.open(io.BytesIO(png_data))
        # cropped_image = image1.crop(box)
        # cropped_image.save(outputpng)

def fun_QRBill_toKbyK_amount2(df,df_index):
    print('6.2 QRBill Payable to = K, Payable by = K 和有價錢的')
    OutputPath = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    box2 = (780, 195, 1345, 750)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标
    for i in range(df_index,len(df)+df_index):
        Payable_to = {'name': df['Payable_to_Name'][i], 'line1': df['Payable_to_street'][i], 'line2': df['Payable_to_house_num'][i], 'country': df['Payable_to_country'][i]}
        Payable_by = {'name': df['Payable_by_Name'][i], 'line1': df['Payable_by_street'][i], 'line2': df['Payable_by_house_num'][i], 'country': df['Payable_by_country'][i]}
        my_bill = QRBill(
            account=df['Account'][i],
            creditor=Payable_to,
            currency=df['currency'][i],
            amount=df['Payable_amount'][i],
            language=ui_mainwindow.Language,  # 'en', 'de', 'fr' or 'it'
            debtor=Payable_by,
            reference_number=df['Reference'][i],
            additional_information=df['additional_information'][i],
            top_line=False,
            payment_line=False,
            font_factor=1,  # 0 就不輸出文字, 1 輸出字體
        )
        outputsvg = './temp/' + str(i + 1).strip() + ".svg"
        my_bill.as_svg(outputsvg)

        # outputpng = OutputPath + str(i + 1).strip() + ".png"
        # png_data = cairosvg.svg2png(url=outputsvg, dpi=300)
        # image1 = Image.open(io.BytesIO(png_data))
        # cropped_image = image1.crop(box2)
        # cropped_image.save(outputpng)

def fun_QRBill_toKbyS_amountNone1(df,df_index):
    print('7.1 QRBill Payable to = K, Payable by = S 和沒有價錢的')
    OutputPath = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    box = (780, 195, 1345, 750)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标
    for i in range(df_index,len(df)+df_index):
        Payable_to = {'name': df['Payable_to_Name'][i], 'line1': df['Payable_to_street'][i], 'line2': df['Payable_to_house_num'][i], 'country': df['Payable_to_country'][i]}
        Payable_by = {'name': df['Payable_by_Name'][i], 'street': df['Payable_by_street'][i], 'house_num': df['Payable_by_house_num'][i], 'pcode': df['Payable_by_pcode'][i], 'city': df['Payable_by_city'][i], 'country': df['Payable_by_country'][i]}
        my_bill = QRBill(
            account=df['Account'][i],
            creditor=Payable_to,
            currency=df['currency'][i],
            amount=None,
            language=ui_mainwindow.Language,  # 'en', 'de', 'fr' or 'it'
            debtor=Payable_by,
            reference_number=df['Reference'][i],
            additional_information=df['additional_information'][i],
            top_line=False,
            payment_line=False,
            font_factor=1,  # 0 就不輸出文字, 1 輸出字體
        )
        outputsvg = './temp/' + str(i + 1).strip() + ".svg"
        my_bill.as_svg(outputsvg)

        # outputpng = OutputPath + str(i + 1).strip() + ".png"
        # png_data = cairosvg.svg2png(url=outputsvg, dpi=300)
        # image1 = Image.open(io.BytesIO(png_data))
        # cropped_image = image1.crop(box)
        # cropped_image.save(outputpng)

def fun_QRBill_toKbyS_amountNone2(df,df_index):
    print('7.2 QRBill Payable to = K, Payable by = S 和沒有價錢的')
    OutputPath = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    box2 = (780, 195, 1345, 750)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标
    for i in range(df_index,len(df)+df_index):
        Payable_to = {'name': df['Payable_to_Name'][i], 'line1': df['Payable_to_street'][i], 'line2': df['Payable_to_house_num'][i], 'country': df['Payable_to_country'][i]}
        Payable_by = {'name': df['Payable_by_Name'][i], 'street': df['Payable_by_street'][i], 'house_num': df['Payable_by_house_num'][i], 'pcode': df['Payable_by_pcode'][i], 'city': df['Payable_by_city'][i], 'country': df['Payable_by_country'][i]}
        my_bill = QRBill(
            account=df['Account'][i],
            creditor=Payable_to,
            currency=df['currency'][i],
            amount=None,
            language=ui_mainwindow.Language,  # 'en', 'de', 'fr' or 'it'
            debtor=Payable_by,
            reference_number=df['Reference'][i],
            additional_information=df['additional_information'][i],
            top_line=False,
            payment_line=False,
            font_factor=1,  # 0 就不輸出文字, 1 輸出字體
        )
        outputsvg = './temp/' + str(i + 1).strip() + ".svg"
        my_bill.as_svg(outputsvg)

        # outputpng = OutputPath + str(i + 1).strip() + ".png"
        # png_data = cairosvg.svg2png(url=outputsvg, dpi=300)
        # image1 = Image.open(io.BytesIO(png_data))
        # cropped_image = image1.crop(box2)
        # cropped_image.save(outputpng)

def fun_QRBill_toKbyS_amount1(df,df_index):
    print('8.1 QRBill Payable to = K, Payable by = S 和有價錢的')
    OutputPath = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    box = (780, 195, 1345, 750)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标
    for i in range(df_index,len(df)+df_index):
        Payable_to = {'name': df['Payable_to_Name'][i], 'line1': df['Payable_to_street'][i], 'line2': df['Payable_to_house_num'][i], 'country': df['Payable_to_country'][i]}
        Payable_by = {'name': df['Payable_by_Name'][i], 'street': df['Payable_by_street'][i], 'house_num': df['Payable_by_house_num'][i], 'pcode': df['Payable_by_pcode'][i], 'city': df['Payable_by_city'][i], 'country': df['Payable_by_country'][i]}
        my_bill = QRBill(
            account=df['Account'][i],
            creditor=Payable_to,
            currency=df['currency'][i],
            amount=df['Payable_amount'][i],
            language=ui_mainwindow.Language,  # 'en', 'de', 'fr' or 'it'
            debtor=Payable_by,
            reference_number=df['Reference'][i],
            additional_information=df['additional_information'][i],
            top_line=False,
            payment_line=False,
            font_factor=1,  # 0 就不輸出文字, 1 輸出字體
        )
        outputsvg = './temp/' + str(i + 1).strip() + ".svg"
        my_bill.as_svg(outputsvg)

        # outputpng = OutputPath + str(i + 1).strip() + ".png"
        # png_data = cairosvg.svg2png(url=outputsvg, dpi=300)
        # image1 = Image.open(io.BytesIO(png_data))
        # cropped_image = image1.crop(box)
        # cropped_image.save(outputpng)

def fun_QRBill_toKbyS_amount2(df,df_index):
    print('8.2 QRBill Payable to = K, Payable by = S 和有價錢的')
    OutputPath = ui_mainwindow.JobPath + '/' + ui_mainwindow.JobName + '/'
    box2 = (780, 195, 1345, 750)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标
    for i in range(df_index,len(df)+df_index):
        Payable_to = {'name': df['Payable_to_Name'][i], 'line1': df['Payable_to_street'][i], 'line2': df['Payable_to_house_num'][i], 'country': df['Payable_to_country'][i]}
        Payable_by = {'name': df['Payable_by_Name'][i], 'street': df['Payable_by_street'][i], 'house_num': df['Payable_by_house_num'][i], 'pcode': df['Payable_by_pcode'][i], 'city': df['Payable_by_city'][i], 'country': df['Payable_by_country'][i]}
        my_bill = QRBill(
            account=df['Account'][i],
            creditor=Payable_to,
            currency=df['currency'][i],
            amount=df['Payable_amount'][i],
            language=ui_mainwindow.Language,  # 'en', 'de', 'fr' or 'it'
            debtor=Payable_by,
            reference_number=df['Reference'][i],
            additional_information=df['additional_information'][i],
            top_line=False,
            payment_line=False,
            font_factor=1,  # 0 就不輸出文字, 1 輸出字體
        )
        outputsvg = './temp/' + str(i + 1).strip() + ".svg"
        my_bill.as_svg(outputsvg)

        # outputpng = OutputPath + str(i + 1).strip() + ".png"
        # png_data = cairosvg.svg2png(url=outputsvg, dpi=300)
        # image1 = Image.open(io.BytesIO(png_data))
        # cropped_image = image1.crop(box2)
        # cropped_image.save(outputpng)

if __name__ == '__main__':
    app = QApplication([])
    check_status = 0
    ui_mainwindow = mainwindow(QMainWindow())
    sys.exit(app.exec_())







