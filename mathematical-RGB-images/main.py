import numpy as np
import matplotlib.pyplot as plt

# 1. Resim boyutlarını ve koordinat sistemini tanımlama
# Burada -10 ile 10 arasında eşit aralıklı değerler üreterek x ve y dizilerini oluşturuyoruz.
width, height = 400, 400  # Resmin piksel boyutları
x = np.linspace(-10, 10, width)
y = np.linspace(-10, 10, height)
X, Y = np.meshgrid(x, y)  # Her noktanın (x, y) koordinatını elde etmek için

# 2. Matematiksel ifadelerle RGB kanallarını oluşturma
# Amacımız, her renk kanalı için [0, 1] aralığında değerler üreten fonksiyonlar tanımlamak.
# Bu fonksiyonlar tamamen matematiksel ilişkilere (trigonometrik fonksiyonlar) dayanmaktadır.

"""
1. Red Kanalı:
   R(X, Y) = 0.5 * (cos(3Y) * exp(-X^2 / 20) + 1)
   - cos(3Y): Y yönünde 2π/3 periyodlu osilasyon,
   - exp(-X^2 / 20): X yönünde Gaussian sönümleme,
   Normalizasyon: sonuç [0,1] aralığına çekiliyor.
"""
R = 0.5 * (np.cos(3 * Y) * np.exp(-X**2 / 20) + 1)

"""
2. Green Kanalı:
   G(X, Y) = 0.5 * (sin(2X) * exp(-Y^2 / 20) + 1)
   - sin(2X): X yönünde π periyodlu dalgalanma,
   - exp(-Y^2 / 20): Y yönünde Gaussian etkisi,
   Normalizasyon: -1 ile 1 arası değeri [0,1]'e getiriyor.
"""
G = 0.5 * (np.sin(2 * X) * np.exp(-Y**2 / 20) + 1)

"""
3. Blue Kanalı:
   B(X, Y) = arctan(X * Y) / π + 0.5
   - arctan: girdi [-π/2, π/2] aralığında çıktı üretir,
   - X ve Y'nin çarpımı: koordinatlar arası etkileşim,
   Normalizasyon: sonuç 0.5'den başlayarak [0,1]'e çekilir.
"""
B = (np.arctan(X * Y) / np.pi) + 0.5

# 3. RGB Resmini Oluşturma
# Üç kanalı birleştirip (stacking) resim verimizi oluşturuyoruz.
img = np.dstack((R, G, B))

# 4. Resmin Görselleştirilmesi
# Matplotlib'in imshow fonksiyonu ile oluşturduğumuz resmi gösteriyoruz.
plt.figure(figsize=(10, 8))
plt.imshow(img, extent=(x.min(initial=0), x.max(initial=0), y.min(initial=0), y.max(initial=0)))
plt.title("Matematiksel İfadeye Dayalı RGB Resim")
plt.xlabel("X Koordinatı")
plt.ylabel("Y Koordinatı")
plt.colorbar(label="Renk Yoğunluğu")  # Opsiyonel: renk yoğunluğu barı ekleyerek görselleştirme
plt.show()

# 5. 3B Mesh Plot ile Matematiksel İfadenin Yüzeyini Gösterme
# Her bir renk kanalını ayrı ayrı 3B mesh plot kullanarak, fonksiyonun uzaydaki dağılımını görselleştireceğiz.

# 5.1. Red Kanalı için 3B Mesh Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, R, cmap='viridis', edgecolor='none')
ax.set_title("3D Mesh Plot: Red Kanalı Yüzeyi")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("R Değeri")
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
plt.show()

# 5.2. Green Kanalı için 3B Mesh Plot
fig2 = plt.figure(figsize=(10, 8))
ax2 = fig2.add_subplot(111, projection='3d')
surf2 = ax2.plot_surface(X, Y, G, cmap='plasma', edgecolor='none')
ax2.set_title("3D Mesh Plot: Green Kanalı Yüzeyi")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("G Değeri")
fig2.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)
plt.show()

# 5.3. Blue Kanalı için 3B Mesh Plot
fig3 = plt.figure(figsize=(10, 8))
ax3 = fig3.add_subplot(111, projection='3d')
surf3 = ax3.plot_surface(X, Y, B, cmap='inferno', edgecolor='none')
ax3.set_title("3D Mesh Plot: Blue Kanalı Yüzeyi")
ax3.set_xlabel("X")
ax3.set_ylabel("Y")
ax3.set_zlabel("B Değeri")
fig3.colorbar(surf3, ax=ax3, shrink=0.5, aspect=5)
plt.show()
