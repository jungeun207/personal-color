from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt

def average_color(image):
    """
    이미지의 평균 색상을 계산하는 함수
    """
    # 이미지를 열어서 RGB 모드로 변환
    img = Image.open(image).convert('RGB')
    # 이미지를 numpy 배열로 변환
    img_array = np.array(img)
    # 각 색상 채널의 평균값 계산
    average_color = np.mean(img_array, axis=(0, 1))
    return tuple(average_color)

def extract_palette(image_folder):
    """
    이미지 폴더에서 평균 색상 팔레트와 해당 색상들을 추출하는 함수
    """
    # 이미지 폴더 내의 모든 이미지 파일에 대해 반복
    palette = []
    for filename in os.listdir(image_folder):
        # 파일 경로 생성
        file_path = os.path.join(image_folder, filename)
        # 이미지 파일인 경우에만 처리
        if os.path.isfile(file_path) and any(file_path.endswith(ext) for ext in ['.jpg', '.png', '.jpeg']):
            # 이미지의 평균 색상 계산
            avg_color = average_color(file_path)
            palette.append(avg_color)
    return palette

# 이미지가 저장된 폴더 경로
image_folder = r"C:\Users\user\Desktop\sample.태용.jpg"

# 이미지 폴더에서 평균 색상 팔레트와 해당 색상들을 추출
palette = extract_palette(image_folder)

# 추출된 평균 색상 팔레트 시각화
fig, ax = plt.subplots(1, len(palette), figsize=(len(palette)*2, 2))
for i, color in enumerate(palette):
    ax[i].imshow([[np.array(color)/255]])
    ax[i].axis('off')
    ax[i].set_title(f'Color {i+1}')

plt.show()