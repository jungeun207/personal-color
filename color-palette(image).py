from colorthief import ColorThief
import matplotlib.pyplot as plt

ct=ColorThief(r"C:\Users\user\Desktop\sample.태용.jpg")
dominant_color=(ct.get_color(quality=1))

plt.imshow([[dominant_color]])
plt.show()

palette=ct.get_palette(color_count=5)
plt.imshow([[palette[i] for i in range(5)]])
plt.show()