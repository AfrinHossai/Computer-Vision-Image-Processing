"""
CS136 Term Project - Improved Canny Edge Detection
--------------------------------------------------

This program applies Canny edge detection to all 4 project images.

The DW geology image has many fine rock textures, so it uses higher
Canny thresholds to reduce unnecessary small edges and produce a cleaner result.

Input folder:
Input_Images/

Output folder:
Canny_Edge_Detection/Canny_Edge_Images/

Required folder structure:

CS136_Term_Project/
│
├── Input_Images/
│   ├── coastline.jpg
│   ├── tahoe.jpg
│   ├── DW.jpg
│   └── marine_brood.jpg
│
└── Canny_Edge_Detection/
    ├── Canny_edge_detection.py
    └── Canny_Edge_Images/

How to run from terminal:

python3 Canny_Edge_Detection/Canny_edge_detection.py

or:

python Canny_Edge_Detection/Canny_edge_detection.py
"""

import cv2
from pathlib import Path


# --------------------------------------------------
# Set folder paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_DIR = BASE_DIR / "input_images"
OUTPUT_DIR = BASE_DIR / "Canny_Edge_detection" / "Canny_Edge_Images"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# List of input images
# --------------------------------------------------

image_files = [
    "coastline.JPG",
    "tahoe.JPG",
    "DW.jpg",
    "marine_brood.jpg"
]

# --------------------------------------------------
# Canny edge detection parameters
# --------------------------------------------------

# Gaussian blur is applied before Canny to reduce small noise.
GAUSSIAN_KERNEL_SIZE = (5, 5)

# Different images have different textures, so thresholds are adjusted per image.
# Lower thresholds detect more edges.
# Higher thresholds remove weak/noisy edges and keep stronger boundaries.

canny_thresholds = {
    "coastline.JPG": (50, 150),
    "tahoe.JPG": (50, 150),
    "DW.jpg": (50, 150),
    "marine_brood.jpg": (50, 150)
}

# --------------------------------------------------
# Apply Canny edge detection to each image
# --------------------------------------------------

for image_name in image_files:
    image_path = INPUT_DIR / image_name

    # Read original image
    image = cv2.imread(str(image_path))

    # Check if image loaded correctly
    if image is None:
        print(f"Error: Could not read {image_path}")
        print("Check that the image exists and the file name is correct.")
        continue

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur before Canny
    # This reduces noise and helps create cleaner edges.
    blurred_image = cv2.GaussianBlur(gray_image, GAUSSIAN_KERNEL_SIZE, 0)

    # Get threshold values for the current image
    low_threshold, high_threshold = canny_thresholds[image_name]

    # Apply Canny edge detector
    canny_edges = cv2.Canny(
        blurred_image,
        low_threshold,
        high_threshold
    )

    # Create output file name
    output_name = image_path.stem + "_canny.jpg"
    output_path = OUTPUT_DIR / output_name

    # Save final Canny edge image
    cv2.imwrite(str(output_path), canny_edges)

    print(f"Saved Canny edge image: {output_path}")
    print(f"Thresholds used for {image_name}: low={low_threshold}, high={high_threshold}")


print("Improved Canny edge detection completed for all images.")
