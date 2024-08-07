import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

window=tk.Tk()

window.title("sample")
window.geometry("640x400+100+100")
window.resizable(True, True)


#이름 입력
label_name=tk.Label(window, text="이름을 입력해 주세요.", font=("bold", 13))
label_name.place(x=0, y=10)
entry = tk.Entry(window)
entry.place(x=5, y=40, height=35)


#사진 삽입
label_photo=tk.Label(window, text="사진을 입력해 주세요.", pady=20, font=("bold", 13))
label_photo.place(x=5, y=70)
image_path = ""

def photo(fpath):
    global image_path
    image_path=fpath
    newImage=Image.open(fpath).resize((200, 300))
    imageData=ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData

def openFile():
    fpath=filedialog.askopenfilename()
    if fpath:
        photo(fpath)
window.geometry("400x350")

btn=tk.Button(text="사진 입력", command=openFile)
imageLabel=tk.Label()
btn.place(x=190, y=88)
imageLabel.place(x=0, y=120)

label_name_print = tk.Label(window)

def show_photo():
    label_name_print.config(text= entry.get()+ " 님이 입력하신 사진입니다.", font=("bold", 13))
    label_name_print.place(x=600, y=10)

    if image_path:
        newImage = Image.open(image_path).resize((200, 300))
        imageData = ImageTk.PhotoImage(newImage)
        copied_image_label = tk.Label(window, image=imageData)
        copied_image_label.image = imageData
        copied_image_label.place(x=600, y=120)

#진단 시작 버튼
start_button = tk.Button(window, text="출력하기", overrelief="solid", width=15, height=2, repeatdelay=100, repeatinterval=100,
                         padx=20,command=show_photo)
start_button.place(x=10, y=450)

window.mainloop()