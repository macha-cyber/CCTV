import cv2
import requests
import time
from ultralytics import YOLO

API_URL = "http://api:8000/event"

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

last_trigger = 0
COOLDOWN = 5  # 秒

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    results = model(frame, verbose=False)

    person_count = 0

    for box in results[0].boxes:
        cls = int(box.cls[0])
        if cls == 0:  # person
            person_count += 1

    now = time.time()

    if person_count > 0 and now - last_trigger > COOLDOWN:

        print("🚨 PERSON DETECTED")

        requests.post(API_URL, json={
            "type": "person_detected",
            "count": person_count
        })

        last_trigger = now