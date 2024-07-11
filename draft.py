import cv2
from ultralytics import YOLO
from ultralytics.solutions import object_counter as oc

input_video_path = "street.mp4"
output_video_path = "street_object_counting.mp4"

video_capture = cv2.VideoCapture(input_video_path)
assert video_capture.isOpened(), "Illegal or non-existing video file"

video_width, video_height, video_fps = (
    int(video_capture.get(p))
    for p in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS)
)

video_writer = cv2.VideoWriter(
    output_video_path, cv2.VideoWriter_fourcc(*"mp4v"), video_fps, (video_width, video_height)
)

yolo = YOLO("yolov8n.pt")

# Initialize ObjectCounter
object_counter = oc.ObjectCounter(classes_names=yolo.names)

# Set reg_pts to cover the entire frame
object_counter.reg_pts = [(0, 0), (video_width, 0), (video_width, video_height), (0, video_height)]

# Manually set other attributes
object_counter.view_img = True
object_counter.draw_tracks = True

while video_capture.isOpened():
    success, frame = video_capture.read()
    if not success:
        break

    tracks = yolo.track(frame, persist=True, show=False, classes=[0])
    frame = object_counter.start_counting(frame, tracks)
    video_writer.write(frame)

video_capture.release()
video_writer.release()
cv2.destroyAllWindows()
