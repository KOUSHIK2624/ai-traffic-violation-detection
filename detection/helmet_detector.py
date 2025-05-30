import cv2

def detect_helmet_violation(frame):
    violations = []
    # Dummy logic — replace with actual helmet detection later
    height, width, _ = frame.shape
    cv2.putText(frame, 'Helmet OK', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return frame, violations
