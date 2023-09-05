import random
letters_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                 "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]

letters_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+"]



print("歡迎使用密碼產生器")
len1 = int(input("請問需要幾個大寫英文字母?"))
len2 = int(input("請問需要幾個小寫英文字母?"))
len3 = int(input("請問需要幾個數字?"))
len4 = int(input("請問需要幾個符號?"))


# 初級密碼產生器

# for i in range(len1):
#     lu = random.randint(0, 25)
#     print(letters_upper[lu],end="")
#
# for i in range(len2):
#     ll = random.randint(0, 25)
#     print(letters_lower[ll],end="")
#
# for i in range(len3):
#     ln = random.randint(0, 9)
#     print(numbers[ln], end="")
#
# for i in range(len4):
#     ls = random.randint(0, 9)
#     print(symbols[ls], end="")


# 進階密碼產生器

pw=[]

for i in range(len1):
    lu = random.randint(0, 25)
    pw.append(letters_upper[lu])

for i in range(len2):
    ll = random.randint(0, 25)
    pw.append(letters_lower[ll])

for i in range(len3):
    ln = random.randint(0, 9)
    pw.append(numbers[ln])

for i in range(len4):
    ls = random.randint(0, 9)
    pw.append(symbols[ls])

# len5 = len6 = len1 + len2 + len3 + len4
# for i in range(len5):
#     l = random.randint(0,len6-1)
#     print(pw[l], end="")
#     pw.remove(pw[l])
#     len6 = len6-1


# better solution
new_pw = ""
random.shuffle(pw)    # 將列表pw打亂
for char in pw:
    new_pw += char    # 將列表轉換成字串
print(new_pw)