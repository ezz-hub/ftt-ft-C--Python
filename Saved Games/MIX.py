import sys
from PyQt5 import QtWidgets as qtw
from mixergui import Ui_MainWindow
from import_images import image
from error_msg import error
from draw_img import drawing
from fourier_Trans import fourier
import numpy as np
import logging
class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.labels_list=[self.ui.label_img1,self.ui.label_img2,self.ui.label_component1_2,self.ui.label_component2,self.ui.output1,self.ui.output2]
        self.ui.actionNew_file.triggered.connect(self.open_newwindow)
        self.ui.actionimages.triggered.connect(self.getdata)
        for i in range(len(self.ui.list_combobox)):
            self.ui.list_combobox[i].currentTextChanged.connect(self.gain)
        for i in range(len(self.ui.list_sliders)):
            self.ui.list_sliders[i].sliderReleased.connect(self.gain)
        for i in range(len(self.ui.list_combobox_image_component)):
            self.ui.list_combobox_image_component[i].currentTextChanged.connect(self.view_component)
    def view_component(self):
        try:
            for i in range(len(self.ui.list_combobox_image_component)):
                self.gray=fourier().image_components(self.ui.list_combobox_image_component[i].currentText(),self.data_list_timedomain[i])
                #self.data_single_component=fourier().image_components(self.ui.list_combobox_image_component[i].currentText(),self.data_list[i])
                self.draw_label(self.gray,self.labels_list[i+2],'gray')
        except Exception:
            pass
    def reshape(self,data,shape_of_data):
        data_shaped = data.reshape(shape_of_data)
        return data_shaped
    def gain(self):
        try:

            error().error_if_not_equal(self.data1,self.data2)
            self.ui.gain1.setText(str(self.ui.list_sliders[0].value()))
            self.ui.gain2.setText(str(self.ui.list_sliders[1].value()))
            self.data_mixed=fourier().choose_image_sequence(self.ui.list_sliders[0].value()/100,self.ui.list_sliders[1].value()/100,self.ui.list_combobox[2].currentText(),self.ui.list_combobox[3].currentText(),self.ui.list_combobox[0].currentText(),self.ui.list_combobox[1].currentText(),self.data_list[0],self.data_list[1])
            if self.ui.list_combobox[4].currentText()=='output1':
                self.draw_label(self.reshape(self.data_mixed,self.data_shape),self.labels_list[4])
            else:
                self.draw_label(self.reshape(self.data_mixed,self.data_shape),self.labels_list[5])
        except Exception: 
            pass
    def get_fourier_list(self,i):
        self.data_list[i]=fourier().get_fourier(self.data_list[i].reshape(-1))
    def draw_label(self,data,label,layout='rgb'):
        pix1=drawing.image_to_label(data,label.width(),label.height(),layout)
        label.setPixmap(pix1)
        label.show()
    def getdata(self):
        #the function responsibile to get the data needed
        self.data1,path1,self.data2,path2=image().get_2arrays()
        try:
            error().error_if_not_equal(self.data1,self.data2,path1,path2)
            self.data1_timedomain,self.data2_timedomain=self.data1.copy(),self.data2.copy()
            self.data_shape=self.data1.shape
            self.data_list=[self.data1,self.data2]
            self.data_list_timedomain=[self.data1_timedomain,self.data2_timedomain]
            for i in range(2):
                self.draw_label(self.data_list[i],self.labels_list[i])
                self.get_fourier_list(i)
            self.gain()
            self.view_component()
        except Exception:
            pass
    def open_newwindow(self):
        self.new_instance = MainWindow()
        self.new_instance.show()
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    app.setStyle("Fusion")
    mw = MainWindow()
    sys.exit(app.exec_())
