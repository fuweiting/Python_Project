import json
import random

def get_questions():
    with open("questions.json", "r", encoding="utf-8") as f:
        return json.loads(f.read())

class Question:
    def __init__(self, description, answer):
        self.description = description
        self.answer = answer

    def ask(self):
        x = input(self.description)
        if x == self.answer:
            return print("True")
        else:
            return print("False")

class QuestionGame:
    def __init__(self, questions, score):
        self.questions = questions
        self.score = score

    def random_pick(self, num):
        return num

    def play(self,num):
        for i in range(num):
            p = random.randint(0,n-1)
            x = input(l[p]["description"])
            if x == l[p]["answer"]:
                print("恭喜答對")
                self.score += 1
            else:
                print("答錯了 答案為" + l[p]["answer"])

        print(f"共答對{self.score}題")


l = get_questions()
n = len(l)

question_game = QuestionGame(l,0)
num = question_game.random_pick(3)

question_game.play(num)

