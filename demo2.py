from ultralytics.models import YOLO,RTDETR
import numpy as np
# 初始化模型
model = YOLO("yolov8x.pt") 
# model = RTDETR(weights_path) # weights_path为指向训练好的权重文件的路径
 
# 调用track方法进行追踪
results = model.track(
    source="street.mp4", # 待处理视频的地址，如果是webcam实时录制处理，则source=0
    stream=True,  # 对于视频采用流模式处理，防止因为因为堆积而内存溢出
    #show=True,  # 实时推理演示
    tracker="botsort.yaml",  # 默认tracker为botsort
    #save=True, # 选择是否保存处理后的视频
    save_dir="counting_demo.mp4", # 处理视频的保存路径
    vid_stride=2,  # 视频帧数的步长，即隔几帧检测跟踪一次
    save_txt=True,  # 把结果以txt形式保存
    # save_conf=True,  # 保存置信度得分
    # save_crop=True,  # 保存剪裁的图像
    conf=0.4, # 规定阈值，即低于该阈值的检测框会被剔除
    iou=0.5, # 交并比阈值，用于去除同一目标的冗余框
    device="mps", # 用GPU进行推理，如果使用cpu，则为device="cpu" # Here we use macbook, so device is "mps"
)
 
# 对每一帧返回的结果进行处理
for r in results:
    boxes = r.boxes  # Boxes object for bbox outputs

    # The parameters below have no contribution to the specific project

    # masks = r.masks  # Masks object for segment masks outputs
    # probs = r.probs  # Class probabilities for classification outputs
    # 加上自己的结果处理代
    class_ids = boxes.cls.cpu().numpy().astype(int)
    num = np.sum(class_ids == 0)
    print(num)