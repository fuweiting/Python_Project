import random

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


ken = ["s", "r", "p"]
player = input("請輸入字母 s(剪刀) r(石頭) p(布)")

num = random.randint(0,2)
com = ken[num]

print("你出:")
if player == "s":
    print(scissor)
    if com == "s":
        print(f"電腦出:\n{scissor}\n平手")
    elif com == "r":
        print(f"電腦出:\n{rock}\n你輸了QQ")
    else:
        print(f"電腦出:\n{paper}\n你贏了XD")
elif player == "r":
    print(rock)
    if com == "s":
        print(f"電腦出:\n{scissor}\n你贏了XD")
    elif com == "r":
        print(f"電腦出:\n{rock}\n平手")
    else:
        print(f"電腦出:\n{paper}\n你輸了QQ")
elif player == "p":
    print(paper)
    if com == "s":
        print(f"電腦出:\n{scissor}\n你輸了QQ")
    elif com == "r":
        print(f"電腦出:\n{rock}\n你贏了XD")
    else:
        print(f"電腦出:\n{paper}\n平手")
