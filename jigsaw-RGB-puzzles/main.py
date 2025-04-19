import cv2
import numpy as np
import random

# Load the image
image_path = "amasya-elmasi.png"
img = cv2.imread(image_path)
size = min(img.shape[:2])  # Ensure square image
img = cv2.resize(img, (size, size))

# Define puzzle grid size
grid_size = 4  # 4x4 grid
tile_size = size // grid_size

# Split image into tiles
tiles = [img[i*tile_size:(i+1)*tile_size, j*tile_size:(j+1)*tile_size] 
         for i in range(grid_size) for j in range(grid_size)]

# Shuffle tiles randomly
random.shuffle(tiles)

# Reconstruct shuffled image
puzzle_img = np.zeros_like(img)
for idx, tile in enumerate(tiles):
    i, j = divmod(idx, grid_size)
    puzzle_img[i*tile_size:(i+1)*tile_size, j*tile_size:(j+1)*tile_size] = tile

# Save and display
cv2.imwrite("jigsaw_puzzle.jpg", puzzle_img)
cv2.imshow("Jigsaw Puzzle", puzzle_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
