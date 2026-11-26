import numpy as np
import matplotlib.pyplot as plt

# データ数
n = 200

# 横軸を作成（0～4π）
x = np.linspace(0, 4*np.pi, n)

# 正弦波を作成
y = np.sin(x)

# グラフを描画
plt.plot(x, y)

# 表示
plt.show()

#test変わってますか!