from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
from PIL import ImageFilter

# 이미지 로드
img = Image.open("001.jpg")

# 이미지 회전
img_rotated = img.rotate(90)

# 이미지 밝기 조정
enhancer = ImageEnhance.Brightness(img)
img_brightened = enhancer.enhance(2.0)

# 이미지 흑백
img_gray = img.convert("L")

# 이미지 블러
img_blur = img.filter(ImageFilter.GaussianBlur(10))

# 결과 확인
fig, ax = plt.subplots(1, 5, figsize=(10, 5))

ax[0].imshow(img)
ax[0].axis('off')
ax[0].set_title("ORG_IMAGE")

ax[1].imshow(img_rotated)
ax[1].axis('off')
ax[1].set_title("ROTATED_IMAGE")

ax[2].imshow(img_brightened)
ax[2].axis('off')
ax[2].set_title("BRIGHT")

ax[3].imshow(img_gray)
ax[3].axis('off')
ax[3].set_title("GRAY")

ax[4].imshow(img_blur)
ax[4].axis('off')
ax[4].set_title("BLUR")

img_blur.save("./results.png")

plt.show()



# # 이미지 2개 더 튜닝하여 시각화
# # 이미지 로드
# img = Image.open("벚꽃.jpg")

# # 이미지 회전
# img_rotated = img.rotate(90)

# # 이미지 밝기 조정
# enhancer = ImageEnhance.Brightness(img)
# img_brightened = enhancer.enhance(2.0)

# # 이미지 흑백
# img_gray = img.convert("1")

# # 결과 확인
# fig, ax = plt.subplots(1, 4, figsize=(10, 5))

# ax[0].imshow(img)
# ax[0].axis('off')
# ax[0].set_title("ORG_IMAGE")

# ax[1].imshow(img_rotated)
# ax[1].axis('off')
# ax[1].set_title("ROTATED_IMAGE")

# ax[2].imshow(img_brightened)
# ax[2].axis('off')
# ax[2].set_title("BRIGHT")

# ax[3].imshow(img_gray)
# ax[3].axis('off')
# ax[3].set_title("GRAY")

# plt.show()


# # 이미지 로드
# img1 = Image.open("벚꽃2.jpg")

# # 이미지 회전
# img1_rotated = img1.rotate(90)

# # 이미지 밝기 조정
# enhancer = ImageEnhance.Brightness(img1)
# img1_brightened = enhancer.enhance(2.0)

# # 이미지 흑백
# img1_gray = img1.convert("1")

# # 결과 확인
# fig1, ax1 = plt.subplots(1, 4, figsize=(10, 5))

# ax1[0].imshow(img1)
# ax1[0].axis('off')
# ax1[0].set_title("ORG_IMAGE")

# ax1[1].imshow(img1_rotated)
# ax1[1].axis('off')
# ax1[1].set_title("ROTATED_IMAGE")

# ax1[2].imshow(img1_brightened)
# ax1[2].axis('off')
# ax1[2].set_title("BRIGHT")

# ax1[3].imshow(img1_gray)
# ax1[3].axis('off')
# ax1[3].set_title("GRAY")

# plt.show()