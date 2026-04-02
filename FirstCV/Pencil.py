import cv2 as p

# Read image
image = p.imread("image.png")

if image is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = p.cvtColor(image, p.COLOR_BGR2GRAY)

# Invert grayscale
gray_inv = 255 - gray


# Blur the inverted image
blur = p.GaussianBlur(gray_inv, (21, 21), 0)

# Create sketch
sketch = p.divide(gray, 255 - blur, scale=256)

# Show result
# p.imshow('Sketch Image', sketch)
p.imshow("gryayscale",gray_inv)
# p.imshow("gryayscale",blur)
p.waitKey(0)
p.destroyAllWindows()