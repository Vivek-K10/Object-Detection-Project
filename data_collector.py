import os
import cv2
import time
import uuid

IMAGE_PATH = "CollectedImages"

labels = ['Hello', 'Yes', 'No', 'Thanks', 'ILoveYou', 'Please']
number_of_images = 5

# Create base folder
os.makedirs(IMAGE_PATH, exist_ok=True)

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path, exist_ok=True)

    print(f"\n=== Collecting images for: {label} ===")
    print("Starting camera in 2 seconds...")
    time.sleep(5)

    # Open the camera correctly
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("ERROR: Could not access camera.")
        continue

    print("Camera started. Press 'q' to stop early.")

    for img_num in range(number_of_images):
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Construct image name
        imagename = os.path.join(img_path, f"{label}_{uuid.uuid1()}.jpg")

        # Save image
        cv2.imwrite(imagename, frame)

        # Show preview
        cv2.imshow("frame", frame)

        print(f"Saved: {imagename}")
        time.sleep(5)

        # Exit early
        if cv2.waitKey(5) & 0xFF == ord('q'):
            print("Early quit.")
            break

    cap.release()

cv2.destroyAllWindows()
print("\n=== Data collection complete ===")
