import sys

import pygame

from settings import Settings
from messi import Messi

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                     ai_settings.screen_height))
    pygame.display.set_caption("Beat Real Madrid")

    messi = Messi(screen)
    #开始游戏主循环
    while True:

        # 监视鼠标和键盘
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        messi.blitme()
       #让屏幕可见
        pygame.display.flip()

run_game()