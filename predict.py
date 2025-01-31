from ultralytics import YOLO
from PIL import Image

# 加载模型
model = YOLO("./runs/segment/train/weights/best.pt")

# 使用模型进行预测
results = model.predict(source="./data/images/0ad3fd10-8e9b-47d7-b7f5-ffdaaae159a6.png")

# 遍历预测结果
for result in results:
    boxes = result.boxes
    masks = result.masks
    keypoints = result.keypoints
    probs = result.probs
    print(result)
    # 可视化结果
    im_array = result.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show() 