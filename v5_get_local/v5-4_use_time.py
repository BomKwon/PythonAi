import cv2
import os
from datetime import datetime
import time

# 1. 저장 디렉토리 설정
SAVE_DIR = "time_captured_images"
os.makedirs(SAVE_DIR, exist_ok=True)

# 사진 간격 설정
CAPTURE_INTERVAL = 10
LAST_CAPTURE_TIME = 0

# 2. 카메라 불러오기
def capture_image():
    cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv001.stream/playlist.m3u")
    
    if not cap.isOpened():
        raise RuntimeError("카메라 연결 안됨")
    
    print("카메라 연결 됐습니다.")
    
    # 3. 카메라 프레임 읽기
    success, frame = cap.read()
    if success:
        timestamp = datetime.now().strftime("%Y%m%d_%M%S")
        file_path = os.path.join(SAVE_DIR, f"time_{timestamp}.jpg")
        
        # 3-1. 이미지 저장
        cv2.imwrite(file_path, frame)
        print(f"사진이 저장됐습니다. {file_path}")
    
    else:
        print("카메라 연결 안됐슴")

    
    # 4. 카메라 연결 해제
    cap.release()
    cv2.destroyAllWindows()
    
while True:
    current_time = time.time()
    # 설정된 간격으로 이미지 수집
    if current_time - LAST_CAPTURE_TIME >= CAPTURE_INTERVAL:
        capture_image()
        LAST_CAPTURE_TIME = current_time
        
    time.sleep(1) # 반복