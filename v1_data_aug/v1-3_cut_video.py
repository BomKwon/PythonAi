from moviepy import *

# 비디오 파일 로드 및 특정 구간 잘라내기
clip = (
    VideoFileClip("가오리.mp4").subclipped(5, 10)
)

# 비디오 편집
# final_video = CompositeVideoClip([clip])

# 자막 추가하기
txt_clip = TextClip(
    font="Arially.otf", 
    text="korean why not",
    font_size=70,
    color='white'
)

txt_clip = txt_clip.with_position('center').with_duration(10)
final_clip = CompositeVideoClip([clip, txt_clip])

# 결과 비디오 저장
final_clip.write_videofile("final_videoo.mp4") 