import matplotlib.pyplot as plt
from PIL import Image

# 讀取影像
image = Image.open('/nfs/RS2416RP/Workspace/spec/TPTS/picture/青春咱的夢/LIeyKtCw5Ok_72765_73632.jpg')


# 顯示影像
# plt.imshow(image)
# plt.axis('off')  # 關閉座標軸
# plt.show()
# 保存影像
image.save('show_img.jpg')