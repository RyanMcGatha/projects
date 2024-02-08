import pygame, random

pygame.init()

cell_size = 40
cell_count = 20  
screen = pygame.display.set_mode((cell_size * cell_count, cell_size * cell_count))
background_image = pygame.image.load("assets/black.jpg") 
background_image = pygame.transform.scale(background_image, (cell_size * cell_count, cell_size * cell_count))
pygame.mixer.music.load("assets/homept2.mp3")
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
caption = pygame.display.set_caption('Sneaky Serpent')
font = pygame.font.Font(None, 36)  
white = (255, 255, 255)

def render_text(text, color, x, y):
    score_text = font.render(text, True, color)
    screen.blit(score_text, (x, y))

snake_size = 40
snake_speed = 10 
snake_x = 200
snake_y = 240
snake_direction = "RIGHT"

def draw_snake():
    snake_x -= 40
    pygame.draw.rect(screen, white, (snake_x, snake_y, snake_size, snake_size))

apple_size = 40
apple_x = random.randrange(0, cell_count) * cell_size
apple_y = random.randrange(0, cell_count) * cell_size

score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN" and snake_y > 0:
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP" and snake_y < (cell_count - 1) * cell_size:
                snake_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT" and snake_x > 0:
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT" and snake_x < (cell_count - 1) * cell_size:
                snake_direction = "RIGHT"

    if snake_direction == "UP":
        snake_y -= cell_size  
    elif snake_direction == "DOWN":
        snake_y += cell_size  
    elif snake_direction == "LEFT":
        snake_x -= cell_size  
    elif snake_direction == "RIGHT":
        snake_x += cell_size 

    if (
        snake_x < 0
        or snake_x >= cell_count * cell_size
        or snake_y < 0
        or snake_y >= cell_count * cell_size
    ):
        snake_x = 200
        snake_y = 240
        snake_direction = "RIGHT"
        score = 0 
        snake_speed = 10 

    screen.blit(background_image, (0, 0))

    for x in range(0, cell_count * cell_size, cell_size):
        pygame.draw.line(screen, white, (x, 0), (x, cell_count * cell_size))
    for y in range(0, cell_count * cell_size, cell_size):
        pygame.draw.line(screen, white, (0, y), (cell_count * cell_size, y))

    pygame.draw.rect(screen, white, (snake_x, snake_y, snake_size, snake_size))

    pygame.draw.rect(screen, (255, 0, 0), (apple_x, apple_y, apple_size, apple_size))

    snake_rect = pygame.Rect(snake_x, snake_y, snake_size, snake_size)
    apple_rect = pygame.Rect(apple_x, apple_y, apple_size, apple_size)

    if snake_rect.colliderect(apple_rect):
        apple_x = random.randrange(0, cell_count) * cell_size
        apple_y = random.randrange(0, cell_count) * cell_size
        score += 1  
        snake_speed += 1  
        draw_snake

    render_text(f'Score: {score}', (('red')), 10, 10)

    pygame.display.update()

    clock.tick(snake_speed)  
