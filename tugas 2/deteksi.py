from ultralytics import YOLO
import cv2
import torch

#setup GPU
print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")
###

model = YOLO("trash_detection_v3.pt")

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    raise("No Camera")

while True:
    frame, image = cam.read()
    if not frame:
        break

    result = model.predict(image, show=True, conf = 0.5)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
