from ultralytics import YOLO
import cv2

# 1. 모델 로드
# model = YOLO("yolo11n-cls.pt")
model = YOLO("runs/classify/train3/weights/best.pt") # 본인이 6-2에서 만든 모델

# 2. 모델 예측
results = model(
    "wtdc/v6_advanced_yolo/datasets/val/dog/puppy2.jpg",
    save=True
)

# 이미지 저장
# image = results[0].plot()
# cv2.imwrite("results_image_cls.jpg", image)

