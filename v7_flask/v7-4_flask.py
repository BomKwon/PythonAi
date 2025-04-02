from ultralytics import YOLO
import cv2
from flask import Flask, Response

# 실습: Flask 웹 영상에서 상태 메시지 정의

# 1. Flask 애플리케이션 초기화
app = Flask(__name__)

# 2. YOLO 모델 로드
model = YOLO('yolo11n.pt')

# 3. 비디오 스트리밍(처리) 함수 정의
def generate_frame():
    cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv006.stream/playlist.m3u8")

    while True:
        
        # 3-1. 프레임 확인
        success, frame = cap.read()
        if not success:
            print("FRAME CHECK")
            break
        
        # 3-2. 객체 탐지
        results = model(frame)
        
        # 3-4. 객체 수 추출
        # 탐지 표시
        annotated_frame = results[0].plot()
        
        # 3-5. 상태 메시지 정의
        number = len(results[0])
        if number <= 5:
            status = "Nomal"
            color = (0, 255, 0) # 초록색
        elif 6 <= number <= 10:
            status = "Warning"
            color = (0, 165, 255) # 주황색
        else:
            status = "Danger"
            color = (0, 0, 255) # 빨간색

        print(f"탐지된 개수: {number}, 상태: {status}")
        
        annotated_frame = results[0].plot()
        
        # 3-6. 상태 메시지 화면 추가
        cv2.putText(
            annotated_frame,
            f"Detected: {number}, Status: {status}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2,
            cv2.LINE_AA
        )

        # 3-7. 프레임을 인코딩
        _, buffer = cv2.imencode('.jpg', annotated_frame)

        # 3-8. 인코딩을 바이트
        frame_bytes = buffer.tobytes()

        # 3-9. 데이터 전송(yield)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
               )
        
    cap.release()
    
# 4. Flask 라우드 정의
@app.route('/')
def video_feed():
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

# 5. 애플리케이션 실행
if __name__ == ("__main__"):
    # Flask 서버를 실행
    app.run(host='0.0.0.0', port=5000, debug=True)
    # app.run()

