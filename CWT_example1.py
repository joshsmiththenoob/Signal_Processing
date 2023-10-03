'''
CWT 3D圖展示
'''

import pywt
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(512)
y = np.sin(2*np.pi*x/32)
scales = np.arange(1,129)
coef, freqs=pywt.cwt(y,np.arange(1,129),'morl')

# 建立一個3D圖表
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, Y = np.meshgrid(x, scales)
Z = coef

# 使用`plot_surface`方法將數據繪製為3D曲面
surf = ax.plot_surface(X, Y, Z, cmap="viridis")

# 一些常見的3D圖表調整
ax.set_xlabel('Time')
ax.set_ylabel('Scale')
ax.set_zlabel('Coefficient')
ax.set_title("3D Representation of CWT")
ax.view_init(90, 90)

fig.colorbar(surf)

plt.show()
