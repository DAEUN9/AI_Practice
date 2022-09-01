# day2
1.  image에 Bluer(kernel 3), (kernel 5), (kernel 7)을 적용해서 결과를 본다

   

2. image를 numpy를 이용하여 500*500(250000)로 바꾼다



3. numpy를 다시 이미지로 바꾼다



4. 바꾼 이미지에 Blur kernel을 만들고 cv2.filter에 적용한다



5. 이미지와 kernel의 관계를 이해하고 convolution을 이해한다

---

- cv2
  - y, x 순서
  - BGR 순서
- kernel
  - kernel은 kernel의 중앙이 이미지의 0,0부터 시작하여 가로로 이동
  - kernel은 1,1시작
- image를 numpy로 바꿀때
  - (500, 500, 3) -> (250000, 3) 으로 변경가능
  - 차원의 곱의 수가 맞아야 변환가능
