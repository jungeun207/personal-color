import numpy as np
from PIL import Image

name=str(input("이름을 입력해 주세요.: "))

def euclidean_distance(p1, p2):
    """
    두 점 사이의 유클리디안 거리를 계산하는 함수
    """
    return np.sqrt(np.sum((p1 - p2) ** 2))

def find_closest_palette(input_palette, palettes):
    """
    입력된 팔레트와 주어진 팔레트들 간의 거리를 계산하여 가장 가까운 팔레트를 찾는 함수
    """
    closest_distance = float('inf')
    closest_index = None
    for i, palette in enumerate(palettes):
        distance = euclidean_distance(input_palette, palette)
        if distance < closest_distance:
            closest_distance = distance
            closest_index = i
    return closest_index

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

# 사용자가 입력한 이미지 파일 경로
image_path = r"파일 경로"

# 이미지의 평균 색상 계산
input_palette = average_color(image_path)

#계산한 평균 색상을 np 배열로 변형
palette=np.array(input_palette)

# 봄웜톤, 여름쿨톤, 가을웜톤, 겨울쿨톤 팔레트
spring_palette = np.array([[]])
summer_palette = np.array([[]])
autumn_palette = np.array([[]])
winter_palette = np.array([[]])

# 팔레트들 간의 거리를 계산하여 가장 가까운 퍼스널 컬러 톤을 찾음
palettes = [spring_palette, summer_palette, autumn_palette, winter_palette]
closest_index = find_closest_palette(input_palette, palettes)

# 가장 가까운 퍼스널 컬러 톤 출력
personal_color_tones = ['봄웜톤', '여름쿨톤', '가을웜톤', '겨울쿨톤']
closest_tone = personal_color_tones[closest_index]
print(name, " 님의 퍼스널컬러는", closest_tone, "입니다.")
