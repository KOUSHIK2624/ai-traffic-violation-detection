import cv2
from ultralytics import YOLO
from detection.helmet_detector import detect_helmet_violation
from ocr.plate_recognizer import detect_license_plate
import os

os.makedirs('outputs', exist_ok=True)

image_path = os.path.join(os.getcwd(), 'uploads', 'test_image.jpg')
print(f'Looking for image at: {image_path}\n')

frame = cv2.imread(image_path)
model = YOLO('yolov8n.pt')

results = model(frame)
annotated_frame = results[0].plot()

annotated_frame, violations = detect_helmet_violation(annotated_frame)

for (x1, y1, x2, y2) in violations:
    print(f'🚫 Helmet violation detected at [{x1}, {y1}, {x2}, {y2}]')

plates = detect_license_plate(annotated_frame)
print('\n🔍 Plates detected:', plates)

output_path = os.path.join('outputs', 'annotated_result.jpg')
cv2.imwrite(output_path, annotated_frame)
print(f'\n✅ Detection complete. Annotated image saved to: {output_path}')
