import cv2
import os
from detection.helmet_detector import detect_helmet_violation
from detection.seatbelt_detector import detect_seatbelt_violation
from detection.red_light_violation import detect_red_light_violation

# Load test image
image_path = 'uploads/test_image.jpg'
print(f'Looking for image at: {os.path.abspath(image_path)}')

if not os.path.exists(image_path):
    print('❌ Image not found. Please place test_image.jpg in the uploads folder.')
    exit()

frame = cv2.imread(image_path)

# Run detection modules
frame, _ = detect_helmet_violation(frame)
frame, _ = detect_seatbelt_violation(frame)
frame, _ = detect_red_light_violation(frame)

# Save annotated image
os.makedirs('outputs', exist_ok=True)
output_path = 'outputs/annotated_result.jpg'
cv2.imwrite(output_path, frame)
print(f'✅ Detection complete. Annotated image saved to: {output_path}')
