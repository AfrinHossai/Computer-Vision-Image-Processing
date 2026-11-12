"""
CS136 Term Project - Gaussian Filter
------------------------------------

This program applies a Gaussian filter to all 4 project images.

Input folder:
Input_Images/

Output folder:
Gaussian_Filter/Gaussian_Filter_Images/

Required folder structure:

CS136_Term_Project/
│
├── Input_Images/
│   ├── coastline.jpg
│   ├── tahoe.jpg
│   ├── DW.jpg
│   └── marine_brood.jpg
│
└── Gaussian_Filter/
    ├── Gaussian_filter.py
    └── Gaussian_Filter_Images/

How to run from terminal:

python Gaussian_Filter/Gaussian_filter.py

If that does not work, use:

python3 Gaussian_Filter/Gaussian_filter.py
"""

import cv2
from pathlib import Path


# --------------------------------------------------
# Set folder paths
# --------------------------------------------------

# BASE_DIR means the main project folder: CS136_Term_Project
BASE_DIR = Path(__file__).resolve().parents[1]

# Folder containing the original 4 images
INPUT_DIR = BASE_DIR / "Input_Images"

# Folder where Gaussian filtered images will be saved
OUTPUT_DIR = BASE_DIR / "Gaussian_Filter" / "Gaussian_Filter_Images"

# Create output folder if it does not already exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# List of input images
# Make sure your image names match these names exactly
# --------------------------------------------------

image_files = [
    "coastline.jpg",
    "tahoe.jpg",
    "DW.jpg",
    "marine_brood.jpg"
]


# --------------------------------------------------
# Gaussian filter parameters
# --------------------------------------------------

# Kernel size controls the area used for smoothing.
# It must use odd numbers, such as (3, 3), (5, 5), or (7, 7).
# (5, 5) gives a moderate blur for these images.
KERNEL_SIZE = (5, 5)

# Sigma controls the amount of blur.
# 0 allows OpenCV to calculate sigma automatically.
SIGMA = 0


# --------------------------------------------------
# Apply Gaussian filter to each image
# --------------------------------------------------

for image_name in image_files:
    image_path = INPUT_DIR / image_name

    # Read the original image
    image = cv2.imread(str(image_path))

    # Check whether the image was loaded correctly
    if image is None:
        print(f"Error: Could not read {image_path}")
        print("Check that the image exists and the file name is correct.")
        continue

    # Apply Gaussian filter
    gaussian_image = cv2.GaussianBlur(image, KERNEL_SIZE, SIGMA)

    # Create output file name
    output_name = image_path.stem + "_gaussian.jpg"
    output_path = OUTPUT_DIR / output_name

    # Save the filtered image
    cv2.imwrite(str(output_path), gaussian_image)

    print(f"Saved Gaussian filtered image: {output_path}")


print("Gaussian filtering completed for all images.")
