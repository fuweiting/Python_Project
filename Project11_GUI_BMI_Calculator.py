from tkinter import *
from tkinter import messagebox
import tkinter.font as tkfont

# print(tkfont.families())    #印出可用字體

window = Tk()
window.title("BMI計算機")
window.geometry("450x450")
# window.maxsize(width = 900, height = 600)
# window.minsize(width = 200, height = 200)
window.resizable(False, False)
window.config(padx=60, pady=100)

def click():
    try:
        h = float(entry1.get())/100
        w = float(entry2.get())
        if h < 0 or w < 0:
            raise ValueError("身高體重不可為負數")
    except:
        messagebox.showerror(title="輸入錯誤", message="亂輸入 不計算")
    else:
        BMI = w / h ** 2
        BMI = round(BMI, 1)
        # label3["text"] ="您的BMI: "+str(BMI)
        label3["text"] = f"您的BMI: {BMI}"

label1 = Label(text="身高", font=("標楷體", 20))
label1.grid(row=0, column=0)

entry1 = Entry(width=15, font=("標楷體", 20))
entry1.grid(row=0, column=1)

label2 = Label(text="公分", font=("標楷體", 20))
label2.grid(row=0, column=2)

label3 = Label(text="體重", font=("標楷體", 20))
label3.grid(row=1, column=0)

entry2 = Entry(width=15, font=("標楷體", 20))
entry2.grid(row=1, column=1)

label3 = Label(text="公斤", font=("標楷體", 20))
label3.grid(row=1, column=2)

label3 = Label(text="您的BMI: ", font=("標楷體", 20))
label3.grid(row=2, column=1)

my_button = Button(text="計算", font=("標楷體", 20), command=click)
my_button.grid(row=3, column=1)




window.mainloop()