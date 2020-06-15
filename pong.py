import pygame, sys

def ball_movement():
    global horizontal_speed, vertical_speed
    ball.x += horizontal_speed
    ball.y += vertical_speed
    if ball.top <= 0 or ball.bottom >= screen_height:
        vertical_speed *= -1
    if ball.right >= screen_width or ball.left <= 0:
        horizontal_speed *= -1
    if ball.colliderect(player1) or ball.colliderect(player2):
        horizontal_speed *= -1
# General setup
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Hamzah\'s Pong')

# Colors
light_grey = (200,200,200)
ball_color = (5, 80, 171)
rect_color = (15, 80, 171)
bg_color = pygame.Color('grey12')

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player1 = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,140)
player2 = pygame.Rect(10, screen_height / 2 - 70, 10,140)
horizontal_speed = 5
vertical_speed = 5
player1_speed = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed +=7
            if event.key == pygame.K_UP:
                player1_speed -=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -=7
            if event.key == pygame.K_UP:
                player1_speed +=7
        ball_movement()
    player1.y +=player1_speed
	# Visuals 
    screen.fill(bg_color)
    pygame.draw.rect(screen, rect_color, player1)
    pygame.draw.rect(screen, rect_color, player2)
    pygame.draw.ellipse(screen, ball_color, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))

    pygame.display.flip()
    clock.tick(60)
