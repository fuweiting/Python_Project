import random

print("歡迎來到猜數字遊戲\n謎底為1~100隨機的一個整數(最多5次猜測機會)")

secret = random.randint(1,100)

i=0
f = False
for i in range(0,5):
    guess_str = input(f"第{i+1}次猜測\n請輸入猜測的數字:")
    if guess_str.isdigit() == False:
        print("請輸入整數")
        continue

    guess = int(guess_str)

    if guess < secret:
        print("大一點")
    elif guess > secret:
        print("小一點")
    elif guess == secret:
        print("猜對了")
        f = True
        break

if f == False:
    print(f"你輸了 超出猜測次數\n謎底為{secret}")