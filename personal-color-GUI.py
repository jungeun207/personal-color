import tkinter as tk
import PIL.Image
import PIL.ImageTk
import numpy as np
from PIL import Image
from tkinter import filedialog

window=tk.Tk()

window.title("CO;DE 퍼스널컬러 진단 프로그램")
window.geometry("640x400+100+100")
window.resizable(True, True)

#이름 입력
label_name=tk.Label(window, text="이름을 입력해 주세요.", font=("bold", 13))
label_name.place(x=0, y=10)

entry = tk.Entry(window)
entry.place(x=5, y=40, height=35)

#사진 삽입
label_photo=tk.Label(window, text="퍼스널 컬러 진단을 원하는 사진을 입력해 주세요.", pady=20, font=("bold", 13))
label_photo.place(x=5, y=70)

image_path = ""

def photo(fpath):
    global image_path
    image_path = fpath
    newImage=PIL.Image.open(fpath).resize((200, 300))
    imageData=PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image=imageData

def openFile():
    fpath=filedialog.askopenfilename()
    if fpath:
        photo(fpath)

window.geometry("400x350")

btn=tk.Button(text="사진 입력", command=openFile)
imageLabel=tk.Label()
btn.place(x=392, y=88)
imageLabel.place(x=0, y=110)

#퍼스널컬러 판단
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

label_name_print = tk.Label(window)

def analyze_personal_color():
    global image_path
    input_palette = average_color(image_path)
    input_palette = np.array(input_palette)

    spring_palette = np.array([[177.64194697, 157.50059045, 155.04722948]])
    summer_palette = np.array([[129.16025068, 120.73418611, 136.25991809]])
    autumn_palette = np.array([[149.66640364, 127.82089121, 121.45471694]])
    winter_palette = np.array([[101.06281293, 101.29546201, 117.32740631]])

    palettes = [spring_palette, summer_palette, autumn_palette, winter_palette]
    closest_index = find_closest_palette(input_palette, palettes)

    personal_color_tones = ['봄 웜톤', '여름 쿨톤', '가을 웜톤', '겨울 쿨톤']
    closest_tone = personal_color_tones[closest_index]

    label_name_print.config(text= entry.get()+ " 님의 퍼스널 컬러는 " +closest_tone+ "입니다.", font=("bold", 13))
    label_name_print.place(x=600, y=10)
    if closest_tone == '봄 웜톤':
        label_spring=tk.Label(window, text="봄 웜톤", font=("bold", 13))
        label_spring.place(x=600, y=40)
        label_spring_explanation=tk.Label(window, text="화사하면서도 따뜻한 느낌이 감돈다.\n파스텔 톤의 은은한 컬러, 아이보리, 베이지 등이 여성스럽고 맑은 분위기를 만들어줄 수 있다.", justify='left', font=("bold", 13))
        label_spring_explanation.place(x=600, y=60)
        spring_palette_image=PIL.Image.open(r"C:\Users\user\Desktop\personal-color\봄웜_팔레트.png")
        spring_palette_image=PIL.ImageTk.PhotoImage(spring_palette_image)
        spring_palette_label=tk.Label(window, image=spring_palette_image)
        spring_palette_label.image = spring_palette_image
        spring_palette_label.place(x=600, y=100)
        label_spring_celebrity=tk.Label(window, text="대표 연예인", font=("bold", 13))
        label_spring_celebrity.place(x=600, y=240)
        spring_celebrity_image=PIL.Image.open(r"C:\Users\user\Desktop\personal-color\봄웜_연예인.png")
        spring_celebrity_image=PIL.ImageTk.PhotoImage(spring_celebrity_image)
        spring_celebrity_label=tk.Label(window, image=spring_celebrity_image)
        spring_celebrity_label.image = spring_celebrity_image
        spring_celebrity_label.place(x=600, y=260)
        spring_celebrity_label=tk.Label(window, text="아이유                                    NCT 정우", font=("bold", 13))
        spring_celebrity_label.place(x=600, y=530)
        label_spring_cosmetics=tk.Label(window, text="추천 화장품", font=("bold", 13))
        label_spring_cosmetics.place(x=600, y=560)
        spring_cosmetics_image=PIL.Image.open(r"C:\Users\user\Desktop\personal-color\봄웜_화장품.png")
        spring_cosmetics_image=PIL.ImageTk.PhotoImage(spring_cosmetics_image)
        spring_cosmetics_label=tk.Label(window, image=spring_cosmetics_image)
        spring_cosmetics_label.image = spring_cosmetics_image
        spring_cosmetics_label.place(x=600, y=585)
        spring_cosmetics_label=tk.Label(window, text="페리페라 글로이 틴트     롬앤 베러 댄 아이즈           릴리바이레드 치크 블러셔\n12호 웜고리즘                 W02 말린 복숭아꽃            청순빔", justify='left', font=("bold", 13))
        spring_cosmetics_label.place(x=600, y=715)

    elif closest_tone == '여름 쿨톤':
        label_summer=tk.Label(window, text="여름 쿨톤", font=("bold", 13))
        label_summer.place(x=600, y=40)
        label_summer_explanation=tk.Label(window, text="시크하고 깨끗하며 우아한 인상이다. 전반적으로 맑고 청초한 이미지를 가진다.\n새하얀 흰색, 노란기 없는 차가운 색들이 잘어울린다.", justify='left', font=("bold", 13))
        label_summer_explanation.place(x=600, y=60)
        summer_palette_image=PIL.Image.open(r"C:\Users\user\Desktop\personal-color\여쿨_팔레트.png")
        summer_palette_image=PIL.ImageTk.PhotoImage(summer_palette_image)
        summer_palette_label=tk.Label(window, image=summer_palette_image)
        summer_palette_label.image = summer_palette_image
        summer_palette_label.place(x=600, y=110)
        label_summer_celebrity=tk.Label(window, text="대표 연예인", font=("bold", 13))
        label_summer_celebrity.place(x=600, y=250)
        summer_celebrity_image=PIL.Image.open(r"C:\Users\user\Desktop\personal-color\여쿨_연예인.png")
        summer_celebrity_image=PIL.ImageTk.PhotoImage(summer_celebrity_image)
        summer_celebrity_label=tk.Label(window, image=summer_celebrity_image)
        summer_celebrity_label.image = summer_celebrity_image
        summer_celebrity_label.place(x=600, y=280)
        summer_celebrity_label=tk.Label(window, text="레드벨벳 아이린          소녀시대 태연           아이브 장원영", font=("bold", 13))
        summer_celebrity_label.place(x=600, y=490)
        label_summer_cosmetics=tk.Label(window, text="추천 화장품", font=("bold", 13))
        label_summer_cosmetics.place(x=600, y=525)
        summer_cosmetics_image=PIL.Image.open(r"C:\Users\user\Desktop\personal-color\여쿨_화장품.png")
        summer_cosmetics_image=PIL.ImageTk.PhotoImage(summer_cosmetics_image)
        summer_cosmetics_label=tk.Label(window, image=summer_cosmetics_image)
        summer_cosmetics_label.image = summer_cosmetics_image
        summer_cosmetics_label.place(x=600, y=555)
        summer_cosmetics_label=tk.Label(window, text="롬앤 쥬시 래스팅 틴트    크리니크 치크팝     에스쁘아 리얼 아이팔레트\n6호 피그피그                  헤더팝                    4호 모브 미", justify='left', font=("bold", 13))
        summer_cosmetics_label.place(x=600, y=665)

    elif closest_tone == '가을 웜톤':
        label_autumn=tk.Label(window, text="가을 웜톤", font=("bold", 13))
        label_autumn.place(x=600, y=40)
        label_autumn_explanation=tk.Label(window, text="편안하고 네추럴한 인상이며 따뜻한 색조를 가진다.\n브라운, 베이지, 올리브 그린과 같이 부드러운 컬러를 활용하면 자연스럽고 우아한 분위기를 연출할 수 있다.", justify='left', font=("bold", 13))
        label_autumn_explanation.place(x=600, y=60)
        autumn_palette_image=PIL.Image.open(r"C:\Users\user\Desktop\personal-color\갈웜_팔레트.png")
        autumn_palette_image=PIL.ImageTk.PhotoImage(autumn_palette_image)
        autumn_palette_label=tk.Label(window, image=autumn_palette_image)
        autumn_palette_label.image = autumn_palette_image
        autumn_palette_label.place(x=600, y=100)
        label_autumn_celebrity=tk.Label(window, text="대표 연예인", font=("bold", 13))
        label_autumn_celebrity.place(x=600, y=245)
        autumn_celebrity_image=PIL.Image.open(r"C:\Users\user\Desktop\personal-color\갈웜_연예인.png")
        autumn_celebrity_image=PIL.ImageTk.PhotoImage(autumn_celebrity_image)
        autumn_celebrity_label=tk.Label(window, image=autumn_celebrity_image)
        autumn_celebrity_label.image=autumn_celebrity_image
        autumn_celebrity_label.place(x=600, y=270)
        autumn_celebrity_label=tk.Label(window, text="이성경                       신세경                       블랙핑크 제니", font=("bold", 13))
        autumn_celebrity_label.place(x=600, y=490)
        label_autumn_cosmetics=tk.Label(window, text="추천 화장품", font=("bold", 13))
        label_autumn_cosmetics.place(x=600, y=525)
        autumn_cosmetics_image=PIL.Image.open(r"C:\Users\user\Desktop\personal-color\갈웜_화장품.png")
        autumn_cosmetics_image=PIL.ImageTk.PhotoImage(autumn_cosmetics_image)
        autumn_cosmetics_label=tk.Label(window, image=autumn_cosmetics_image)
        autumn_cosmetics_label.image = autumn_cosmetics_image
        autumn_cosmetics_label.place(x=600, y=555)
        autumn_cosmetics_label=tk.Label(window, text="에뛰드 픽싱 틴트        클리오 프로아이 팔레트     페리페라 맑게 물든 선샤인 치크\n16호 베이크드 피칸     8호 라떼는 선임                 16호 도토리 좋아해", justify='left', font=("bold", 13))
        autumn_cosmetics_label.place(x=600, y=695)

    else:
        label_winter=tk.Label(window, text="겨울 쿨톤", font=("bold", 13))
        label_winter.place(x=600, y=40)
        label_winter_explanation=tk.Label(window, text="비치는 듯 창백한 피부톤이며 전반적으로 시크하고 화려한 이미지이다.\n컬러감이 확실하고 뚜렷한 비비드 색상이 잘 어울린다.", justify='left', font=("bold", 13))
        label_winter_explanation.place(x=600, y=60)
        winter_palette_image=PIL.Image.open(r"C:\Users\user\Desktop\personal-color\겨쿨_팔레트.png")
        winter_palette_image=PIL.ImageTk.PhotoImage(winter_palette_image)
        winter_palette_label=tk.Label(window, image=winter_palette_image)
        winter_palette_label.image = winter_palette_image
        winter_palette_label.place(x=600, y=110)
        label_winter_celebrity=tk.Label(window, text="대표 연예인", font=("bold", 13))
        label_winter_celebrity.place(x=600, y=250)
        winter_celebrity_image=PIL.Image.open(r"C:\Users\user\Desktop\personal-color\겨쿨_연예인.png")
        winter_celebrity_image=PIL.ImageTk.PhotoImage(winter_celebrity_image)            
        winter_celebrity_label=tk.Label(window, image=winter_celebrity_image)
        winter_celebrity_label.image = winter_celebrity_image
        winter_celebrity_label.place(x=600, y=280)
        winter_celebrity_label=tk.Label(window, text="임지연                        에스파 카리나           선미", font=("bold", 13))
        winter_celebrity_label.place(x=600, y=500)            
        label_winter_cosmetics=tk.Label(window, text="추천 화장품", font=("bold", 13))
        label_winter_cosmetics.place(x=600, y=535)
        winter_cosmetics_image=PIL.Image.open(r"C:\Users\user\Desktop\personal-color\겨쿨_화장품.png")
        winter_cosmetics_image=PIL.ImageTk.PhotoImage(winter_cosmetics_image)
        winter_cosmetics_label=tk.Label(window, image=winter_cosmetics_image)
        winter_cosmetics_label.image=winter_cosmetics_image
        winter_cosmetics_label.place(x=600, y=565)
        winter_cosmetics_label=tk.Label(window, text="롬앤 블러 퍼지 틴트           데이지크 블렌딩 무드 치크    웨이크메이크 아이팔레트\n7호 쿨로즈업                      5호 바이올렛 니트                 9호 하이핑크 블러링", justify='left', font=("bold", 13))
        winter_cosmetics_label.place(x=600, y=705)

#진단 시작 버튼
start_button = tk.Button(window, text="진단하기", overrelief="solid", width=15, height=2, repeatdelay=100, repeatinterval=100, padx=20, command=analyze_personal_color)
start_button.place(x=10, y=450)

'''#처음으로 버튼
start_button = tk.Button(window, text="처음으로", overrelief="solid", width=15, height=2, repeatdelay=100, repeatinterval=100, padx=20)
start_button.place(x=200, y=450)'''

window.mainloop()