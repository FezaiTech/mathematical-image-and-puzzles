import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Rotasyon koordinat dönüşümü
def rotate_coord(x, y, theta=np.pi/4):
    x_rot = x * np.cos(theta) - y * np.sin(theta)
    y_rot = x * np.sin(theta) + y * np.cos(theta)
    return x_rot, y_rot

# Sin fonksiyonu
def sin_func(var, freq, phase):
    return np.sin(2 * np.pi * freq * var + phase)

# AbsSin fonksiyonu
def abs_sin(var):
    return np.abs(np.sin(var))

# Mix fonksiyonu
def mix(a, b, t):
    return a * (1 - t) + b * t

# Görüntü boyutları
width, height = 256, 256

# Koordinat grid'i oluştur
x = np.linspace(0, 1, width)
y = np.linspace(0, 1, height)
X, Y = np.meshgrid(x, y)

# Rotasyon dönüşümü uygula
X_rot, Y_rot = rotate_coord(X, Y)

# Formülün hesaplanması
palette1 = np.array([-0.578125, -0.945312, -0.460938])[:, None, None]
sin_palette1 = sin_func(palette1, 2.1658, 2.7498)
mix_y_x = mix(Y_rot, X_rot, X_rot)
abs_sin_y = abs_sin(Y_rot)

mix1 = mix(sin_palette1, mix_y_x, abs_sin_y)

palette2 = np.array([0.671875, -0.78125, -0.304688])[:, None, None]
mix_palette2_y_x = mix(palette2, Y_rot, X_rot)
sin_mix2 = sin_func(mix_palette2_y_x, 1.79861, 4.40506)

palette3 = np.array([0.804688, 0.6875, -0.414062])[:, None, None]
mix_y_palette3 = mix(Y_rot, palette3, X_rot)
mix_x_y = mix(X_rot, Y_rot, Y_rot)
palette4 = np.array([0.867188, 0.828125, 0.539062])[:, None, None]
palette5 = np.array([-0.789062, 0.0546875, 0.1875])[:, None, None]
mix_palette4_x_palette5 = mix(palette4, X_rot, palette5)
mix3 = mix(mix_y_palette3, mix_x_y, mix_palette4_x_palette5)

mix_result = mix(mix1, sin_mix2, mix3)

sin1 = sin_func(mix_result, 0.509853, 1.94753)
sin2 = sin_func(sin1, 1.60346, 4.52132)
image = sin_func(sin2, 0.666452, 2.83759)

# RGB görüntüsü oluştur ve normalizasyon yap
image_rgb = np.stack([image[0], image[1], image[2]], axis=-1)
image_rgb = (image_rgb - image_rgb.min()) / (image_rgb.max() - image_rgb.min())

# Kanal fonksiyonları
R = np.sin(X**2 + Y) * np.cos(Y**2)
G = np.cos(np.sin(X * Y)) * np.tanh(X - Y)
B = np.sin(np.exp(X / 2) + Y**2)

# 2x2 grid: RGB görüntüsü ve 3D yüzey grafikleri
fig = plt.figure(figsize=(12, 12))

# RGB Resim
ax1 = fig.add_subplot(221)
ax1.imshow(image_rgb, origin='lower')
ax1.set_title("Matematiksel RGB Resim")
ax1.axis('off')

# Kırmızı kanal 3D yüzey
ax2 = fig.add_subplot(222, projection='3d')
surf2 = ax2.plot_surface(X, Y, R, cmap='Reds', edgecolor='none')
ax2.set_title('Kırmızı: sin(x² + y) * cos(y²)')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Değer')
fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)

# Yeşil kanal 3D yüzey
ax3 = fig.add_subplot(223, projection='3d')
surf3 = ax3.plot_surface(X, Y, G, cmap='Greens', edgecolor='none')
ax3.set_title('Yeşil: cos(sin(xy)) * tanh(x - y)')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Değer')
fig.colorbar(surf3, ax=ax3, shrink=0.5, aspect=5)

# Mavi kanal 3D yüzey
ax4 = fig.add_subplot(224, projection='3d')
surf4 = ax4.plot_surface(X, Y, B, cmap='Blues', edgecolor='none')
ax4.set_title('Mavi: sin(e^(x/2) + y²)')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Değer')
fig.colorbar(surf4, ax=ax4, shrink=0.5, aspect=5)

# Kaydet ve göster
plt.tight_layout()
plt.savefig('math_art_output.png', dpi=300, bbox_inches='tight')
plt.show()
