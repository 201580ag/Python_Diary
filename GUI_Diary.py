import datetime
import tkinter as tk
from tkinter import messagebox

def save_diary(title, content):
    now = datetime.datetime.now()
    filename = now.strftime("%Y-%m-%d") + "-" + title + ".txt"

    with open(filename, 'w') as file:
        file.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        file.write("제목: " + title + "\n")
        file.write("내용: " + content)

    messagebox.showinfo("일기 저장", "일기가 저장되었습니다.")

def create_diary():
    def save_button_click():
        save_diary(title_entry.get(), content_text.get("1.0", tk.END))
        root.destroy()

    root = tk.Tk()
    root.title("일기장")
    root.geometry("500x400")
    root.configure(background="white")  # 배경색 설정

    # 아이콘 설정
    root.iconbitmap("diary.ico")  # 아이콘 파일 경로

    # 프레임 생성
    frame = tk.Frame(root, bg="white")
    frame.pack(pady=10)

    title_label = tk.Label(frame, text="제목:", bg="white")
    title_label.grid(row=0, column=0, sticky="w")

    title_entry = tk.Entry(frame, width=50)
    title_entry.grid(row=0, column=1, padx=5)

    content_label = tk.Label(frame, text="내용:", bg="white")
    content_label.grid(row=1, column=0, sticky="nw")

    content_text = tk.Text(frame, height=15, width=50)
    content_text.grid(row=1, column=1, padx=5)

    save_button = tk.Button(root, text="저장", command=save_button_click, width=50)
    save_button.pack(pady=20)  # 버튼과 위젯 사이의 공백 조절

    root.mainloop()

create_diary()
