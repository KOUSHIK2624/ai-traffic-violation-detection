from ultralytics import YOLO

model = YOLO('models/yolov8n.pt')

def detect_objects(frame, conf_threshold=0.5):
    results = model(frame)[0]
    detections = []
    for box in results.boxes.data.tolist():
        x1, y1, x2, y2, score, cls_id = box
        if score >= conf_threshold:
            detections.append({
                "bbox": [int(x1), int(y1), int(x2), int(y2)],
                "confidence": float(score),
                "class_id": int(cls_id),
                "class_name": model.names[int(cls_id)]
            })
    return detections
