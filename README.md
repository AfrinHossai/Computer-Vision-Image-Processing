# Computer Vision and Image Processing

## Project Overview

This project was developed as a CS 136 term project at San José State University. It explores fundamental computer vision and image processing techniques using Python and OpenCV.

The project implements six image processing methods and applies them to a collection of images to examine image smoothing, edge detection, thresholding, line detection, and texture-based segmentation.

The goal is to understand how different computer vision algorithms process visual information and how their results vary across images with different characteristics.

## Technologies Used

- **Programming Language:** Python
- **Computer Vision Library:** OpenCV
- **Numerical Computing:** NumPy
- **Image Processing:** Filtering, edge detection, thresholding, and segmentation
- **Development Tools:** Python scripts and local development environment

## Implemented Techniques

### 1. Gaussian Filtering

Applies Gaussian smoothing to reduce image noise and soften fine details.

**Implementation:** `Gaussian_Filter/gaussian_filter.py`

### 2. Sobel Edge Detection

Uses image intensity gradients to identify edges and structural boundaries.

**Implementation:** `Sobel_Edge_detection/Sobel_edge_detection.py`

### 3. Canny Edge Detection

Uses the Canny algorithm to identify image edges. The implementation adjusts thresholds for images with complex textures.

**Implementation:** `Canny_Edge_detection/Canny_edge_detection.py`

### 4. Otsu Thresholding

Automatically selects a threshold to separate darker and brighter image regions.

**Implementation:** `Otsu_Thresholding/Otsu_thresholding.py`

### 5. Hough Transform

Uses Canny edge maps and the Hough line transform to identify line structures in images.

**Implementation:** `Hough_Transform/Hough_transform.py`

### 6. Texture Segmentation

Uses grayscale texture features, including local mean and standard deviation, with K-means clustering to segment images into texture regions.

**Implementation:** `Texture_segmentation/Texture_segmentation.py`

## Project Structure

```text
Computer-Vision-Image-Processing/
│
├── Gaussian_Filter/
│   ├── gaussian_filter.py
│   └── Gaussian_Filter_Images/
│
├── Sobel_Edge_detection/
│   ├── Sobel_edge_detection.py
│   └── Sobel_Edge_Images/
│
├── Canny_Edge_detection/
│   ├── Canny_edge_detection.py
│   └── Canny_Edge_Images/
│
├── Otsu_Thresholding/
│   ├── Otsu_thresholding.py
│   └── Otsu_Thresholding_Images/
│
├── Hough_Transform/
│   ├── Hough_transform.py
│   └── Hough_Images/
│
├── Texture_segmentation/
│   ├── Texture_segmentation.py
│   └── Texture_Segmentation_Images/
│
├── input_images/
│   ├── coastline.JPG
│   ├── DW.jpg
│   ├── marine_brood.jpg
│   └── tahoe.JPG
│
└── Computer_Vision_Project_Report.docx
```

The technique folders contain the Python implementations and their generated image results.

## Input Images

The project uses four images to test and compare the computer vision algorithms:

- `coastline.JPG`
- `DW.jpg`
- `marine_brood.jpg`
- `tahoe.JPG`

These images contain different visual structures and textures, making them useful for comparing the effects of image processing methods.

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/AfrinHossai/Computer-Vision-Image-Processing.git
```

### 2. Navigate to the Project

```bash
cd Computer-Vision-Image-Processing
```


### 3. Install Dependencies

Install the required Python packages using:

```bash
python3 -m pip install -r requirements.txt
```

The project uses OpenCV for image processing and NumPy for numerical operations.

**Note:** The dependency versions are not pinned. The scripts have been successfully executed on macOS, but installation has not been independently verified in a clean environment.



### 4. Check Input and Output Paths

Before running the scripts, make sure their folder paths match the repository structure.

The current scripts reference `Input_Images`, while the uploaded folder is named `input_images`. Some output folder names also differ in capitalization.

These differences need to be corrected before reliable execution on case-sensitive systems.

### 5. Run an Image Processing Script

From the repository's root directory, run Gaussian Filtering using:

```bash
python3 Gaussian_Filter/gaussian_filter.py
```

Other techniques can be executed using their corresponding Python scripts.

All six image processing scripts were successfully executed on macOS using the four included input images.

The scripts save processed images in their respective output folders.

**Note:** Installation and execution have not yet been independently verified in a clean environment.

## Project Results

The repository contains saved processed images for all six techniques.

The resulting images illustrate the effects of smoothing, gradient-based edge detection, Canny edge detection, automatic thresholding, Hough line detection, and texture-based segmentation.

## Project Report

The project report provides additional background, methodology, implementation details, and discussion of the image processing results.

**[View Project Report](Computer_Vision_Project_Report.docx)**

## Limitations

- Different images may require different processing parameters.
- Edge detection can be sensitive to image noise and texture.
- Thresholding performance depends on image intensity distributions.
- Hough line detection may identify unwanted lines in highly textured images.
- Texture segmentation results depend on feature selection and clustering parameters.


## Future Improvements

- Standardize input and output directories across all scripts.
- Add command-line arguments for input images and processing parameters.
- Provide automated evaluation and comparisons between techniques.
- Add reproducible dependency versions.
- Expand testing to additional image datasets.
- Improve the documentation with visual before-and-after comparisons.

## Author

**Afrin Hossain**

CS 136 — Computer Vision Term Project

San José State University

**GitHub:** [AfrinHossai](https://github.com/AfrinHossai)
