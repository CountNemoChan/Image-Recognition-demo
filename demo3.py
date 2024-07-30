import os
import pandas as pd
import numpy as np
from ultralytics.models import YOLO, RTDETR
from model.calculate_density import Cal_density
from datetime import datetime

# Initialize the environment parameters
area_square = 1  # default unit is square meter

# Initialize model
model = YOLO("../yolov8x.pt")

# Define file path
file_path = 'demo3_output.csv'

# Erase all history data
with open(file_path, 'w') as file:
    pass

# Define column names
column_names = ['Time', 'num_of_staff']

source = 'street.mp4'

# 调用track方法进行追踪
results = model.track(
    source=source,
    stream=True,
    tracker="botsort.yaml",
    save_dir="counting_demo.mp4",
    vid_stride=2,
    save_txt=True,
    conf=0.4,
    iou=0.5,
    device="mps", # Generally, we use "cuda" to accelerate
)

temp = 0  # Store the result of last epoch

# 对每一帧返回的结果进行处理
for r in results:
    boxes = r.boxes  # Boxes object for bbox outputs
    n = 1 

    class_ids = boxes.cls.cpu().numpy().astype(int)
    num = np.sum(class_ids == 0)
    print(num)

    # Calculate density of people (record the data only when density has changed)
    cal_density = Cal_density(num, area_square)
    if (n == 1 and temp != cal_density.method1()):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        df = pd.DataFrame({'Time': [current_time], 'num_of_staff': [cal_density.method1()]})
        # Write header if the file does not exist or is empty
        if os.path.getsize(file_path) == 0:
            df.to_csv(file_path, index=False, mode='a', header=True)
        else:
            df.to_csv(file_path, index=False, mode='a', header=False)
        print(f"Time: {current_time}, num_of_staff: {cal_density.method1()}")
        n = n - 1

    temp = cal_density.method1()