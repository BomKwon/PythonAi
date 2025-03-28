from ultralytics import YOLO

# 모델 로드
model = YOLO("yolo11n-pose.pt")

# 모델 훈련
results = model.train(
    data = "v6_advanced_yolo.py\hand-keypoints.yaml",
    epochs = 40,
    imgsz = 320,
    batch = 2
)

# epochs, imgsz, batch 변경해서 학습해보기!
# Train할때 데이터 imagsz=320 => Predict imgsz=320 으로 동일하게!