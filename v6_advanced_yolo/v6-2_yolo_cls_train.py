from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolo11n-cls.pt")

# 2. 모델 훈련
model.train(
    data="wtdc/v6_advanced_yolo/datasets", # 훈련 데이터셋 경로
    epochs=10, #=> 학습 횟수는 우선 본인이 원하는 만큼
    batch=2,
    imgsz=640
)

# 데이터셋 클래스 3개 이상 학습 후 예측 확인해보기
# 각 클래스 이미지는 10장 이상
# datasets /
            # train /
                    # class1(강아지) /
                                    # 강아지 images
                    # class2(고양이) /
                                    # 고양이 images                       
# 같은 구