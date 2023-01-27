import pygame

# Initialize Pygame
pygame.init()

# Set screen size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set title
pygame.display.set_caption("Pong")

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)

# Initialize ball position and speed
ball_x = 350
ball_y = 250
ball_speed_x = 5
ball_speed_y = 5

# Initialize paddle position and speed
paddle1_y = 200
paddle2_y = 200
paddle_speed = 5

# Set font
font = pygame.font.Font(None, 30)

# Initialize score
score1 = 0
score2 = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check for ball collision with top and bottom of screen
    if ball_y > 490 or ball_y < 10:
        ball_speed_y = -ball_speed_y

    # Check for ball collision with left and right of screen
    if ball_x < 10:
        score2 += 1
        ball_x = 350
        ball_y = 250
    elif ball_x > 690:
        score1 += 1
        ball_x = 350
        ball_y = 250

    # Check for ball collision with paddles
    if ball_x == 20 and (paddle1_y < ball_y < paddle1_y + 80):
        ball_speed_x = -ball_speed_x
    elif ball_x == 680 and (paddle2_y < ball_y < paddle2_y + 80):
        ball_speed_x = -ball_speed_x

    # Move paddles based on user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN]:
        paddle2_y += paddle_speed
    if keys[pygame.K_w]:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s]:
        paddle1_y += paddle_speed

    # Check for paddle collision with top and bottom of screen
    if paddle1_y < 0:
        paddle1_y = 0
    elif paddle1_y > 420:
        paddle1_y = 420
    if paddle2_y < 0:
        paddle2_y = 0
    elif paddle2_y > 420:
        paddle2_y = 420

    # Clear screen
    screen.fill(black)

    # Draw paddles
    pygame.draw.rect(screen, white, (10, paddle1_y, 20, 80))
    pygame.draw.rect(screen, white, (670, paddle2_y, 20, 80))

    # Draw ball
    pygame.draw.circle(screen, white, (ball_x, ball_y), 10)

    # Draw scores
    score1_text = font.render("Player 1: " + str(score1), True, white)
    score2_text = font.render("Player 2: " + str(score2), True, white)
    screen.blit(score1_text, (250, 10))
    screen.blit(score2_text, (350, 10))

    # Update screen
    pygame.display.flip()

    # Set frame rate
    clock = pygame.time.Clock()
    clock.tick(60)
pygame.quit()
