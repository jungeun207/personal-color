import numpy as np
from PIL import Image

def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

def find_closest_palette(input_palette, palettes):
    closest_distance = float('inf')
    closest_index = None
    for i, palette in enumerate(palettes):
        distance = euclidean_distance(input_palette, palette)
        if distance < closest_distance:
            closest_distance = distance
            closest_index = i
    return closest_index

def average_color(image):
    img = Image.open(image).convert('RGB')
    img_array = np.array(img)
    average_color = np.mean(img_array, axis=(0, 1))
    return tuple(average_color)

image_path = r"이미지 경로"

input_palette = average_color(image_path)
palette=np.array(input_palette)

input_palette = np.array(palette)

spring_palette = np.array([[177.64194697, 157.50059045, 155.04722948]])
summer_palette = np.array([[129.16025068, 120.73418611, 136.25991809]])
autumn_palette = np.array([[149.66640364, 127.82089121, 121.45471694]])
winter_palette = np.array([[101.06281293, 101.29546201, 117.32740631]])

palettes = [spring_palette, summer_palette, autumn_palette, winter_palette]
closest_index = find_closest_palette(input_palette, palettes)

personal_color_tones = ['봄웜톤', '여름쿨톤', '가을웜톤', '겨울쿨톤']
closest_tone = personal_color_tones[closest_index]
print("입력하신 이미지의 퍼스널컬러는", closest_tone, "입니다.")