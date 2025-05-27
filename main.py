import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

# Game variables
gravity = 0.5
bird_movement = 0
bird_y = HEIGHT // 2
bird_radius = 20

pipe_width = 70
pipe_height = 500
pipe_gap = 150
pipe_x = WIDTH
pipe_y = random.randint(150, HEIGHT - 150)

score = 0
font = pygame.font.SysFont(None, 40)

clock = pygame.time.Clock()

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill(BLUE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = -10

    # Bird movement
    bird_movement += gravity
    bird_y += bird_movement

    # Pipe movement
    pipe_x -= 5
    if pipe_x < -pipe_width:
        pipe_x = WIDTH
        pipe_y = random.randint(150, HEIGHT - 150)
        score += 1

    # Draw bird
    pygame.draw.circle(screen, WHITE, (50, int(bird_y)), bird_radius)

    # Draw pipes
    pygame.draw.rect(screen, GREEN, (pipe_x, 0, pipe_width, pipe_y - pipe_gap // 2))
    pygame.draw.rect(screen, GREEN, (pipe_x, pipe_y + pipe_gap // 2, pipe_width, HEIGHT))

    # Collision detection
    bird_rect = pygame.Rect(50 - bird_radius, bird_y - bird_radius, bird_radius * 2, bird_radius * 2)
    top_pipe_rect = pygame.Rect(pipe_x, 0, pipe_width, pipe_y - pipe_gap // 2)
    bottom_pipe_rect = pygame.Rect(pipe_x, pipe_y + pipe_gap // 2, pipe_width, HEIGHT)

    if bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect) or bird_y - bird_radius <= 0 or bird_y + bird_radius >= HEIGHT:
        print(f"Game Over! Your score: {score}")
        pygame.quit()
        sys.exit()

    # Display score
    score_surface = font.render(f"Score: {score}", True, RED)
    screen.blit(score_surface, (10, 10))

    pygame.display.update()
