import pygame
import math
import random
import time

over = 0
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake game")
color = (250, 0, 0)
foodX = 300
foodY = 400
snake_pos = [300, 300]
speed = 5
move = 0
collusion = 0
snake_body = [[300, 300],[290,300]]
font = pygame.font.Font('freesansbold.ttf', 32)


def food(foodX, foodY):
    pygame.draw.rect(screen, (0, 250, 0), (foodX, foodY, 10, 10))

def grid():
    for x in range(800):
        for y in range(600):
            rec = pygame.draw.rect(x*20, y*20, 20, 20)
            pygame.draw.rect(screen,(0,0,255),rec, 1)

# def snake(x, y):
fps_controller = pygame.time.Clock()


def isCollision(foodX, foodY, snakeX, snakeY):
    distance = math.sqrt((math.pow(foodX - snake_pos[0], 2)) + (math.pow(foodY - snake_pos[1], 2)))
    if distance < 20:
        return True
    else:
        return False


def game_over_text():
    over_text = font.render(" GAME OVER BRO", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


running = True
while running:
    screen.fill((0, 0, 0))
    grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        move = 'up'
    elif keys[pygame.K_DOWN]:
        move = 'dwn'
    elif keys[pygame.K_LEFT]:
        move = 'lft'
    elif keys[pygame.K_RIGHT]:
        move = 'rgt'

    # SNAKE MOVEMENTS--------------------------------------------------------

    if move == 'up' and move!= 'dwn':
        snake_pos[1] -= speed

    if move == 'dwn' and snake_pos[1] <= 580:
        snake_pos[1] += speed

    if move == 'lft' and snake_pos[0] > 0:
        snake_pos[0] -= speed

    if move == 'rgt' and snake_pos[0] <= 780:
        snake_pos[0] += speed

    snake_body.insert(0, list(snake_pos))
    print("body inserted")

    if isCollision(foodX, foodY, snake_pos[0], snake_pos[1]):
        foodX = random.randint(0, 790)
        foodY = random.randint(0, 590)
    else:
        snake_body.pop()
        print("body poped")

    if (snake_pos[0] <= 0 or snake_pos[0] >= 780) or (snake_pos[1] <= 0 or snake_pos[1] >= 580):
        game_over_text()
        over = 1

    if over != 1:
        for i in snake_body:
            pygame.draw.rect(screen, color, (i[0], i[1], 10, 10))

    food(foodX, foodY)
    pygame.display.update()
    fps_controller.tick(70)

pygame.quit()
