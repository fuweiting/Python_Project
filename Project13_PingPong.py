import pygame
from PingPong_ball import Ball
from PingPong_paddle import Paddle

# def paddle_move(keys, paddle1, paddle2):
#     if keys[pygame.K_LEFT]:
#         paddle1.update2(True, HEIGHT)
#     if keys[pygame.K_RIGHT]:
#         paddle1.update2(False, HEIGHT)
#
#     if keys[pygame.K_UP]:
#         paddle2.update2(True, HEIGHT)
#     if keys[pygame.K_DOWN]:
#         paddle2.update2(False, HEIGHT)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 700
HEIGHT = 500

FPS = 60             # frames per second

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))         # tuple表示視窗的(寬,高)
pygame.display.set_caption("PingPong")


font = pygame.font.Font("微軟正黑體.ttf", 30)               # 字形, 字體大小

ball = Ball(WIDTH/2, HEIGHT/2, 10, WHITE)


paddle1 = Paddle(10, HEIGHT/2-50, 15, 100, WHITE)
paddle2 = Paddle(WIDTH-25, HEIGHT/2-50, 15, 100, WHITE)

clock = pygame.time.Clock()         # 利用Clock函式限制while迴圈每秒執行次數的上限

run = True
x = 0
y = 100

while run:
    clock.tick(FPS)                  # 限制每秒最多執行FPS次
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    # 遊戲更新
    ball.update(WIDTH, HEIGHT, paddle1, paddle2)

    paddle1.update(pygame.K_UP, pygame.K_DOWN, HEIGHT-100)
    paddle2.update(pygame.K_LEFT, pygame.K_RIGHT, HEIGHT-100)
    # keys = pygame.key.get_pressed()
    # paddle_move(keys, paddle1, paddle2)

    ball.collision(paddle1, paddle2)


    # 畫面顯示
    window.fill(BLACK)         # (R, G, B) ,也可以使用16進位編碼

    text1 = font.render(f"{paddle1.score}", True, WHITE)  # 文字, 反鋸齒, 顏色
    window.blit(text1, (100, 50))                         # 顯示文字

    text2 = font.render(f"{paddle2.score}", True, WHITE)
    window.blit(text2, (WIDTH-100-30, 50))

    #pygame.draw.rect(window, WHITE, (100, y, 100, 100))       # (x, y, 寬, 高)
    #pygame.draw.circle(window, WHITE, (400, 400), 50)           # (x, y), 半徑
    ball.draw(window)

    paddle1.draw(window)
    paddle2.draw(window)

    pygame.display.update()

pygame.quit()