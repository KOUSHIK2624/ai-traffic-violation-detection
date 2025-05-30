import cv2

def detect_red_light_violation(frame):
    violations = []
    # Dummy logic — replace with actual red light detection
    cv2.putText(frame, 'No Red Light Violation', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    return frame, violations
