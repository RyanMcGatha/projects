
import pygame, random # import pygame and random modules

pygame.init() # Initialize Pygame

# Set up display
cell_size = 40 # sets size of cells to 40px

cell_count = 20 #sets width of display winjdow to 20 cells wide 

screen = pygame.display.set_mode((cell_size * cell_count, cell_size * cell_count))# main game window       (width,height)
# ^ there can only be one display surface. is seprate from element surfaces. is displayed by default 

background_image = pygame.image.load("sean.png") # loads image file to br displayed (does not display until)

background_image = pygame.transform.scale(background_image, (cell_size * cell_count, cell_size * cell_count)) # displays image  file 

pygame.mixer.music.load("homept2.mp3") # loads audio file to be played (does not play until called)

pygame.mixer.music.play(-1) # plays audio file 
        #(loops infinitly)^

clock = pygame.time.Clock() # renaming fps control for easier use 

caption = pygame.display.set_caption('Seans Serpent') # caption for main display window 

font = pygame.font.Font(None, 36)  # sets font style and size 

white = (255, 255, 255) #renaming for easier use 

# scoreboard setup
def render_text(text, color, x, y):
    score_text = font.render(text, True, color)
    screen.blit(score_text, (x, y))

def draw_snake():
    snake_x -= 40
    pygame.draw.rect(screen, white, (snake_x, snake_y, snake_size, snake_size))


# Snake setup
snake_size = 40
snake_speed = 10 
snake_x = 200
snake_y = 250
snake_direction = "RIGHT"

# Apple setup
apple_size = 40
apple_x = random.randrange(0, cell_count) * cell_size #sets the x position to be random
apple_y = random.randrange(0, cell_count) * cell_size # sets the y position to be random

score = 0 # init scoreboard


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #when usr clicks x on main display
            pygame.quit()
            running = False

        # snake movement
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN" and snake_y > 0:
                snake_direction = "UP"# only allows up if snake is not going down

            elif event.key == pygame.K_DOWN and snake_direction != "UP" and snake_y < (cell_count - 1) * cell_size:
                snake_direction = "DOWN"# only allows down if snake is not going up

            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT" and snake_x > 0:
                snake_direction = "LEFT"# only allows left if snake ia not going right 

            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT" and snake_x < (cell_count - 1) * cell_size:
                snake_direction = "RIGHT"#only allows right if snake is not going left 

    # user input
    if snake_direction == "UP":
        snake_y -= cell_size # subtracts 40px from snakes y position 
    elif snake_direction == "DOWN":
        snake_y += cell_size  # adds 40px to snakes y position
    elif snake_direction == "LEFT": 
        snake_x -= cell_size   # subtracts 40px from snakes x position
    elif snake_direction == "RIGHT":
        snake_x += cell_size  # adds 40px to snakes x position 
   
    # Check for collision with borders
    if ( #defines borders 
        snake_x < 0
        or snake_x >= cell_count * cell_size
        or snake_y < 0
        or snake_y >= cell_count * cell_size
    ):
        # Snake hit the border = reset game 
        snake_x = 200
        snake_y = 250
        snake_direction = "RIGHT"
        score = 0 
        snake_speed = 10 

    # Draw background image
    screen.blit(background_image, (0, 0))

    # Draw grid lines
    for x in range(0, cell_count * cell_size, cell_size):
        pygame.draw.line(screen, white, (x, 0), (x, cell_count * cell_size))
    for y in range(0, cell_count * cell_size, cell_size):
        pygame.draw.line(screen, white, (0, y), (cell_count * cell_size, y))

    # Draw snake
    pygame.draw.rect(screen, white, (snake_x, snake_y, snake_size, snake_size))

    # Draw apple
    pygame.draw.rect(screen, (255, 0, 0), (apple_x, apple_y, apple_size, apple_size))

    # Check for snake-apple collision
    snake_rect = pygame.Rect(snake_x, snake_y, snake_size, snake_size)
    apple_rect = pygame.Rect(apple_x, apple_y, apple_size, apple_size)

    # Snake has collided with apple
    if snake_rect.colliderect(apple_rect):
        apple_x = random.randrange(0, cell_count) * cell_size
        apple_y = random.randrange(0, cell_count) * cell_size
        score += 1  
        snake_speed += 1  
        pygame.draw.rect(screen, white, (snake_x, snake_y, snake_size, snake_size))


    # Render and display score
    render_text(f'Score: {score}', (('red')), 10, 10)

    # Update the display
    pygame.display.update()

    # set fps to snake speed
    clock.tick(snake_speed)  
