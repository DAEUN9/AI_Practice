"""
txt파일을 읽고 이미지경로로 파일을 열기
이미지를 다른 경로에 저장하기
"""

import os
import cv2
import sys
#from glob import glob
#import natsort
from PIL import Image
path = "C:/Users/multicampus/Desktop/day1/"

sys.stdin = open("Path/test.txt", "r")
for i in range(5):
    a=input().split()[0]
    path1= path+a

    # # IMREAD_UNCAHNGED는 origin속성
    # img = cv2.imread(path1, cv2.IMREAD_UNCHANGED)
    # img= cv2.resize(img, (500, 500))
    # # 이미지 저장
    # cv2.imwrite(path+"result/"+str(i)+'.jpg', img)
    #
    # # 이미지 보이기
    # cv2.imshow('ss',img)
    #
    # # 기다리는 시간
    # # 0은 무한정 기다리기
    # cv2.waitKey(0)


    img = Image.open(path1)
    img = img.resize((500, 500))
    img.save(path+"result/"+str(i)+'PIL.jpg', "JPEG")
    img.show()


"""
image = natsort.natsorted(glob(path+'Image/'+'*.jpg',recursive=True))
for i in image:
    print(i)
"""