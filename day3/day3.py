import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import torch
from torchvision import transforms
# resner모델 불러오기
model = torch.hub.load('pytorch/vision:v0.8.2', 'resnet50', pretrained=True)

path = 'C:/Users/AI_Practice/day3/Image/'
img1 = 'test1.jpg'
img2 = 'test2.jpg'

#img1 = cv2.imread(path+img1)
#img2 = cv2.imread(path+img2)

# tensor로 변환할때 이미지는 TIL 사용
img1  = Image.open(path+img1)
img2 = Image.open(path+img2)


preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    # 정규화 0~1
    # Relu함수를 거친부분 정규화해줌
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

img1_p = preprocess(img1)
img2_p = preprocess(img2)

# dim=int는 위치
# 4자리수로 맞춰주기위해 의미없는 1을 추가해줌
# (batchsize, channel, 가로, 세로)
img1_p = torch.unsqueeze(img1_p,dim=0)
img2_p = torch.unsqueeze(img2_p,dim=0)

print(img1_p.shape)

# 차원 순서바꾸기
img1_pp = img1_p.permute(2,1,0,3)
print(img1_pp.shape)
# print(img1_p.shape)

# 경사를 변경하지 않음(그냥 돌릴때)
with torch.no_grad():
    output1 = model(img1_p)
    output2 = model(img2_p)

    # feature합치기
    result=torch.stack([output1, output2], dim=1)
    print(result.shape)


#print(img1.shape)
#img1 = torch.Tensor(img1)

# 그냥 이미지는 list
# numpy는 plt로 읽을수가 있다.
# tensor는 읽을수가 없다.

#print(img1.shape)
