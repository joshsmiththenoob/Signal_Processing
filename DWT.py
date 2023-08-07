# 小波變換基礎
# 離散小波變換 : 一個訊號是由"有限的縮放、平移的小波基"所組成的
import pywt
import matplotlib.pyplot as plt
import numpy as np

fs = 1024 # 取樣頻率[pts/sec] sampling rate
t = np.arange(0,1.0, 1.0/ fs) # 建立時域座標 ~ linspace on Matlab
f1 = 100
f2 = 200
f3 = 300
f4 = 400

# 生成隨時間變化的正弦波形
data = np.piecewise(t, [t < 1, t < 0.8, t < 0.5, t < 0.3],
                    [lambda t : 400 * np.sin(2 * np.pi * f4 * t),
                     lambda t : 300 * np.sin(2 * np.pi * f3 * t),
                     lambda t : 200 * np.sin(2 * np.pi * f2 * t),
                     lambda t : 100 * np.sin(2 * np.pi * f1 * t)])
wave_name = 'cgau8' # cgau8 為 小波的名稱
total_scale = 256
fc = pywt.central_frequency(wave_name)  # 以該小波(cgau8)為基底，進行平移、伸縮，產生彼此獨立的小波基函數
c_param = 2 * fc * total_scale
scales = c_param / np.arange(total_scale, 1, -1)

[cwtmatr, frequencies] = pywt.cwt(data, scales, wave_name, 1.0 / fs)


plt.figure(figsize= (8,4))
plt.subplot(211)
plt.plot(t,data)
plt.title('Signal', fontsize = 20)
plt.subplot(212)
plt.contourf(t, frequencies, abs(cwtmatr))
plt.ylabel(u'prinv(Hz)')
plt.xlabel(u't(s)')
plt.subplots_adjust(hspace = 0.4)
plt.show()
