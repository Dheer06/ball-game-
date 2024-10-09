import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_COLOR = (200, 0, 0)
PADDLE_COLOR = (0, 0, 255)
FPS = 60

# Game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong Game')

# Paddle dimensions
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100

# Ball dimensions
BALL_RADIUS = 10

# Paddle positions
paddle1_x, paddle1_y = 50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_x, paddle2_y = SCREEN_WIDTH - 60, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2

# Ball position and velocity
ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
ball_dx, ball_dy = random.choice([10, 10]), random.choice([4, -4])

# Paddle movement variables
paddle1_dy = 0
paddle2_dy = 0
PADDLE_SPEED = 10

# Game loop
clock = pygame.time.Clock()

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1_dy = -PADDLE_SPEED
            elif event.key == pygame.K_s:
                paddle1_dy = PADDLE_SPEED
            elif event.key == pygame.K_UP:
                paddle2_dy = -PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                paddle2_dy = PADDLE_SPEED
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_w, pygame.K_s]:
                paddle1_dy = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                paddle2_dy = 0

    # Move paddles
    paddle1_y += paddle1_dy
    paddle2_y += paddle2_dy

    # Boundary for paddles
    paddle1_y = max(0, min(SCREEN_HEIGHT - PADDLE_HEIGHT, paddle1_y))
    paddle2_y = max(0, min(SCREEN_HEIGHT - PADDLE_HEIGHT, paddle2_y))

    # Move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with top and bottom
    if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= SCREEN_HEIGHT:
        ball_dy *= -1

    # Ball collision with paddles
    if (paddle1_x < ball_x - BALL_RADIUS < paddle1_x + PADDLE_WIDTH and 
        paddle1_y < ball_y < paddle1_y + PADDLE_HEIGHT):
        ball_dx *= -1
    if (paddle2_x < ball_x + BALL_RADIUS < paddle2_x + PADDLE_WIDTH and 
        paddle2_y < ball_y < paddle2_y + PADDLE_HEIGHT):
        ball_dx *= -1

    # Ball goes out of bounds
    if ball_x < 0 or ball_x > SCREEN_WIDTH:
        ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        ball_dx, ball_dy = random.choice([4, -4]), random.choice([4, -4])

    # Clear screen
    screen.fill(BLACK)

    # Draw paddles
    pygame.draw.rect(screen, PADDLE_COLOR, (paddle1_x, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, PADDLE_COLOR, (paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw ball
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)

    # Update display
    pygame.display.flip()

    # Frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
