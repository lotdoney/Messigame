import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_settings,screen,messi):
        super(Bullet,self).__init__()
        self.screen = screen

        #在（0，0）处创建一个表示子弹的圆形
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = messi.rect.centerx
        self.rect.top = messi.rect.top

        self.y  = float(self.rect.y)

        self.radius = ai_settings.bullet_radius
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

