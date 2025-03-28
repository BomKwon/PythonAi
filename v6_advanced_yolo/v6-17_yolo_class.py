from ultralytics import YOLO

# 1. 모델 로드
model = YOLO('yolo11n.pt')

# 2. 모델 예측
results = model(
    "wtdc/v6_advanced_yolo/datasets/cafe.jpg",
    save=True
)