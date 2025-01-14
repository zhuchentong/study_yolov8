from ultralytics import YOLO
from PIL import Image

# 加载模型
model = YOLO("./test/model.pt")

# 使用模型进行预测
results = model.predict(source="./test/image.png")

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