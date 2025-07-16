import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

ball_size = 20
ball_x = WIDTH // 2 - ball_size // 2
ball_y = HEIGHT // 2 - ball_size // 2
ball_speed_x = 7
ball_speed_y = 7

paddle_width = 10
paddle_height = 100

player1_x = 30
player1_y = HEIGHT // 2 - paddle_height // 2

player2_x = WIDTH - 40
player2_y = HEIGHT // 2 - paddle_height // 2

paddle_speed = 10

score1 = 0
score2 = 0

computer_turn = True
font = pygame.font.Font(None, 74)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < HEIGHT - paddle_height:
        player1_y += paddle_speed

    if computer_turn:
        if player2_y + paddle_height // 2 < ball_y - 10:
            player2_y += paddle_speed
        elif player2_y + paddle_height // 2 > ball_y + 10:
            player2_y -= paddle_speed

    player2_y = max(0, min(player2_y, HEIGHT - paddle_height))

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y <= 0 or ball_y >= HEIGHT - ball_size:
        ball_speed_y *= -1

    if (player1_x < ball_x + ball_size and
        player1_x + paddle_width > ball_x and
        player1_y < ball_y + ball_size and
        player1_y + paddle_height > ball_y):
        ball_speed_x *= -1
        computer_turn = True

    if (player2_x < ball_x + ball_size and
        player2_x + paddle_width > ball_x and
        player2_y < ball_y + ball_size and
        player2_y + paddle_height > ball_y):
        ball_speed_x *= -1
        computer_turn = False

    if ball_x < 0:
        score2 += 1
        ball_x = WIDTH // 2 - ball_size // 2
        ball_y = HEIGHT // 2 - ball_size // 2
        ball_speed_x *= -1
        computer_turn = True

    if ball_x >= WIDTH:
        score1 += 1
        ball_x = WIDTH // 2 - ball_size // 2
        ball_y = HEIGHT // 2 - ball_size // 2
        ball_speed_x *= -1
        computer_turn = True

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, ball_size, ball_size))
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    text1 = font.render(str(score1), True, WHITE)
    text2 = font.render(str(score2), True, WHITE)

    screen.blit(text1, (WIDTH // 4, 20))
    screen.blit(text2, (WIDTH * 3 // 4, 20))

    pygame.display.flip()
    clock.tick(60)
