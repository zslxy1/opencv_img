# 抽帧图片目标检测
用 YOLOv8 模型，20 行内代码就能实现抽帧图片的目标检测，直接输出结果。

## 使用步骤
1. 安装依赖：`pip install ultralytics opencv-python`  
2. 把代码里的 `yolov8n.pt` 换成你的 `cs16.pt`（若用自定义模型）  
3. 确保 `img_dir = 'dataset_cs1.6'` 和你抽帧文件夹名一致  
4. 运行代码，按 `q` 切换图片，按 `ESC` 退出  
