from ultralytics import YOLO
import cv2
import time

# YOLO 5~11 모델 속도와 정확도를 비교해보세요

# 1. 모델 목록
models = [
    "yolov5n.pt",
    "yolov6n.yaml",
    "yolov8n.pt",
    "yolov9c.pt",
    "yolov10n.pt"
]

# 2. 테스트 이미지
image_path = "001.jpg"

# 3. 각 모델에 대해 추론 속도 및 정확도 비교

for i in models:
    # 3-1. 모델 로드
    model = YOLO(i)

    # 3-2. 모델 추론 시작 시간
    start_time = time.time()

    # 3-3. 이미지에 대한 예측 수행
    results = model(image_path, save=True)

    # 3-4. 모델 추론 종료 시간
    end_time = time.time()

    # 3-5. 모델 추론 시간 계산
    inference_time = end_time - start_time
    
    # 3-6. 모델 추론 결과 시각화
    image = results[0].plot()
    
    # 3-7. 결과 이미지 저장
    result_image_path = f"./result_{i.split('.')[0]}.jpg"
    cv2.imwrite(result_image_path, image)

    # 3-8. 모델 정보 출력
    print("----------------------")
    print(f"모델: {i}")
    print(f"추론 시간: {inference_time}")
    print("----------------------") 