import numpy as np

#팔레트 리스트
spring_palette_list = []
summer_palette_list =  []   
autumn_palette_list = []
winter_palette_list = []

spring_palette = np.array([np.array(color) for color in spring_palette_list])
summer_palette = np.array([np.array(color) for color in summer_palette_list])
autumn_palette = np.array([np.array(color) for color in autumn_palette_list])
winter_palette = np.array([np.array(color) for color in winter_palette_list])

spring_palette_average = np.mean(spring_palette, axis=0)
summer_palette_average = np.mean(summer_palette, axis=0)
autumn_palette_average = np.mean(autumn_palette, axis=0)
winter_palette_average = np.mean(winter_palette, axis=0)

#(3, 3) 형태의 배열로 변환
spring_palette_array = np.array([spring_palette_average])
summer_palette_array = np.array([summer_palette_average])
autumn_palette_array = np.array([autumn_palette_average])
winter_palette_array = np.array([winter_palette_average])

print("배열:")
print(spring_palette_array)
print(summer_palette_array)
print(autumn_palette_array)
print(winter_palette_array)
