import sys

import pygame
from bullet import Bullet


def check_events(ai_settings,screen,messi,bullets):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN :
            check_keydown_events(event,ai_settings,screen,messi,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,messi)



def check_keydown_events(event,ai_settings,screen,messi,bullets):
    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        messi.moving_right = True
    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
        messi.moving_left = True
    elif event.key ==pygame.K_SPACE:
        new_bullet = Bullet(ai_settings,screen,messi)
        bullets.add(new_bullet)

def check_keyup_events(event,messi):
    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        messi.moving_right = False
    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
        messi.moving_left = False

def update_screen(ai_settings,screen,messi,bullets):
    screen.fill(ai_settings.bg_color)
    messi.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 让屏幕可见
    pygame.display.flip()
