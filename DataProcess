import os.path
import glob  #引入文件路径查找模块
import cv2   #引入opencv2
import copy

# def convertjpg(jpgfile, outdir):
#     src = cv2.imread(jpgfile, cv2.IMREAD_GRAYSCALE) #imread方法生成灰度图片
#     binary_src = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,25,25)
#     #hline = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2), (-1, -1))  # 定义结构元素，卷积核
#     # 提取垂直线    src.shape[0]得到src行数
#     #vline = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2), (-1, -1))
#     gradX = cv2.Sobel(binary_src, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
#     gradY = cv2.Sobel(binary_src, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)
#     #img_gradient = cv2.subtract(gradX, gradY)
#     #img_gradient = cv2.convertScaleAbs(img_gradient)
#     #blurred = cv2.blur(binary_src, (9, 9))
#     #(_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)
#     print(os.path.join(outdir, os.path.basename(jpgfile)))#查看保存路径
#     try:
#         # dst = cv2.morphologyEx(binary_src, cv2.MORPH_OPEN, hline)  # 水平方向
#         # dst = cv2.morphologyEx(dst, cv2.MORPH_OPEN, vline)
#         dst = cv2.resize(binary_src, (196, 64), interpolation=cv2.INTER_CUBIC)  # resize方法缩放图片
#         cv2.imwrite(os.path.join(outdir, os.path.basename(jpgfile)), dst)  # imwrite方法保存图片，os.path.join能拼接路径
#     except Exception as e:
#         print(e)


def del_noise(jpgfile,outdir, number):
    # number：周围像素数为黑色的小于number个，就算为噪声，并将其去掉，如number=6，就是一个像素周围9个点（包括本身）中小于6个的就将这个像素归为噪声
    img=cv2.imread(jpgfile,cv2.IMREAD_GRAYSCALE)#读取灰度图
    binary = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 20)#二值化
    height = binary.shape[0]
    width = binary.shape[1]
    img_new = copy.deepcopy(binary)
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            point = [[], [], []]
            count = 0
            point[0].append(binary[i - 1][j - 1])
            point[0].append(binary[i - 1][j])
            point[0].append(binary[i - 1][j + 1])
            point[1].append(binary[i][j - 1])
            point[1].append(binary[i][j])
            point[1].append(binary[i][j + 1])
            point[2].append(binary[i + 1][j - 1])
            point[2].append(binary[i + 1][j])
            point[2].append(binary[i + 1][j + 1])
            for k in range(3):
                for z in range(3):
                    if point[k][z] == 0:
                        count += 1
            if count <= number:
                img_new[i, j] = 255
    cv2.imwrite(os.path.join(outdir, os.path.basename(jpgfile)), img_new)

for jpgfile in glob.glob(r'C:\Users\86155\Pictures\Camera Roll\*.jpg'):
    del_noise(jpgfile,r'C:\Users\86155\Pictures\pic',6)
