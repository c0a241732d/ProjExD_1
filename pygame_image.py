import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    fbg_img = pg.transform.flip(bg_img, True, False)
    tmr = 0
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        t = tmr
        x = 0
        y = 0

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_RIGHT] == True:
            x += 2
        elif key_lst[pg.K_LEFT] == True:
            x -= 1
        elif key_lst[pg.K_UP] == True:
            y -= 1
        elif key_lst[pg.K_DOWN] == True:
            y += 1
        
        screen.blit(bg_img, [-t, 0])
        screen.blit(fbg_img, [-t + 1600, 0])
        screen.blit(bg_img, [-t + 3200, 0])
        
        kk_rct.move_ip((x - 1, y))
    
        screen.blit(kk_img, kk_rct)

        pg.display.update()
        tmr += 1
        if tmr == 3200:
            tmr = 0  
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()