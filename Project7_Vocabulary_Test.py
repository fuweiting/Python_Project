eng_dic = {
    "蘋果": "apple",
    "香蕉": "banana",
    "貓": "cat",
    "狗": "dog",
    "蛋": "egg",
    "食物": "food",
    "遊戲": "game",
    "手": "hand",
    "冰": "ice",
    "果醬": "jam",
    "國王": "king",
    "標籤": "label",
    "郵件": "mail",
    "脖子": "neck",
    "油": "oil",
    "豬": "pig",
    "皇后": "queen"
}

import random
key = list(eng_dic)
key_numbers = len(key)
num = random.randint(0,key_numbers-1)

q_numbers = int(input("請問要練習幾題?"))
count = 0

for i in range(q_numbers):
    num = random.randint(0, key_numbers - 1)
    ans = input(f"第{i+1}題\n請問'{key[num]}'的英文是:")
    if ans == eng_dic[key[num]]:
        count += 1
        print("恭喜答對")
    else:
        print(f"答錯了,答案是:{eng_dic[key[num]]}")

print(f"總共{q_numbers}題 答對{count}題")