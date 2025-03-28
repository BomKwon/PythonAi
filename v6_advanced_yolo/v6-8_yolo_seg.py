from ultralytics import YOLO
import cv2

# Classify, Detect, Segment
# 분류, 탐지, 분할

# 모델 로드
model = YOLO("yolo11n-seg.pt")

# 모델 예측
results = model(
    "001.jpg",
)

# 결과 저장
image = results[0].plot()
cv2.imwrite("results.jpg", image)

# segment 데이터셋 구축 방법 => 구글링 => roboflow
# https://velog.io/@everglow83/Semantic-segmentation-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%83%9D%EC%84%B1-%EB%B0%A9%EB%B2%95roboflow
# 분류, 탐지, 분할 차이점

# 8에서 모델예측은 봄님이 가진 이미지로 바꿔주시면 되구요!