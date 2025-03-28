from ultralytics import solutions
import cv2
import shapely

# 비디오 로드
cap=cv2.VideoCapture(0)

# 이메일 인증 정보
from_email = "kweonbom@gmail.com"
password = "nlai sxtv dvic cula"
to_email = "kweonbom@gmail.com"

# 보안 알림 시스템 객체 생성
security = solutions.SecurityAlarm(
    model='yolo11n.pt',    
    record=1 # 탐지된 객체 수가 record 수 이상일 떄 이메일 전송합니다.
)

# 이메일 인증
security.authenticate(from_email, password, to_email)

# 프레임처리
while cap.isOpened():
    success, frame = cap.read()
    if success:
        result_data = security.monitor(frame)
    else:
        print("프레임 처리 실패")
        break
    
# 종료
cap.release()
cv2.destroyAllWindows()

print("알람이 전송 되었습니다.")