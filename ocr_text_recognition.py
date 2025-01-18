from paddleocr import PaddleOCR
import time
#用finetune過的模型請註解第14行
#用pretrain model 請註解6到13行
rec_model_dir = './inference/_cht_PP-OCRv3_rec/'
# 初始化 PaddleOCR
ocr = PaddleOCR(
    use_angle_cls=False, 
    lang='chinese_cht',
    use_gpu=True,  # 如果使用 GPU，请设置为 True
    rec_model_dir=rec_model_dir  # 加载自定义识别模型
)
# ocr = PaddleOCR(use_angle_cls=False, lang='chinese_cht',use_gpu=0) # need to run only once to load model into memory
# img_path = "/home/kevin/TinyLLaVA_Factory/data/image/image_1.jpg"
img_path = '/nfs/RS2416RP/Workspace/spec/TPTS/picture/大港的台灣/lcw8BJhhK7M_230066_232432.jpg'
# img_path ="/home/kevin/TinyLLaVA_Factory/frame_5.jpg" 
# img_path = '/home/kevin/PaddleOCR/show_img.jpg'
s=time.time()
result = ocr.ocr(img_path, cls=False)
print(time.time()-s)
for idx in range(len(result)):
    if result[0] ==None:
        break
    res = result[idx]
    for line in res:
        print(line)
    # print(res[1][-1][0])



# from cnocr import CnOcr

# img_fp = '/home/kevin/TinyLLaVA_Factory/data/image/image_1.jpg'
# # img_fp = '/nfs/RS2416RP/Workspace/spec/TPTS/picture/大港的台灣/lcw8BJhhK7M_230066_232432.jpg'
# img_fp = "/home/kevin/TinyLLaVA_Factory/frame_5.jpg" 
# img_fp = '/home/kevin/PaddleOCR/show_img.jpg'
# n=time.time()
# ocr = CnOcr(rec_model_name='chinese_cht_PP-OCRv3')  # 识别模型使用繁体识别模型
# out = ocr.ocr(img_fp, cls=True)
# print(time.time()-n)
# print(out)