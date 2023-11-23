import tkinter as tk
import csv

"""
count_1 = 青箱
count_2 = ヒヒイロカネ
"""
total_count_1 = 0
total_count_2 = 0
count_1 = 0
count_2 = 0

with open('temp.csv', mode = 'r', encoding = 'utf-8') as input_file:

    init_datas = csv.reader(input_file)
    next(init_datas)

    init_data = next(init_datas, None)
    total_count_1 = int(init_data[1])
    total_count_2 = int(init_data[2])


def increment_count_1():
    global count_1
    count_1 += 1
    count_label_1.config(text = "青箱: " + str(count_1))

    global total_count_1
    total_count_1 += 1
    total_count_label_1.config(text = "総青箱: " + str(total_count_1))

def increment_count_2():
    global count_2
    count_2 += 1
    count_label_2.config(text = "ヒヒ: " + str(count_2))

    global total_count_2
    total_count_2 += 1
    total_count_label_2.config(text = "総青箱: " + str(total_count_2))

def window_close():
    total_ratio = count_2 / count_1 

    with open('data.csv', mode = 'a', encoding = 'utf-8') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(["date", total_count_1, total_count_2, total_ratio, count_1, count_2])

    with open('temp.csv', mode = 'w', encoding = 'utf-8') as temp_file:
        writer = csv.writer(temp_file)
        writer.writerow(["date", total_count_1, total_count_2, total_ratio, count_1, count_2])

    root.destroy()

# Tkinterウィンドウの作成
root = tk.Tk()
root.title("アーカーシャ カウント")

# Count 1
frame_1 = tk.Frame(root)
frame_1.pack()

# カウント表示用のラベル
count_label_1 = tk.Label(frame_1, text = "青箱: " + str(count_1))
count_label_1.pack(side = tk.LEFT)

# カウント増加ボタン
increment_button_1 = tk.Button(frame_1, text="増加", command=increment_count_1)
increment_button_1.pack(side = tk.LEFT)


# Count 2
frame_2 = tk.Frame(root)
frame_2.pack()

count_label_2 = tk.Label(frame_2, text = "ヒヒ: " + str(count_2))
count_label_2.pack(side = tk.LEFT)

increment_button_2 = tk.Button(frame_2, text="増加", command=increment_count_2)
increment_button_2.pack(side = tk.LEFT)


# Total Count 1
frame_total_1 = tk.Frame(root)
frame_total_1.pack()

# カウント表示用のラベル
total_count_label_1 = tk.Label(frame_total_1, text = "総青箱: " + str(total_count_1))
total_count_label_1.pack(side = tk.LEFT)


# Total Count 2
frame_total_2 = tk.Frame(root)
frame_total_2.pack()

total_count_label_2 = tk.Label(frame_total_2, text = "総ヒヒ: " + str(total_count_2))
total_count_label_2.pack(side = tk.LEFT)


# ウィンドウのメインループ
root.protocol("WM_DELETE_WINDOW", window_close)
root.mainloop()