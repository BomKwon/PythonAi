from ultralytics import YOLO
import cv2

# 모델 로드
model = YOLO("yolo11n.pt")

# 비디오 생성
cap = cv2.VideoCapture("car.mp4")

# 프레임처리
while cap.isOpened():
    success, frame = cap.read()
    
    if success:
        results = model.track(frame, persist=True, stream=True)
        
        for result in results:
            # 시각화
            annotated_frame = result.plot()
            
            # 화면 출력
            cv2.namedWindow("HTTPS", cv2.WINDOW_NORMAL)
            cv2.imshow("HTTPS", annotated_frame)
            
        # "q"키를 눌러서 나가기
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("q를 눌러서 종료했습니다.")
            break
    else:
        print("프레임 확인해주세요.")
        break

cap.release()
cv2.destroyAllWindows() 