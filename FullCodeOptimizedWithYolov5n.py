from ultralytics import YOLO
from picamera2 import Picamera2
import cv2
import time

# Load YOLOv5n model
model = YOLO('yolov5n.pt')

# Initialize Picamera2
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()

time.sleep(1)  # Allow camera to warm up

# Detection control variables
frame_count = 0
detect_every_n = 5  # Run detection every 5 frames
results = None

while True:
    frame = picam2.capture_array()
    small_frame = cv2.resize(frame, (320, 240))  # Resize for speed
    frame_count += 1

    if frame_count % detect_every_n == 0:
        results = model(small_frame)[0]

    if results:
        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = model.names[cls]
            cv2.rectangle(small_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(small_frame, f'{label} {conf:.2f}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("YOLOv5n Detection", small_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
