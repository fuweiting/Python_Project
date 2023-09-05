# password = {
#     "account" : "123456",
#     "password" : "123"
# }

# with open("password.json", "a") as file:
#     password_j = json.dumps(password)
#     file.write(password_j)

# with open("password.json", "r") as file:
#     x = json.loads(file.read())
#     print(x["account"])

import json

def get_acc_dic():                          #讀取password.json中的str
    with open("password.json", "r") as f:
        password_str = f.read()
        if password_str == "":
            return {}
        else:
            return json.loads(password_str)     #loads將str轉換為dic

def add_acc(name,acc,pw):
    acc_dic = get_acc_dic()
    acc_dic[name] = {
        "account": acc,
        "password": pw
    }
    with open("password.json", "w") as f:
        f.write(json.dumps(acc_dic))



print("歡迎使用密碼管理器")

while True:
    mode = input("請問要使用什麼功能呢? (r查詢 a新增 q離開)")


    if mode == "a":
        name = input("請輸入帳號名稱")
        acc = input("請輸入帳號")
        pw = input("請輸入密碼")
        if (name in get_acc_dic()) == True:
            print("已有此帳號名稱")
        else:
            add_acc(name,acc,pw)
            print("新增成功")

    elif mode == "q":
        break

    elif mode == "r":
        name = input("請輸入帳號名稱")
        if (name in get_acc_dic()) == False:
            print("無此帳號名稱")
        else:
            dic = get_acc_dic()
            print("帳號: "+ dic[name]["account"] + ", 密碼: " + dic[name]["password"])