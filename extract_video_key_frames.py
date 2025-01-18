import cv2
from PIL import Image, ImageFile
import numpy as np
def extract_frames(video_path, output_dir):
    # 開啟影片
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"無法打開影片: {video_path}")
        return

    # 獲取影片的總幀數
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"影片總幀數: {total_frames}")
    
    # 計算頭、中間、尾的幀索引
    indices = [1, total_frames // 2, total_frames - 2]

    for idx, frame_no in enumerate(indices):
        # 設置幀位置
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
        
        # 讀取指定幀
        ret, frame = cap.read()
        if not ret:
            print(f"無法讀取幀: {frame_no}")
            continue
        
        # 儲存幀為圖片
        output_path = f"{output_dir}/frame_{idx+1}.jpg"
        cv2.imwrite(output_path, frame)
        print(f"儲存幀至: {output_path}")

    cap.release()

# 使用範例
video_path = "/nfs/RS2416RP/Workspace/spec/all_cropped_video/青春咱的夢cropped/LIeyKtCw5Ok_dir/LIeyKtCw5Ok_33_2266.mp4"  # 影片檔案路徑
output_dir = "./data"    # 輸出目錄
extract_frames(video_path, output_dir)
image=Image.open('data/frame_1.jpg').convert('RGB')
print(image.size)