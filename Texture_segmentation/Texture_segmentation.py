"""
CS136 Term Project - Texture-Based Image Segmentation
-----------------------------------------------------

This program performs texture-based image segmentation on all 4 project images.

The project requirement says to try grayscale first, so this code uses
grayscale texture features.

Main idea:
1. Convert the image to grayscale.
2. Compute local texture features:
   - local mean intensity
   - local standard deviation
3. Use K-means clustering to group pixels into texture regions.
4. Save only the final segmented image for each input image.

Input folder:
Input_Images/

Output folder:
Texture_Segmentation/Texture_Segmentation_Images/

Required folder structure:

CS136_Term_Project/
│
├── Input_Images/
│   ├── coastline.jpg
│   ├── tahoe.jpg
│   ├── DW.jpg
│   └── marine_brood.jpg
│
└── Texture_Segmentation/
    ├── Texture_segmentation.py
    └── Texture_Segmentation_Images/

How to run from terminal:

python3 Texture_Segmentation/Texture_segmentation.py

or:

python Texture_Segmentation/Texture_segmentation.py
"""

import cv2
import numpy as np
from pathlib import Path


# --------------------------------------------------
# Set folder paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_DIR = BASE_DIR / "input_images"
OUTPUT_DIR = BASE_DIR / "Texture_segmentation" / "Texture_Segmentation_Images"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# Input image names
# --------------------------------------------------

image_files = [
    "coastline.JPG",
    "tahoe.JPG",
    "DW.jpg",
    "marine_brood.jpg"
]

# --------------------------------------------------
# Texture segmentation parameters
# --------------------------------------------------

# Window size for local texture analysis.
# Larger values create smoother texture regions.
TEXTURE_WINDOW_SIZE = 15

# Number of texture regions.
# 3 separates the image into low, medium, and high texture regions.
NUM_TEXTURE_REGIONS = 3


# --------------------------------------------------
# Texture segmentation function
# --------------------------------------------------

def texture_segmentation(image):
    """
    Segment an image based on local grayscale texture.

    Returns:
        segmented_image: final texture segmented image
    """

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert to float for mathematical calculations
    gray_float = gray.astype(np.float32)

    # Compute local mean intensity
    local_mean = cv2.blur(
        gray_float,
        (TEXTURE_WINDOW_SIZE, TEXTURE_WINDOW_SIZE)
    )

    # Compute local mean of squared intensity
    local_mean_square = cv2.blur(
        gray_float ** 2,
        (TEXTURE_WINDOW_SIZE, TEXTURE_WINDOW_SIZE)
    )

    # Compute local variance
    local_variance = local_mean_square - (local_mean ** 2)

    # Remove small negative values caused by numerical error
    local_variance = np.maximum(local_variance, 0)

    # Compute local standard deviation
    # Standard deviation represents texture strength.
    local_std = np.sqrt(local_variance)

    # Normalize features to 0-255
    local_mean_norm = cv2.normalize(
        local_mean,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )

    local_std_norm = cv2.normalize(
        local_std,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )

    # Create a feature vector for each pixel:
    # Feature 1 = local mean intensity
    # Feature 2 = local texture strength
    features = np.float32(
        np.dstack((local_mean_norm, local_std_norm)).reshape((-1, 2))
    )

    # K-means stopping criteria
    criteria = (
        cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
        100,
        0.2
    )

    # Apply K-means clustering
    compactness, labels, centers = cv2.kmeans(
        features,
        NUM_TEXTURE_REGIONS,
        None,
        criteria,
        10,
        cv2.KMEANS_RANDOM_CENTERS
    )

    # Convert labels back to original image shape
    labels_image = labels.reshape(gray.shape)

    # Convert cluster labels into visible grayscale regions
    segmented_image = np.uint8(
        255 * labels_image / (NUM_TEXTURE_REGIONS - 1)
    )

    return segmented_image


# --------------------------------------------------
# Apply texture segmentation to all images
# --------------------------------------------------

for image_name in image_files:
    image_path = INPUT_DIR / image_name

    # Read original image
    image = cv2.imread(str(image_path))

    if image is None:
        print(f"Error: Could not read {image_path}")
        print("Check that the image exists and the file name is correct.")
        continue

    # Perform texture-based segmentation
    segmented_image = texture_segmentation(image)

    # Save final segmented image only
    output_name = image_path.stem + "_texture_segmented.jpg"
    output_path = OUTPUT_DIR / output_name

    cv2.imwrite(str(output_path), segmented_image)

    print(f"Saved texture segmented image: {output_path}")


print("Texture-based image segmentation completed for all images.")
