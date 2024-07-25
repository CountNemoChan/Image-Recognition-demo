import cv2

from ultralytics import YOLO, solutions

model = YOLO("../yolov8x.pt").to("mps") # Generally, we use "cuda" to accelerate
cap = cv2.VideoCapture("street.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Define region points
region_points = [(0, 0), (w, 0), (w, h), (0, h)]

# Video writer
video_writer = cv2.VideoWriter("object_counting_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Init Object Counter
counter = solutions.ObjectCounter(
    view_img=True,
    reg_pts=region_points,
    classes_names=model.names,
    draw_tracks=True,
    line_thickness=2,
)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    tracks = model.track(im0, persist=True, show=False, classes=[0])

    im0 = counter.start_counting(im0, tracks)
    video_writer.write(im0)
    #print(tracks)

cap.release()
video_writer.release()
cv2.destroyAllWindows()