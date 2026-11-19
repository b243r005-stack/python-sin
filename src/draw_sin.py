import numpy as np
import matplotlib.pyplot as plt

# x軸のデータ
x = np.linspace(0, 2 * np.pi, 1000)

# 正弦波の計算
y = np.sin(x)

# グラフの描画
plt.plot(x, y)

# グラフの設定
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid()

# グラフを表示
plt.show()
