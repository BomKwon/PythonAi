from ultralytics import YOLO
import cv2
import timeit

# 1. 모델 로드
model = YOLO("yolo11n.pt")

# v3_cv2_yolo/v3-5_puttext_yolo.py 참고하여 
# 영상 출력시 화면에 상태 정의가 표시될 수 있도록 코드 수정

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("https://cctvsec.ktict.co.kr/6066/Q6gk5AOyeKlKa8hEb8RypXKsp4AyvcNi1ziVItrRp48Ry72I4AlIJv/6LZq8M744")

# 2. 비디오 프레임 가져오기
fps = cap.get(cv2.CAP_PROP_FPS)

# 3. 모델로드
model = YOLO("yolo11n.pt")

# 4. 비디오 프레임 처리
while cap.isOpened():
    suc, fr = cap.read()
    
    if suc:
        start_time = timeit.default_timer()
        
        results = model(fr)
        
        annotated_frame = results[0].plot()
        boxes = results[0].boxes # 탐지된 객체의 정보(좌표, 클래스 등)
        
        count = 0
        
        for i in boxes.cls:
            count += 1
            
        end_time = timeit.default_timer()
        
        FPS = int(1./(end_time - start_time))
        
        # 3. 상태 정의
        number = len(results[0])
        print(f"탐지된 개수: {number}")
        if number <= 2:
            status = "Nomal"
        elif 3 <= number <= 6:
            status = "Warning"
        else:
            status = "Danger"
            
        # 화면에 텍스트 표시
        if status == "Nomal":
            cv2.putText(
                annotated_frame, # (나타낼 화면)
                f"number: {number}, status: {status}", # (텍스트)
                (10, 30), # (표시 위치)
                cv2.FONT_HERSHEY_SIMPLEX, # (폰트)
                1, # (텍스트 굵기)
                (0, 255, 0), # (텍스트 색상)
                2, # (???)
                cv2.LINE_AA # (???)
            )
        elif status == "Warning":
            cv2.putText(
                annotated_frame, # (나타낼 화면)
                f"number: {number}, status: {status}", # (텍스트)
                (10, 30), # (표시 위치)
                cv2.FONT_HERSHEY_SIMPLEX, # (폰트)
                1, # (텍스트 굵기)
                (0, 255, 255), # (텍스트 색상)
                2, # (???)
                cv2.LINE_AA # (???)
            )
        elif status == "Danger":
            cv2.putText(
                annotated_frame, # (나타낼 화면)
                f"number: {number}, status: {status}", # (텍스트)
                (10, 30), # (표시 위치)
                cv2.FONT_HERSHEY_SIMPLEX, # (폰트)
                1, # (텍스트 굵기)
                (0, 0, 255), # (텍스트 색상)
                2, # (???)
                cv2.LINE_AA # (???)
            )
        
        # 결과 화면 출력
        cv2.imshow("PUT_TEXT", annotated_frame)
        
        # "q"키를 눌러서 나가기
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()