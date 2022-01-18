import pygame  as pg
from player import *
pg.init()
# Set up the drawing window

screen = pg.display.set_mode((screen_width,screen_hight))
pg.draw.rect(screen, (255,255,255), (50, 20, 120, 100))
pg.draw.rect(screen, (255,255,255), (350, 20, 120, 100), 1)


running = True
# Player 1
player_1=Player()
# Player 2
player_2 = Player()
player_2.rect= pg.Rect(10, 0,player_2.player_width,player_2.player_hight)
#Ball
ball=Ball()

all_sprites = pg.sprite.Group()
all_sprites.add(player_1)
all_sprites.add(player_2)
all_sprites.add(ball)


ball_speed_y=1
ball_speed_x=1

font=pg.font.Font("freesansbold.ttf",32)
text_x=10
text_y=10


while running:

    # Did the user click the window close button?
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((0, 0, 0))
    ball.rect.x+=ball_speed_x
    ball.rect.y+=ball_speed_y
    # stay on screen
    if ball.rect.top<=0 or ball.rect.bottom>=screen_hight:
        ball_speed_y*=-1

    #     middle screen line
    pg.draw.rect(screen, (255, 240, 255), (screen_width/2, 0, 1, screen_hight), 1)

    # Score
    if ball.rect.left==0:
        player_2.score+=1
        print("player_1.score",player_1.score)



        ball.rect =pg.Rect(800/2, 600/2 -70, 30, 30)

    if ball.rect.right== screen_width:
        player_1.score+=1
        print("player_2.score",player_2.score)



        ball.rect =pg.Rect(screen_width/2, screen_hight/2 -70, 30, 30)

    pg.draw.ellipse(screen, (250, 250, 250), ball.rect)

    # Player 1   Movement
    pressed_keys=pg.key.get_pressed()
    player_1.move(pressed_keys,K_UP,K_DOWN)
    pg.draw.rect(screen,(240, 240, 240),player_1.rect)
    # Player 2  Movement
    pressed_keys=pg.key.get_pressed()
    player_2.move(pressed_keys,K_w,K_s)
    pg.draw.rect(screen,(240, 240, 240),player_2.rect)

    # detect collisions

    hits = pg.sprite.spritecollide(ball, all_sprites, False)
    if hits.__contains__(player_1) or hits.__contains__(player_2):
        ball_speed_x*=-1

    score_text = font.render("player score: " + str(player_1.score), True, (255, 255, 255))
    screen.blit(score_text, (screen_width / 3, 50) )
    score_text = font.render("player score: " + str(player_2.score), True, (255, 255, 255))
    screen.blit(score_text, (screen_width /2 +30 , 50))


    pg.display.flip()



# Done! Time to quit.
pg.quit()