from ultralytics import YOLO
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("wtdc/data/지금보니까한국아님.mp4")   

# 2. 카메라 해상도 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
fps = cap.get(cv2.CAP_PROP_FPS)

# 3. 모델 로드
model = YOLO("yolo11n.pt")

# 4. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if success:
        results = model(frame)
        annotated_frame = results[0].plot()
        cv2.imshow("VIDEO", annotated_frame)
            
        # "q"키를 눌러서 종료
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
cap.release()
cv2.destroyAllWindows()