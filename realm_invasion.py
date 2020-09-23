import sys

import pygame

from settings import Settings
from messi import Messi
from pygame.sprite import Group

import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                  ai_settings.screen_height))
    pygame.display.set_caption("Beat Real Madrid")

    messi = Messi(ai_settings,screen)
    bullets  = Group()
    #开始游戏主循环
    while True:

        # 监视鼠标和键盘
        gf.check_events(ai_settings,screen,messi,bullets)
        messi.update()
        bullets.update()
        gf.update_screen(ai_settings,screen,messi,bullets)

run_game()