import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Resim boyutları
width, height = 256, 256

# X ve Y koordinatları için meshgrid oluştur
x = np.linspace(-np.pi, np.pi, width)
y = np.linspace(-np.pi, np.pi, height)
X, Y = np.meshgrid(x, y)

# RGB kanalları için matematiksel ifadeler
R = (np.sin(X * 2 + Y) + 1) / 2  # Kırmızı kanal: sin(2x + y)
G = (np.cos(X - Y * 2) + 1) / 2  # Yeşil kanal: cos(x - 2y)
B = (np.sin(X * Y) + 1) / 2       # Mavi kanal: sin(xy)

# RGB kanallarını birleştirerek resmi oluştur
image = np.stack([R, G, B], axis=-1)

# 2x2 grid ile görselleştirme
fig = plt.figure(figsize=(12, 12))

# RGB Resim
ax1 = fig.add_subplot(221)
ax1.imshow(image)
ax1.set_title("Matematiksel RGB Resim")
ax1.axis('off')

# Kırmızı kanal
ax2 = fig.add_subplot(222, projection='3d')
ax2.plot_surface(X, Y, R, cmap='Reds')
ax2.set_title('Kırmızı Kanal: sin(2x + y)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

# Yeşil kanal
ax3 = fig.add_subplot(223, projection='3d')
ax3.plot_surface(X, Y, G, cmap='Greens')
ax3.set_title('Yeşil Kanal: cos(x - 2y)')
ax3.set_xlabel('x')
ax3.set_ylabel('y')

# Mavi kanal
ax4 = fig.add_subplot(224, projection='3d')
ax4.plot_surface(X, Y, B, cmap='Blues')
ax4.set_title('Mavi Kanal: sin(xy)')
ax4.set_xlabel('x')
ax4.set_ylabel('y')

# Düzeni optimize et ve kaydet
plt.tight_layout()
plt.savefig('math_art_output.png', dpi=300, bbox_inches='tight')
plt.show()