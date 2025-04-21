import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Resim boyutları
width, height = 512, 512

# X ve Y koordinatları için meshgrid oluştur
x = np.linspace(-2 * np.pi, 2 * np.pi, width)
y = np.linspace(-2 * np.pi, 2 * np.pi, height)
X, Y = np.meshgrid(x, y)

# Daha karmaşık matematiksel ifadeler
R = (np.sin(X**2 + Y) * np.cos(Y**2) + 1) / 2  # Kırmızı: sin(x² + y) * cos(y²)
G = (np.cos(np.sin(X * Y)) * np.tanh(X - Y) + 1) / 2  # Yeşil: cos(sin(xy)) * tanh(x - y)
B = (np.sin(np.exp(X / 2) + Y**2) + 1) / 2  # Mavi: sin(e^(x/2) + y²)

# RGB kanallarını birleştirerek resmi oluştur
image = np.stack([R, G, B], axis=-1)

# 2x2 grid ile görselleştirme
fig = plt.figure(figsize=(12, 12))

# RGB Resim
ax1 = fig.add_subplot(221)
ax1.imshow(image)
ax1.set_title("Matematiksel RGB Resim")
ax1.axis('off')

# Kırmızı kanal 3D yüzey
ax2 = fig.add_subplot(222, projection='3d')
ax2.plot_surface(X, Y, R, cmap='Reds')
ax2.set_title('Kırmızı: sin(x² + y) * cos(y²)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

# Yeşil kanal 3D yüzey
ax3 = fig.add_subplot(223, projection='3d')
ax3.plot_surface(X, Y, G, cmap='Greens')
ax3.set_title('Yeşil: cos(sin(xy)) * tanh(x - y)')
ax3.set_xlabel('x')
ax3.set_ylabel('y')

# Mavi kanal 3D yüzey
ax4 = fig.add_subplot(224, projection='3d')
ax4.plot_surface(X, Y, B, cmap='Blues')
ax4.set_title('Mavi: sin(e^(x/2) + y²)')
ax4.set_xlabel('x')
ax4.set_ylabel('y')

# Düzeni optimize et ve kaydet
plt.tight_layout()
plt.savefig('math_art_output.png', dpi=300, bbox_inches='tight')
plt.show()