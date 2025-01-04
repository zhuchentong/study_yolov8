使用Yolov8实现实例分割检测
---

# python 环境使用 3.9.x (labelme在3.9.x以上版本会报错)
# 安装 yolo 相关
pip install yolo ultralytics ncnn labelme labelme2yolov8

# 使用 labelme 标注数据
labelme

# 使用labelme2yolov8转换数据
python -m labelme2yolov8 --json_dir . --val_size 0.15 --test_size 0.15

# 更新dateset
# window
sed -i -e "1ipath: %cd:\=/%" ./YOLOv8Dataset/dataset.yaml
# linux
sed -i -e "1ipath: $(pwd)" ./YOLOv8Dataset/dataset.yaml

# 训练模型
yolo segment train data=./YOLOv8Dataset/dataset.yaml model=./models/yolov8s-seg.pt epochs=100 imgsz=640

# 验证模型
yolo segment val data=./YOLOv8Dataset/dataset.yaml model=./runs/segment/train/weights/best.pt

# 导出模型(format可以使用 ncnn | onnx )
yolo export model=./runs/segment/train/weights/best.pt format=ncnn

# 测试模型
python predict.py