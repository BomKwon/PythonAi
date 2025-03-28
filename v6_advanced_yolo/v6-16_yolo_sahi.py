from sahi.predict import get_sliced_prediction
from sahi import AutoDetectionModel

# 모델 경로 설정
model_path = "yolo11n.pt"

# 모델 예측 준비
detection_model = AutoDetectionModel.from_pretrained(
    model_type="ultralytics",
    model_path=model_path,
    confidence_threshold=0.4
)

# sahi 예측
results = get_sliced_prediction(
    "WTDC/v6_advanced_yolo/datasets/people2.jpg",
    detection_model,
    slice_height=100,
    slice_width=100,
    overlap_height_ratio=0.3,
    overlap_width_ratio=0.3
)

# 예측 결과 시각화
results.export_visuals(export_dir="sahi/slice")
print("SAHI_SUCCESS")