import numpy as np
import matplotlib.pyplot as plt


# Coordinate transformation functions
def rotate_coord(x, y, theta=np.pi / 4):
    """Rotate coordinates by angle theta."""
    x_rot = x * np.cos(theta) - y * np.sin(theta)
    y_rot = x * np.sin(theta) + y * np.cos(theta)
    return x_rot, y_rot


# Mathematical functions
def sin_func(var, freq, phase):
    """Calculate sine function with frequency and phase."""
    return np.sin(2 * np.pi * freq * var + phase)


def abs_sin(var):
    """Calculate absolute sine function."""
    return np.abs(np.sin(var))


def mix(a, b, t):
    """Linear interpolation between a and b using t."""
    return a * (1 - t) + b * t


# Channel functions
def red_channel(x, y):
    """Calculate red channel value."""
    return np.sin(x ** 2 + y) * np.cos(y ** 2)


def green_channel(x, y):
    """Calculate green channel value."""
    return np.cos(np.sin(x * y)) * np.tanh(x - y)


def blue_channel(x, y):
    """Calculate blue channel value."""
    return np.sin(np.exp(x / 2) + y ** 2)


# Image generation
def generate_image(width=256, height=256):
    """Generate mathematical RGB image."""
    # Create coordinate grid
    x = np.linspace(0, 1, width)
    y = np.linspace(0, 1, height)
    X, Y = np.meshgrid(x, y)

    # Apply rotation transformation
    x_rot, y_rot = rotate_coord(X, Y)

    # Calculate formula components
    palette1 = np.array([-0.578125, -0.945312, -0.460938])[:, None, None]
    sin_palette1 = sin_func(palette1, 2.1658, 2.7498)
    mix_y_x = mix(y_rot, x_rot, x_rot)
    abs_sin_y = abs_sin(y_rot)
    mix1 = mix(sin_palette1, mix_y_x, abs_sin_y)

    palette2 = np.array([0.671875, -0.78125, -0.304688])[:, None, None]
    mix_palette2_y_x = mix(palette2, y_rot, x_rot)
    sin_mix2 = sin_func(mix_palette2_y_x, 1.79861, 4.40506)

    palette3 = np.array([0.804688, 0.6875, -0.414062])[:, None, None]
    mix_y_palette3 = mix(y_rot, palette3, x_rot)
    mix_x_y = mix(x_rot, y_rot, y_rot)
    palette4 = np.array([0.867188, 0.828125, 0.539062])[:, None, None]
    palette5 = np.array([-0.789062, 0.0546875, 0.1875])[:, None, None]
    mix_palette4_x_palette5 = mix(palette4, x_rot, palette5)
    mix3 = mix(mix_y_palette3, mix_x_y, mix_palette4_x_palette5)

    # Combine components
    mix_result = mix(mix1, sin_mix2, mix3)
    sin1 = sin_func(mix_result, 0.509853, 1.94753)
    sin2 = sin_func(sin1, 1.60346, 4.52132)
    image = sin_func(sin2, 0.666452, 2.83759)

    # Create and normalize RGB image
    image_rgb = np.stack([image[0], image[1], image[2]], axis=-1)
    image_rgb = (image_rgb - image_rgb.min()) / (image_rgb.max() - image_rgb.min())

    return X, Y, image_rgb


# Visualization
def create_visualization(X, Y, image_rgb):
    """Create 2x2 visualization with RGB image and 3D channel surfaces."""
    fig = plt.figure(figsize=(12, 12))

    # RGB Image
    ax1 = fig.add_subplot(221)
    ax1.imshow(image_rgb, origin='lower')
    ax1.set_title("Mathematical RGB Image")
    ax1.axis('off')

    # Red channel 3D surface
    ax2 = fig.add_subplot(222, projection='3d')
    surf2 = ax2.plot_surface(X, Y, red_channel(X, Y), cmap='Reds', edgecolor='none')
    ax2.set_title('Red: sin(x² + y) * cos(y²)')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Value')
    fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)

    # Green channel 3D surface
    ax3 = fig.add_subplot(223, projection='3d')
    surf3 = ax3.plot_surface(X, Y, green_channel(X, Y), cmap='Greens', edgecolor='none')
    ax3.set_title('Green: cos(sin(xy)) * tanh(x - y)')
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Value')
    fig.colorbar(surf3, ax=ax3, shrink=0.5, aspect=5)

    # Blue channel 3D surface
    ax4 = fig.add_subplot(224, projection='3d')
    surf4 = ax4.plot_surface(X, Y, blue_channel(X, Y), cmap='Blues', edgecolor='none')
    ax4.set_title('Blue: sin(e^(x/2) + y²)')
    ax4.set_xlabel('X')
    ax4.set_ylabel('Y')
    ax4.set_zlabel('Value')
    fig.colorbar(surf4, ax=ax4, shrink=0.5, aspect=5)

    # Finalize layout and save
    plt.tight_layout()
    plt.savefig('math_art_output.png', dpi=300, bbox_inches='tight')


# Main execution
if __name__ == "__main__":
    X, Y, image_rgb = generate_image()
    create_visualization(X, Y, image_rgb)
