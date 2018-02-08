import pygame
# import time
import random


class FlappyBird:
    def quit_game(self):
        pygame.quit()
        quit()

    def pipes(self, pipex, pipey, pipew, pipeh, color):
        pygame.draw.rect(gameDisplay, color, [pipex, pipey, pipew, pipeh])

    def score(self, count):
        font = pygame.font.Font("/static/font/kirbyss.ttf", 30)
        text = font.render("Score : "+ str(count), True, black)
        gameDisplay.blit(text, (display_width-250, 25))

    def bird(self, x, y):
        gameDisplay.blit(birdImg, (x, y))

    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface,textSurface.get_rect()

    def button(self, msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font("/static/font/kirbyss.ttf", 20)
        button_obj = FlappyBird()
        textSurf, textRect = button_obj.text_objects(msg, smallText, white)
        textRect.center = ((x+(w/2)), (y+(h/2)))
        gameDisplay.blit(textSurf, textRect)

    def crash(self):
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(crash_sound)
        largeText = pygame.font.Font("kirbyss.ttf", 115)
        crash_obj = FlappyBird()
        TextSurf, TextRect = crash_obj.text_objects("You Crashed", largeText, bright_red)
        TextRect.center = ((display_width*0.5), (display_height*0.4))
        gameDisplay.blit(TextSurf, TextRect)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crash_obj.quit_game()
            crash_obj.button("Retry", 350, 450, 200, 50, indigo, bright_indigo, crash_obj.game_loop)
            crash_obj.button("Quit", 750, 450, 200, 50, red, bright_red, crash_obj.quit_game)
            pygame.display.update()
            clock.tick(15)

    def game_intro(self):
        birdStartx = 100
        birdStarty = 300
        birdWithGun = pygame.image.load("/home/amardeep/Downloads/birdWithGun1.png")
        intro_obj = FlappyBird()
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro_obj.quitgame()
            gameDisplay.fill(black)
            largeText = pygame.font.Font('PAC-FONT.TTF', 90)
            smallText = pygame.font.Font('kirbyss.ttf', 30)
            TextSurf, TextRect = intro_obj.text_objects("Flappy Bird", largeText, blue)
            TextRect.center = ((display_width * 0.5), (display_height * 0.4))
            gameDisplay.blit(TextSurf, TextRect)
            TextSurf, TextRect = intro_obj.text_objects("fly, die, retry . . .", smallText, blue)
            TextRect.center = ((display_width * 0.7), (display_height * 0.55))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(birdWithGun, (birdStartx, birdStarty))
            intro_obj.button("GO!", 350, 450, 200, 50, green, bright_green, intro_obj.game_loop)
            intro_obj.button("QUIT", 750, 450, 200, 50, red, bright_red, intro_obj.quitgame)
            pygame.display.update()

    def quitgame(self):
        pygame.quit()
        quit()

    def unpause(self):
        global pause
        pause = False
        pygame.mixer.music.unpause()

    def paused(self):
        global pause
        pygame.mixer.music.pause()
        paused_obj = FlappyBird()
        largeText = pygame.font.Font('kirbyss.ttf', 90)
        smallText = pygame.font.Font('kirbyss.ttf', 30)
        TextSurf, TextRect = paused_obj.text_objects("Paused", largeText, black)
        TextRect.center = ((display_width * 0.5), (display_height * 0.5))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = paused_obj.text_objects("Hit Continue!", smallText, black)
        TextRect.center = ((display_width * 0.5), (display_height * 0.6))
        gameDisplay.blit(TextSurf, TextRect)
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            paused_obj.button("Continue", 350, 450, 200, 50, green, bright_green, paused_obj.unpause)
            paused_obj.button("QUIT", 750, 450, 200, 50, red, bright_red, paused_obj.quitgame)
            pygame.display.update()
            clock.tick(15)

    def game_loop(self):
        global pause
        pygame.mixer.music.play(-1)
        x = (display_width * 0)
        y = (display_height * 0.45)
        game_loop_obj = FlappyBird()
        y_change = 0
        pipe_startx = display_width + 200
        pipe_starty = -200
        pipe_speed = 10
        pipe_width = 150
        pipe_height = random.randrange(display_height * 0.45, display_height * 0.65)
        pipe_startx1 = display_width + 200
        pipe_starty1 = random.randrange(display_height * 0.55, display_height * 0.75)
        pipe_speed1 = 15
        pipe_speed2 = 20
        pipe_width1 = 150
        pipe_height1 = random.randrange(display_height * 0.55, display_height * 0.75)
        gameExit = False
        bird_height = 60
        bird_width = 100
        gravity = 4
        global count
        count = 0
        pipe_change = 0
        # loop to control the events occuring in the game
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        y_change = -10
                    if event.key == pygame.K_DOWN:
                        y_change = 5
                    if event.key == pygame.K_p:
                        pause = True
                        game_loop_obj.paused()
                    if event.key == pygame.K_RIGHT:
                        pipe_change = -10
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_change = 0
                        pipe_change = 0
            y += y_change
            # filling the background with blue color
            gameDisplay.fill(blue)
            # displaying sun and background on the game display
            pygame.draw.circle(gameDisplay, yellow, (150, 50), 50)
            # drawing pipes onto the screen
            game_loop_obj.pipes(pipe_startx, pipe_starty, pipe_width, pipe_height, green)
            game_loop_obj.pipes(pipe_startx1, pipe_starty1, pipe_width1, pipe_height1, green)
            pipe_startx1 -= pipe_speed
            pipe_startx -= pipe_speed
            game_loop_obj.score(count)
            # drawing bird and displaying the count on to the gaming screen
            game_loop_obj.bird(x, y)
            y += gravity
            if y < 0 or y > display_height - bird_height:
                game_loop_obj.crash()
            if pipe_startx == 0:
                if count<20:
                    count += 5
                if count>=20:
                    count += 6
            game_loop_obj.score(count)
            # if a pipe has completely crossed the gaming screen we are drawing another pipe
            if pipe_startx < 0 - pipe_width:
                pipe_startx = display_width - pipe_width
                pipe_starty = random.randrange(-200, -100)
            if pipe_startx1 < 0 - pipe_width:
                pipe_startx1 = display_width - pipe_width1
                pipe_starty1 = random.randrange(display_height * 0.6, display_height * 0.75)
            # checking if crash has occured or not
            if x + bird_width > pipe_startx:
                if y < pipe_starty + pipe_height or y > pipe_starty1 - bird_height:
                    game_loop_obj.crash()
            pygame.display.update()
            clock.tick(70)
        game_loop_obj.game_intro()
        game_loop_obj.game_loop()
        game_loop_obj.quit_game()


if __name__ == "__main__":
    obj = FlappyBird()
    display_width = 1300
    display_height = 600
    pygame.init()
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Flappy Bird")
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (150, 0, 0)
    bright_red = (255, 0, 0)
    green = (0, 150, 0)
    bright_green = (0, 255, 0)
    blue = (102, 255, 255)
    yellow = (255, 255, 0)
    pause = True
    indigo = (70, 0, 130)
    bright_indigo = (70, 0, 200)
    birdImg = pygame.image.load("/home/amardeep/Downloads/bird_image/yellow_bird.png")
    crash_sound = pygame.mixer.Sound("Glass_Shatters_Into_Debris.wav")
    pygame.mixer.music.load("Superboy.mp3")
    clock= pygame.time.Clock()
    obj.game_intro()
    obj.game_loop()
    obj.quit_game()
