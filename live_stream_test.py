import cv2

# 尝试读取RTSP视频流
rtsp_url = "rtsp://192.168.2.243:9000"
cap = cv2.VideoCapture(rtsp_url)

if cap.isOpened():
    print("RTSP视频流已打开")
else:
    print("无法打开RTSP视频流")

# 尝试读取HTTP视频流
http_url = "http://192.168.2.243:9000"
cap = cv2.VideoCapture(http_url)

if cap.isOpened():
    print("HTTP视频流已打开")
else:
    print("无法打开HTTP视频流")

# 释放资源
cap.release()