import cv2
import numpy as np
from PIL import Image
img = cv2.imread('image/test1.jpg')

kernel = np.array([[1,1,1],[1,1,1],[1,1,1]])*(1/9)
img = cv2.filter2D(img,-1,kernel)
cv2.imshow('ss',img)
cv2.waitKey(0)


# img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img = cv2.resize(img,(500,500))
# img = np.array(img)
# nn= img.reshape(250000,3)
# nn = nn.reshape(500,500,3)
# new_img=Image.fromarray(nn)
#
# new_img.show()

# img=cv2.medianBlur(img,3)
# cv2.imshow("ss",img)
# cv2.waitKey(0)
"""
blured3 = cv2.filter2D(img, -1, (3, 3))
blured5 = cv2.filter2D(img, -1, (5, 5))
blured7 = cv2.filter2D(img, -1, (7, 7))
blurs = [blured3, blured5, blured7]

# 결과 출력
# cv2.imshow('origin', img)
# cv2.imshow('blur3', blured3)
# cv2.imshow('blur5', blured5)
# cv2.imshow('blur7', blured7)
# cv2.waitKey()
# cv2.destroyAllWindows()

for blur in blurs:
    pix = np.array(blur)
    cv2.imshow('aa', pix)
    cv2.waitKey()
    print(pix)
"""