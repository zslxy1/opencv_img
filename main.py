'''
#视频抽帧
import cv2
cap = cv2.VideoCapture('video.mp4')
num = 1
while cap.isOpened():
    ret,frame=cap.read()
    if ret:
        cv2.imwrite(f'data_{num}.jpg',frame)
        num += 1
    else:
        cap.release()
        break
'''

import cv2
import os

# 创建保存目录
save_dir = 'dataset_cs1.6'
os.makedirs(save_dir, exist_ok=True)  # 自动创建文件夹，若已存在则忽略

cap = cv2.VideoCapture('video_cs1.6.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
frame_interval = int(fps/2)         #每秒截取的照片数量
frame_count = 0
num = 1
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    if frame_count % frame_interval == 0:
        # 指定保存路径为dataset文件夹
        save_path = os.path.join(save_dir, f'data_{num}.jpg')
        cv2.imwrite(save_path, frame)
        num += 1
cap.release()
