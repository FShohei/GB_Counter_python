import tkinter as tk

def increment_count():
    global count
    count += 1
    count_label.config(text=str(count))

count = 0

# Tkinterウィンドウの作成
root = tk.Tk()
root.title("カウンターアプリ")

# カウント表示用のラベル
count_label = tk.Label(root, text=str(count))
count_label.pack()

# カウント増加ボタン
increment_button = tk.Button(root, text="増加", command=increment_count)
increment_button.pack()

# ウィンドウのメインループ
root.mainloop()