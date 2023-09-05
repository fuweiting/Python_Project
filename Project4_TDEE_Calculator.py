# 綜合健康計算機
def get_bmi(h,w):
    h=h/100
    bmi = w/h**2
    return bmi

def get_bmr(sex,h,w,age):
    if sex == "1":
        bmr = 66 + 13.7*w + 5*h - 6.8*age
    else:
        bmr = 655 + 9.6*w + 1.8*h - 4.7*age
    return bmr

def get_tdee(sex,h,w,age,t):
    bmr = get_bmr(sex, h, w, age)
    if t == "1":
        tdee = bmr*1.2
    elif t == "2":
        tdee = bmr*1.375
    elif t == "3":
        tdee = bmr*1.55
    elif t == "4":
        tdee = bmr*1.725
    elif t == "5":
        tdee = bmr*1.9
    return tdee

print("歡迎使用綜合健康計算機")
print("(1)計算BMI\n(2)計算基礎代謝率BMR\n(3)計算總熱量消耗TDEE")
c = input("請選擇要計算的項目 (輸入1 or 2 or 3)")

if c == "1":
    h = float(input("請輸入您的身高(公分)"))
    w = float(input("請輸入您的體重(公斤)"))
    BMI = get_bmi(h,w)
    BMI = round(BMI,1)
    print(f"您的BMI:{BMI}")

elif c == "2":
    sex = input("請輸入您的性別(1)男 (2)女")
    h = float(input("請輸入您的身高(公分)"))
    w = float(input("請輸入您的體重(公斤)"))
    age = float(input("請輸入您的年齡"))
    BMR = get_bmr(sex,h,w,age)
    BMR = round(BMR,2)
    print(f"您的BMR:{BMR}")

elif c == "3":
    sex = input("請輸入您的性別(1)男 (2)女")
    h = float(input("請輸入您的身高(公分)"))
    w = float(input("請輸入您的體重(公斤)"))
    age = float(input("請輸入您的年齡"))
    print("(1)久坐、幾乎沒運動")
    print("(2)每週低強度運動1~3天")
    print("(3)每週中強度運動3~5天")
    print("(4)每週高強度運動6~7天")
    print("(5)勞力密集工作或是每天高強度訓練")
    t = input("請輸入您的運動量 (輸入1~5)")
    TDEE = get_tdee(sex, h, w, age, t)
    TDEE = round(TDEE,2)
    print(f"您的TDEE:{TDEE}")

