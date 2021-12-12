import numpy as np
from scipy.fft import fft, fftfreq,ifft,fftshift,ifftshift,rfft,rfftfreq,irfft
import matplotlib.pyplot as plt
class fourier():
    def data_processing(self,data):
        data=np.real(data)
        data=np.round(data)
        return data.astype(np.uint8)
    def get_fourier(self,data):
        data=fft(data)
        return data
    def get_inverse(self,data):
        data=ifft(data)
        return self.data_processing(data)
        #data=np.real(data)
        #data=np.round(data)
        #return data
    def get_Magnitude(self,gain,data):
        data = np.abs(data)*gain
        return data
    def get_phase(self,gain,data):
        data=np.angle(data)*gain
        return data
    def get_real(self,gain,data):
        data=np.real(data)*gain
        return data
    def get_imag(self,gain,data):
        data=np.imag(data)*gain*1j
        return data
    def get_uniMag(self,data):
        data = np.abs(data)*0+1
        return data
    def get_uniPhase(self,data):
        data = np.angle(data)*0
        return data
    def combine(self,data1,data2,operation):
        if operation==0:
            data_combined = np.multiply(data1, np.exp(1j*data2))
        if operation==1:
            data_combined=np.array(data1)+np.array(data2)
        data_inverse=self.get_inverse(data_combined)
        return data_inverse
    
    def get_mag_phase(self,gain1,gain2,data1,data2):
        data_magnitude=self.mag_component(gain1,data1,data2)
        data_phase=self.phase_component(gain2,data1,data2)
        return self.combine(data_magnitude,data_phase,0)
    def mag_component(self,gain,data1,data2):
        return self.get_Magnitude(gain,data1)+self.get_Magnitude((1-gain),data2)
    def phase_component(self,gain,data1,data2):
        return self.get_phase(gain,data2)+self.get_phase((1-gain),data1)
    def get_Real_imag(self,gain1,gain2,data1,data2):
        data_real=self.get_real(gain1,data1)+self.get_real((1-gain1),data2)
        data_imag=self.get_imag(gain2,data2)+self.get_imag((1-gain2),data1)
        return self.combine(data_real,data_imag,1) 
    def mix_panel(self,gain1,gain2,chooesed1,choosed2,data1,data2):
        if chooesed1=="Mag" and choosed2=="Phase":
            return self.get_mag_phase(gain1,gain2,data1,data2)
        if chooesed1=="Phase" and choosed2=="Mag":
            return self.get_mag_phase(gain2,gain1,data2,data1)
        if chooesed1=="Real" and choosed2=="Imag":
            return self.get_Real_imag(gain1,gain2,data1,data2)
        if chooesed1=="Imag" and choosed2=="Real":
            return self.get_Real_imag(gain2,gain1,data2,data1)
        if chooesed1=="Uni Mag" and choosed2=="Phase":
            data_Mag=self.get_uniMag(data1)
            data_phase=self.phase_component(gain2,data1,data2)
            return self.combine(data_Mag,data_phase,0)
        if chooesed1=="Mag" and choosed2=="Uni Phase":
            data_Mag=self.mag_component(gain1,data1,data2)
            data_phase=self.get_uniPhase(data2)
            return self.combine(data_Mag,data_phase,0)
        if chooesed1=="Uni Mag" and choosed2=="Uni Phase":
            data_Mag=self.get_uniMag(data1)
            data_phase=self.get_uniPhase(data2)
            return self.combine(data_Mag,data_phase,0)
        #if chooesed1=="Uni Phase" and choosed2=="Mag":
        #    self.get_uniPhase(data1)
        


    def choose_image_sequence(self,gain1,gain2,component1,component2,chooesed1,choosed2,data1,data2):
        if component1=="image1" and component2 =="image 2":
            return self.mix_panel(gain1,gain2,chooesed1,choosed2,data1,data2)
        elif component1=="image 2" and component2 =="image 1":
            return self.mix_panel(gain1,gain2,chooesed1,choosed2,data2,data1)
        elif component1=="image1" and component2 =="image 1":
            return self.mix_panel(gain1,gain2,chooesed1,choosed2,data1,data1)
        elif component1=="image 2" and component2 =="image 2":
            return self.mix_panel(gain1,gain2,chooesed1,choosed2,data2,data2)
    
    def rgb_to_gray(self,rgb):
        gray = []  
        for row in rgb:
            for pixel in row:
                gray.append(pixel[0]/3 + pixel[1]/3 + pixel[2]/3)
        f = np.fft.fft2(np.array(gray,dtype=np.uint8).reshape((rgb.shape[0],rgb.shape[1])))
        fshift = np.fft.fftshift(f)
        return  fshift
        #magnitude_spectrum = 20*np.log(np.abs(fshift))
        ##print
        #plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
        #plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
        #plt.show()
        #return magnitude_spectrum
    
    def image_components(self,choosed_component,data):
        if choosed_component=="magnitude":
            return 20*np.log(self.get_Magnitude(1,self.rgb_to_gray(data)))
        if choosed_component=="phase":
            return self.get_phase(1,self.rgb_to_gray(data))
        if choosed_component=="real":
            return 20*np.log(self.get_real(1,self.rgb_to_gray(data)))
        if choosed_component=="imag":
            return self.get_imag(1,self.rgb_to_gray(data))/(1j)