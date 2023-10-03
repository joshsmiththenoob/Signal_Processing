# 地震模擬訊號 - 連續小波變換

import pywt
import matplotlib.pyplot as plt
import numpy as np

file_path =  r'D:\bridge\DanSuiBridge_rawdata\Broken\KP_Su_CABLEE09_Y.txt'
fs = 200   # 取樣頻率


data = []  # To store lines of data       
    # 讀取txt檔案
with open(file_path) as f:
    lines = f.readlines()
lines = lines[18:] # txt檔第幾行開始為數據
# 紀錄數據
for line in lines:
    if line.strip() == "":  # Stop at the first blank line
        break
    data.append([float(x) for x in line.split()])



# 時域訊號建立完成
data = np.array(data)
time_domain = data[:,0]
data_1 = data[:,2]


# 進行連續小波變換
wave_name = 'morl' # cgau8 為 小波的名稱
total_scale = 256 # 一共有多少個尺度 = 不同大小(壓縮大小)的小波基用作分析
fc = pywt.central_frequency(wave_name)  # 小波的"中心頻率" : 該小波的主要頻率
# 中心頻率 = 母小波基的中心頻率 / 尺度(scale伸縮大小) * 取樣間隔(sampling_period or interval)
print(fc)
c_param = 2 * fc * total_scale
scales = c_param / np.arange(total_scale, 1, -1)
print(c_param)
print(np.arange(total_scale, 1, -1))
print(scales)
print(scales.shape)
# print(np.arange(total_scale, 1, -1))

[cwtmatr, frequencies] = pywt.cwt(data_1, scales, wave_name, 1.0 / fs)


plt.figure(figsize= (8,4))
plt.subplot(211)
plt.plot(time_domain,data_1)
plt.title('Signal', fontsize = 20)
plt.subplot(212)
print(frequencies.shape, cwtmatr.shape)
plt.contourf(time_domain, frequencies, abs(cwtmatr))
plt.ylabel(u'prinv(Hz)')
plt.xlabel(u't(s)')
plt.subplots_adjust(hspace = 0.4)
plt.show()

