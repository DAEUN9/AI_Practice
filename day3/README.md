# day3
1.  torch.hub에서 버전에 맞는 resnet모델 불러오기

   

2. img의 Tensor변환



3. torchvision에서 preprosessing하기



4. permute 사용해서 tensor의 axis변환



5. unsqueeze를 통해 resnet을 통과하여 feature 만들기



6. img1과 img2의 feature를 stack을 통해 합치기



8. feature 변환을 통해 feature의 이해



---

- cv2에서 차원
  - (세로, 가로, channel)
- tensor에서 차원
  - (batchsize, channel, 가로, 세로)

- polling : 줄이기
- downsampling : 늘리기
- FC : Full Connected Layer
- feature의 합
  - 붙여줌
- feature의 곱
  - 섞어줌
