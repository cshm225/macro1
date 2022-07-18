from distutils.errors import LibError
import tkinter as tk
import blue as blue_main


LIST_SIZE = 4  # チェックボックスの数
chk_name = ["cafe", "hard", "battle", "shop"]  # チェックボックスの名前
cval = [None]*LIST_SIZE  # onかoffか
cbtn = [None]*LIST_SIZE  # チェックボタン初期化
def main():

    def btn_click():
        for i in range(LIST_SIZE):
            if cval[i].get() == True:
                if i == 0:
                    blue_main.cafe()
                elif i == 1:
                    blue_main.hard()
                elif i == 2:
                    blue_main.battle()
                elif i == 3:
                    blue_main.shop()
    root = tk.Tk()
    root.geometry("200x300")
    button = tk.Button(text="実行", font=(
            "Times New Roman", 15), command=btn_click)
    button.place(x=80, y=250)
    for i in range(LIST_SIZE):
        cval[i] = tk.BooleanVar()
        cval[i].set(False)
        cbtn[i] = tk.Checkbutton(text=chk_name[i], font=(
                "Times New Roman", 12), variable=cval[i])
        cbtn[i].place(x=80, y=30+40*i)
    root.mainloop()
if __name__ == "__main__":
    main()