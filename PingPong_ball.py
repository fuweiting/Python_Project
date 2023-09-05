import pygame
import random

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        random_list = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.speedx = random.choice(random_list)
        self.speedy = random.choice(random_list)

    def update(self, width, height, paddle1, paddle2):
        self.x += self.speedx
        self.y += self.speedy
        ball_top = self.y - self.radius
        ball_bottom = self.y + self.radius
        ball_left = self.x - self.radius
        ball_right = self.x + self.radius

        if ball_top < 0 or ball_bottom > height:
            self.speedy *= -1                           # y方向反向
        if ball_left < 0:
            paddle2.score += 1
            self.reset(width, height)
        elif ball_right > width:
            paddle1.score += 1
            self.reset(width, height)

    def reset(self, width, height):
        self.x = width / 2
        self.y = height / 2
        random_list = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.speedx = random.choice(random_list)
        self.speedy = random.choice(random_list)

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def collision(self, paddle1, paddle2):
        ball_left = self.x - self.radius
        ball_right = self.x + self.radius

        paddle1_top = paddle1.y
        paddle1_bottom = paddle1.y + paddle1.height
        paddle1_left = paddle1.x
        paddle1_right = paddle1.x + paddle1.width

        paddle2_top = paddle2.y
        paddle2_bottom = paddle2.y + paddle2.height
        paddle2_left = paddle2.x
        paddle2_right = paddle2.x + paddle1.width

        if paddle1_top < self.y < paddle1_bottom:
            if ball_left < paddle1_right:
                self.speedx *= -2

        if paddle2_top < self.y < paddle2_bottom:
            if ball_right > paddle2_left:
                self.speedx *= -2