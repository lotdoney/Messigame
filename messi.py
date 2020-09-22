import pygame

class Messi():

    def __init__(self,screen):
        self.screen = screen

        self.image = pygame.image.load('images/messi.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #放到屏幕底部的中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)
