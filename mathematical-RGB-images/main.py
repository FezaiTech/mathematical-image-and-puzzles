import numpy as np
import matplotlib.pyplot as plt

# Image size
width, height = 512, 512

# Generate coordinate grids
x = np.linspace(-2, 2, width)
y = np.linspace(-2, 2, height)
X, Y = np.meshgrid(x, y)

# Define mathematical functions for RGB channels
R = np.sin(X**2 + Y**2)
G = np.cos(X * Y)
B = np.tanh(X - Y)

# Normalize to range [0, 1]
R = (R - R.min()) / (R.max() - R.min())
G = (G - G.min()) / (G.max() - G.min())
B = (B - B.min()) / (B.max() - B.min())

# Stack channels and save image
rgb_image = np.dstack((R, G, B))
plt.imsave("mathematical_rgb.png", rgb_image)

# Show the image
plt.imshow(rgb_image)
plt.axis("off")
plt.show()
