import cv2 as cv
from pointmarker import PointMarker  # Import the class
import numpy as np

# Path to your image
image_path = "data/TestVehicle.png"

# Load the image using OpenCV
image = cv.imread(image_path)

# Check if the image is loaded properly
if image is None:
    print("Error: Unable to load image. Check the path.")
    exit()

# Initialize the PointMarker
marker = PointMarker()

# Run the marker to mark points
print("Click on the image to mark points. Press 'q' to quit.")
marked_points = marker(image)

# Display the marked points
print("Points marked on the image:")
for idx, point in enumerate(marked_points):
    print(f"Point {idx + 1}: {point}")

# Ensure there are exactly four points
if len(marked_points) < 4:
    print("Error: You need to mark exactly four points.")
else:
    # Convert points to a NumPy array of shape (4, 1, 2)
    points = np.array(marked_points, dtype=np.int32).reshape((-1, 1, 2))

    # Create a copy of the original image for the overlay
    overlay = image.copy()

    # Define a light color in BGR (e.g., light blue)
    light_color = (200, 200, 255)  # BGR format: Light blue

    # Fill the quadrilateral with the light color
    cv.fillPoly(overlay, [points], light_color)

    # Add transparency to the filled polygon
    alpha = 0.4  # Transparency factor (0: fully transparent, 1: fully opaque)
    cv.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

    # Draw the polygon outline (optional)
    cv.polylines(image, [points], isClosed=True, color=(0, 0, 255), thickness=2)  # Red outline

    # Show the resulting image with the quadrilateral
    cv.imshow("Quadrilateral Drawn", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # Save the image with the quadrilateral
    output_path = "Markedvehicle.jpg"
    cv.imwrite(output_path, image)
    print(f"Image with quadrilateral saved at: {output_path}")