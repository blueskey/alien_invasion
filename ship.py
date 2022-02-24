import pygame

class Ship:

    def __init__(self, ai_game):

        """初始化飞船，并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings

        self.image = pygame.image.load('images/ship.bmp')

        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        #  rect.x 只能存储整数值，为了让飞船速度可以设置为小数，所以改为在飞船的属性x中存储小数值
        self.x = float(self.rect.x)

        """移动标志"""
        self.moving_right = False

        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # 根据 self.x 更新 rect 对象
        self.rect.x = self.x
