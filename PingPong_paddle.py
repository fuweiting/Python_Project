import pygame

class Paddle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.score = 0

    def update(self, up, down, h):
        keys = pygame.key.get_pressed()
        if self.y > 0:
            if keys[up]:
                self.y -= 5
        if self.y < h:
            if keys[down]:
                self.y += 5

    # def update2(self, up, h):
    #     if up:
    #         self.y -= 5
    #     else:
    #         self.y += 5
    #
    #     if self.y < 0:
    #         self.y = 0
    #     elif self.y + self.height > h:
    #         self.y = h - self.height

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))