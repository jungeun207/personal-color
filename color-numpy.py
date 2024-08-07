import numpy as np

# 팔레트 리스트
spring_palette_list = [(190.39060283687942, 166.61165455803493, 169.62583895519805), (167.5241682145979, 152.57613090034965, 146.90048281796328), (179.03143846325665, 148.01555357009903, 150.88538083538083), (202.9664106011139, 188.50107547532167, 182.4546235836374), (148.2971147367327, 131.79853775782829, 125.36982122564187)]
summer_palette_list =  [(144.32772319566124, 135.18881935753024, 139.60779098873593), (148.3964345637584, 127.00842344021875, 128.22271159582402), (78.21175405268491, 83.02201367781154, 98.44871580547112), (163.63588556435099, 142.43631237200694, 156.2307887326717), (111.22945601851852, 116.01536168981481, 158.78958333333333)]   
autumn_palette_list = [(162.40162946428572, 134.0763125, 127.12775669642858), (138.4193908898305, 120.37547669491525, 117.98309322033899), (180.9616418490067, 
149.85842708219562, 138.3554325797017), (135.58184637912674, 126.32257587859425, 121.04095181043664), (130.9675096259626, 108.47166391639163, 102.7663503850385)]
winter_palette_list = [(120.58633041381836, 110.5904312133789, 115.17099380493164), (76.93739491382934, 90.22859963920415, 122.24406700994815), (108.221759375, 116.5879328125, 134.72486875), (110.38320848794064, 109.99452922077923, 114.56258928571428), (89.18537144296147, 79.07581717451524, 99.9345127171997)]

spring_palette = np.array([np.array(color) for color in spring_palette_list])
summer_palette = np.array([np.array(color) for color in summer_palette_list])
autumn_palette = np.array([np.array(color) for color in autumn_palette_list])
winter_palette = np.array([np.array(color) for color in winter_palette_list])

spring_palette_average = np.mean(spring_palette, axis=0)
summer_palette_average = np.mean(summer_palette, axis=0)
autumn_palette_average = np.mean(autumn_palette, axis=0)
winter_palette_average = np.mean(winter_palette, axis=0)

# (3, 3) 형태의 배열로 변환
spring_palette_array = np.array([spring_palette_average])
summer_palette_array = np.array([summer_palette_average])
autumn_palette_array = np.array([autumn_palette_average])
winter_palette_array = np.array([winter_palette_average])

print("배열:")
print(spring_palette_array)
print(summer_palette_array)
print(autumn_palette_array)
print(winter_palette_array)