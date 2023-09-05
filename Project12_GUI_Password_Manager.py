import json
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


# def get_acc_dic():                              #讀取password.json中的str
#     with open("password.json", "r") as f:
#         password_str = f.read()
#         if password_str == "":
#             return {}
#         else:
#             return json.loads(password_str)     #將str轉換為dic
#
# def add_acc(name, acc, pw):
#     acc_dic = get_acc_dic()
#     acc_dic[name] = {               #將帳號資料新增到讀取出的dic
#         "account": acc,
#         "password": pw
#     }
#     with open("password.json", "w") as f:
#         f.write(json.dumps(acc_dic))            #將更新過的dic轉換為str並覆寫至password.json
#
#
#
# print("歡迎使用密碼產生器")
#
# while True:
#     mode = input("請問要使用什麼功能? (r a q)")
#
#     if mode == "q":
#         break
#
#     elif mode == "a":
#         name = input("請輸入帳號名稱")
#         acc = input("請輸入帳號")
#         pw = input("請輸入密碼")
#         if (name in get_acc_dic()) == True:
#             print("已有帳號名稱")
#         else:
#             add_acc(name, acc, pw)           #將帳號資料新增到acc_dic
#             print("新增成功")
#
#     elif mode == "r":
#         name = input("請輸入帳號名稱")
#         if (name in get_acc_dic()) == False:
#             print("無此帳號")
#         else:
#             dic = get_acc_dic()
#             print("帳號: "+ dic[name]["account"] + "\n密碼: " + dic[name]["password"])


window = Tk()
window.title("密碼管理器")
window.geometry("600x600")
window.config(padx=50, pady=50)

img = ImageTk.PhotoImage(file="lock.png")
canvas = Canvas(width=224, height=225)
canvas.create_image(112, 112, image=img)                   #參數決定圖片在畫布的中心點座標
canvas.grid(row=0, column=0, columnspan=2)


def get_acc_dic():                              #讀取password.json中的str
    f = open("password.json", "a")              #若目錄底下沒有該檔案，先新增
    f.close()
    with open("password.json", "r") as f:
        password_str = f.read()
        if password_str == "":
            return {}
        else:
            return json.loads(password_str)     #將str轉換為dic

def search_acc():
    acc_dic = get_acc_dic()
    name = entry1.get()
    if (name in acc_dic.keys()) == True:
        messagebox.showinfo(title=name, message="帳號 : " + acc_dic[name]["account"] + "\n密碼 : " + acc_dic[name]["password"])
    else:
        messagebox.showwarning(title="查詢失敗", message="無此帳號名稱")
def add_acc():
    acc_dic = get_acc_dic()
    name = entry1.get()
    acc = entry2.get()
    pw = entry3.get()
    if name == "" or acc == "" or pw == "":
       messagebox.showerror(title="新增失敗", message="輸入框不可為空")
    elif (name in acc_dic.keys()) == True:
        #label4 = Label(text="已有帳號名稱", fg="red", font=("標楷體", 20))
        #label4.grid(row=5, column=0, columnspan=2)
        messagebox.showerror(title="新增失敗", message="已有此帳號名稱")
    else:
        acc_dic[name] = {               #將帳號資料新增到讀取出的dic
            "account": acc,
            "password": pw
        }

        with open("password.json", "w") as f:
            f.write(json.dumps(acc_dic))            #將更新過的dic轉換為str並覆寫至password.json

        entry1.delete(0, 'end')                     #從第0位到最後一位清空entry
        entry2.delete(0, 'end')
        entry3.delete(0, 'end')

        messagebox.showinfo(title="新增成功", message="新增成功")

label1 = Label(text="帳號名稱", font=("標楷體", 20))
label1.grid(row=1, column=0)

entry1 = Entry(width=25, font=("標楷體", 20))
entry1.grid(row=1, column=1)


label2 = Label(text="帳號", font=("標楷體", 20))
label2.grid(row=2, column=0)

entry2 = Entry(width=25, font=("標楷體", 20))
entry2.grid(row=2, column=1)


label3 = Label(text="密碼", font=("標楷體", 20))
label3.grid(row=3, column=0)

entry3 = Entry(width=25, font=("標楷體", 20))
entry3.grid(row=3, column=1)


button1 = Button(width=35, text="搜尋", font=("標楷體", 20),bg="#8E8E8E", fg="white", command=search_acc)
button1.grid(row=4, column=0, columnspan=2)


#button = Button(width=35, text="新增", font=("標楷體", 20),bg="#0066CC", fg="white", command=add_acc(entry1.get(), entry2.get(), entry3.get()))
button2 = Button(width=35, text="新增", font=("標楷體", 20),bg="#0066CC", fg="white", command=add_acc)
button2.grid(row=5, column=0, columnspan=2)




window.mainloop()