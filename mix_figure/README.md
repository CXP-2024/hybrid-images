# Hybrid Image Creator

This project creates hybrid images by combining a low-pass filtered version of one image with a high-pass filtered version of another image. The resulting hybrid image appears different when viewed from different distances.

## How it Works

1. The first image is processed with a low-pass filter (Gaussian blur), which keeps the low-frequency components.
2. The second image is processed with a high-pass filter (original minus Gaussian blur), which keeps the high-frequency components.
3. The two processed images are combined to create the hybrid image.

## Usage

1. Place your input images in the same directory
2. Run the script:
```bash
python hybrid_image.py
```

3. The script will create three output files:
   - `low_pass.jpg`: The low-pass filtered first image
   - `high_pass.jpg`: The high-pass filtered second image
   - `hybrid.jpg`: The final hybrid image

## Tips for Best Results

- Use images of similar size and composition
- Choose images with distinct features
- Adjust sigma values in the code to control the filtering strength
- View the hybrid image from different distances to see both images
