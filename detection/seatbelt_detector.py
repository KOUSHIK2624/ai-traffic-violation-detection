import cv2

def detect_seatbelt_violation(frame):
    violations = []
    # Dummy logic — replace with actual seatbelt detection
    cv2.putText(frame, 'Seatbelt OK', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    return frame, violations
