import tkinter as tk

total_count_1 = 0
total_count_2 = 0
count_1 = 0
count_2 = 0

def increment_count_1():
    global count_1
    count_1 += 1
    count_label_1.config(text=str(count_1))

def increment_count_2():
    global count_2
    count_2 += 1
    count_label_2.config(text=str(count_2))

# Tkinterウィンドウの作成
root = tk.Tk()
root.title("カウンターアプリ")

# カウント表示用のラベル
count_label_1 = tk.Label(root, text=str(count_1))
count_label_1.pack()

count_label_2 = tk.Label(root, text=str(count_2))
count_label_2.pack()

# カウント増加ボタン
increment_button_1 = tk.Button(root, text="増加", command=increment_count_1)
increment_button_1.pack()

increment_button_2 = tk.Button(root, text="増加", command=increment_count_2)
increment_button_2.pack()


# ウィンドウのメインループ
root.mainloop()