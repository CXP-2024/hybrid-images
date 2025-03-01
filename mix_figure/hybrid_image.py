import cv2
import numpy as np

def create_hybrid_image(img1_path, img2_path, sigma1=7, sigma2=20):
    # Read the images
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)
    
    # Resize images to the same size if they're different
    img1 = cv2.resize(img1, (350, 450))
    img2 = cv2.resize(img2, (350, 450))
    print(img2.shape[1], img2.shape[0])
    
    # Create low-pass filtered version of the first image
    low_pass = cv2.GaussianBlur(img1, (0, 0), sigma1)
    
    # Create high-pass filtered version of the second image
    gaussian = cv2.GaussianBlur(img2, (0, 0), sigma2)
    high_pass = cv2.subtract(img2, gaussian)
    
    # Combine the two images
    hybrid = cv2.add(low_pass, high_pass)
    
    return low_pass, high_pass, hybrid

if __name__ == "__main__":
    # Example usage
    img1_path = "mix_figure/einstein2.png"    # Replace with your first image
    img2_path = "mix_figure/monroe.png"    # Replace with your second image
    
    low_pass, high_pass, hybrid = create_hybrid_image(img1_path, img2_path)
    
    # Save the results
    cv2.imwrite("mix_figure/low_pass.jpg", low_pass)
    cv2.imwrite("mix_figure/high_pass.jpg", high_pass)
    cv2.imwrite("mix_figure/hybrid.jpg", hybrid)
    
    # Display results
    cv2.imshow("mix_figure/Low-pass", low_pass)
    cv2.imshow("mix_figure/High-pass", high_pass)
    cv2.imshow("Hybrid Image", hybrid)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()
