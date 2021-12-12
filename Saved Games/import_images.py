import matplotlib.image as mpimg
from numpy import asarray
from PyQt5.QtWidgets import QFileDialog
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from error_msg import error

class image():
    def imp_image(self):
        path_image = QFileDialog.getOpenFileName(None, 'Open JPG ', '/home', "JPG (*.jpg)")[0]
        return path_image
    def get_image_array(self):
        path=self.imp_image()
        img = mpimg.imread(path)
        data = asarray(img)
        return data,len(path)

    def get_2arrays(self):
        try:
            data1,path1=self.get_image_array()
            data2,path2=self.get_image_array()
            return data1,path1,data2,path2
        except Exception:
            pass
        #print(data1,data2)
        return 0,0,0,0
    
