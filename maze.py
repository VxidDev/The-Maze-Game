import pygame
import math

pygame.init()

WIDTH , HEIGHT = 500 , 350
screen = pygame.display.set_mode((WIDTH , HEIGHT))

Running = True
vision_radius = 25

player = pygame.Rect(0 , 0 , 25 , 25)
direction = None

blocks = [
    pygame.Rect(25,0,25,25),pygame.Rect(25,50,25,25),pygame.Rect(0,75,25,25),pygame.Rect(25,75,25,25),pygame.Rect(50,50,25,25),pygame.Rect(75,50,25,25),pygame.Rect(100,50,25,25),pygame.Rect(75,25,25,25),pygame.Rect(125,0,25,25),pygame.Rect(150,0,25,25),
    pygame.Rect(75,100,25,25),pygame.Rect(100,100,25,25),pygame.Rect(125,100,25,25),pygame.Rect(150,100,25,25),pygame.Rect(150,50,25,25),pygame.Rect(150,75,25,25),pygame.Rect(25,125,25,25),pygame.Rect(50,125,25,25),pygame.Rect(75,125,25,25),pygame.Rect(125,150,25,25),
    pygame.Rect(125,175,25,25),pygame.Rect(125,200,25,25),pygame.Rect(0,175,25,25),pygame.Rect(25,175,25,25),pygame.Rect(50,175,25,25),pygame.Rect(75,175,25,25),pygame.Rect(100,175,25,25),pygame.Rect(50,225,25,25),pygame.Rect(75,225,25,25),pygame.Rect(0,225,25,25),
    pygame.Rect(0,250,25,25),pygame.Rect(0,275,25,25),pygame.Rect(25,275,25,25),pygame.Rect(75,250,25,25),pygame.Rect(75,275,25,25),pygame.Rect(25,325,25,25),pygame.Rect(50,325,25,25),pygame.Rect(75,325,25,25),pygame.Rect(100,325,25,25),pygame.Rect(125,325,25,25),
    pygame.Rect(150,325,25,25),pygame.Rect(175,325,25,25),pygame.Rect(200,325,25,25),pygame.Rect(225,325,25,25),pygame.Rect(250,325,25,25),pygame.Rect(125,300,25,25),pygame.Rect(100,250,25,25),pygame.Rect(125,250,25,25),pygame.Rect(150,250,25,25),pygame.Rect(175,250,25,25),
    pygame.Rect(175,275,25,25),pygame.Rect(200,275,25,25),pygame.Rect(225,275,25,25),pygame.Rect(175,100,25,25),pygame.Rect(175,125,25,25),pygame.Rect(175,150,25,25),pygame.Rect(175,175,25,25),pygame.Rect(175,200,25,25),pygame.Rect(175,225,25,25),pygame.Rect(200,25,25,25),
    pygame.Rect(200,50,25,25),pygame.Rect(200,75,25,25),pygame.Rect(200,100,25,25),pygame.Rect(250,0,25,25),pygame.Rect(250,25,25,25),pygame.Rect(250,50,25,25),pygame.Rect(250,75,25,25),pygame.Rect(250,100,25,25),pygame.Rect(250,125,25,25),pygame.Rect(250,150,25,25),
    pygame.Rect(225,150,25,25),pygame.Rect(200,200,25,25),pygame.Rect(225,200,25,25),pygame.Rect(250,200,25,25),pygame.Rect(275,200,25,25),pygame.Rect(300,200,25,25),pygame.Rect(275,100,25,25),pygame.Rect(325,100,25,25),pygame.Rect(350,100,25,25),pygame.Rect(300,150,25,25),
    pygame.Rect(325,150,25,25),pygame.Rect(325,175,25,25),pygame.Rect(325,200,25,25),pygame.Rect(225,250,25,25),pygame.Rect(250,250,25,25),pygame.Rect(275,250,25,25),pygame.Rect(300,250,25,25),pygame.Rect(325,250,25,25),pygame.Rect(350,250,25,25),pygame.Rect(375,100,25,25),
    pygame.Rect(375,125,25,25),pygame.Rect(375,150,25,25),pygame.Rect(375,175,25,25),pygame.Rect(375,200,25,25),pygame.Rect(375,225,25,25),pygame.Rect(375,250,25,25),pygame.Rect(325,50,25,25),pygame.Rect(325,75,25,25),pygame.Rect(300,25,25,25),pygame.Rect(300,50,25,25),
    pygame.Rect(375,0,25,25),pygame.Rect(375,25,25,25),pygame.Rect(375,50,25,25),pygame.Rect(375,75,25,25),pygame.Rect(350,0,25,25),pygame.Rect(275,300,25,25),pygame.Rect(275,325,25,25),pygame.Rect(325,325,25,25),pygame.Rect(325,275,25,25),pygame.Rect(375,250,25,25),
    pygame.Rect(375,275,25,25),pygame.Rect(375,300,25,25),pygame.Rect(425,325,25,25),pygame.Rect(450,325,25,25),pygame.Rect(475,325,25,25),pygame.Rect(475,125,25,25),pygame.Rect(475,150,25,25),pygame.Rect(475,175,25,25),pygame.Rect(475,200,25,25),pygame.Rect(475,225,25,25),
    pygame.Rect(475,250,25,25),pygame.Rect(475,275,25,25),pygame.Rect(475,300,25,25),pygame.Rect(425,225,25,25),pygame.Rect(450,225,25,25),pygame.Rect(450,125,25,25),pygame.Rect(400,175,25,25),pygame.Rect(425,175,25,25),pygame.Rect(400,125,25,25),pygame.Rect(400,75,25,25),
    pygame.Rect(425,75,25,25),pygame.Rect(450,75,25,25),pygame.Rect(425,25,25,25),pygame.Rect(450,25,25,25),pygame.Rect(475,25,25,25),pygame.Rect(400,275,25,25),pygame.Rect(425,275,25,25)
]

destinition = pygame.Rect(475 , 0 , 25 , 25)
font = pygame.font.Font(None , 50)
win_message = font.render("You finished the maze!" , True , (255 , 255 , 255))
finish_block = pygame.Rect(450 , 0 , 25 , 25)

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.x += 25; direction = "right"
            if event.key == pygame.K_a:
                player.x -= 25; direction = "left"
            if event.key == pygame.K_s:
                player.y += 25; direction = "down"
            if event.key == pygame.K_w:
                player.y -= 25; direction = "up"

    if player.left < 0:
        player.x += 25
    if player.top < 0:
        player.y += 25
    if player.right > 500:
        player.x -= 25
    if player.bottom > 350:
        player.y -= 25

    screen.fill((0 , 0 , 0))
    for block in blocks:
        dx = block.centerx - player.centerx; dy = block.centery - player.centery
        distance = math.sqrt(dx*dx + dy*dy)
        if distance <= vision_radius: pygame.draw.rect(screen , (180 , 180 , 180), block)
        if player.colliderect(block) and direction == "left": player.x += 25
        if player.colliderect(block) and direction == "right": player.x -= 25
        if player.colliderect(block) and direction == "up": player.y += 25
        if player.colliderect(block) and direction == "down": player.y -= 25

    dx = destinition.centerx - player.centerx; dy = destinition.centery - player.centery

    if math.sqrt(dx*dx + dy*dy) <= vision_radius:
        pygame.draw.rect(screen , (0 , 255 , 0), destinition)

    if player.colliderect(destinition):
        vision_radius = 1000
        screen.blit(win_message , (75 , 150))
        pygame.draw.rect(screen , (0 , 0 , 0, 255), finish_block)

    if player.colliderect(finish_block): player.x += 32
    pygame.draw.rect(screen, (255, 255, 255), player)
    
    pygame.display.flip()

pygame.quit()
