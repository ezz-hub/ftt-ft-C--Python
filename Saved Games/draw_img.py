from PyQt5.QtGui import QImage, QPixmap
import numpy as np
class drawing():
    def image_to_label(data,width,height,format='rgb'):
        if format=='rgb':
            im = QImage(data.reshape(-1), data.shape[1], data.shape[0], data.shape[1]*3, QImage.Format_RGB888)
        else:
            im = QImage(np.round(data.reshape(-1)).astype(np.uint8), data.shape[1], data.shape[0], QImage.Format_Indexed8)
        pix = QPixmap(im).scaled(width, height)
        return pix
    