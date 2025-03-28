import cv2 # pip install opencv-python
import os
from datetime import datetime # => pip install datetime

def capture_image():
    # 1. 저장할 디렉토리 설정
    SAVE_DIR = "captured_images"
    os.makedirs(SAVE_DIR, exist_ok=True) # 디렉토리가 없으면 생성ㄹ, 있으면 무시합니다.

    # 2. 카메라 불러오기
    cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv001.stream/playlist.m3u")

    # 3. 카메라 확인
    if not cap.isOpened():
        raise RuntimeError("카메라 연결 안됨")

    print("카메라 연결 됐습니다.")

    # 4. 카메라 프레임 읽기
    success, frame = cap.read()
    if success:
        print("OPEN")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        file_path = os.path.join(SAVE_DIR, f"get_{timestamp}.jpg")
        
        # 5. 이미지 저장
        cv2.imwrite(file_path, frame)
        print(f"사진이 저장 됐습니다. {file_path}")

    else:
        print("프레임 못 읽습니다.")
        
    # 6. 카메라 해제
    cap.release()
    cv2.destroyAllWindows() 

# 위 이미지 수집 로직을 함수화
capture_image() ]# capture-image() => 코드 작성시 실행 될 수 있도록

# pip install opencv-contrib-python