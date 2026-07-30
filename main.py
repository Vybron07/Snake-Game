import pygame
import sys
import random
import math


pygame.init()

score = 0 
with open("highscore.txt", "r") as file:
    high_score = int(file.read())
new_high_score = False
show_new_high_score = False
high_score_timer = 0
font = pygame.font.SysFont("consolas", 32)
title_font = pygame.font.SysFont("consolas", 48, bold = True)
death_animation = False
death_start_time = 0

# Bonus Food
bonus_food_active = False
bonus_food_x = 0
bonus_food_y = 0
bonus_food_spawn_time = 0
bonus_food_last_spawn = 0
bonus_event_message = ""
bonus_event_timer = 0


WIDTH = 1280
HEIGHT = 720

HUD_HEIGHT = 90
EVENT_BAR_HEIGHT = 60

CELL_SIZE = 20

GAME_WIDTH = WIDTH
GAME_HEIGHT = HEIGHT - HUD_HEIGHT - EVENT_BAR_HEIGHT

GAME_COLS = GAME_WIDTH // CELL_SIZE
GAME_ROWS = GAME_HEIGHT // CELL_SIZE

DIFFICULTIES = {
    "Easy": 9,
    "Medium":6,
    "Hard":3,
}

STARTING_SPEED = DIFFICULTIES["Medium"]
SNAKE_SPEED = STARTING_SPEED
next_speed_threshold = 5

in_menu = True
current_menu = "main"
paused = False
MAIN_MENU = "main"
MENU_SETTINGS = "settings"
MENU_DIFFICULTY = "difficulty"
PAUSE_MENU = "pause"
selected_difficulty = "Medium"

easy_button = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 - 60,300,60)
medium_button = pygame.Rect(WIDTH//2 - 150, HEIGHT//2, 300,60)
hard_button = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 + 60,300,60)
play_button = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 - 40, 300, 60)
settings_button = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 + 30, 300, 60)
quit_button = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 + 100, 300, 60)
difficulty_button = pygame.Rect(WIDTH//2 - 150, 220, 345, 60)
back_button = pygame.Rect(WIDTH//2 - 150, 300, 300, 60)
difficulty_back_button = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 + 140, 300, 60)
resume_button = pygame.Rect(WIDTH//2 - 150, 180, 300, 60)
restart_button = pygame.Rect(WIDTH//2 - 150, 250, 300, 60)
main_menu_button = pygame.Rect(WIDTH//2 - 150, 320, 300, 60)
pause_quit_button = pygame.Rect(WIDTH//2 - 150, 390, 300, 60)



def spawn_food():
    global bonus_food_x
    global bonus_food_y


    while True:
        fx = random.randint(0,(WIDTH//CELL_SIZE) - 1)
        fy = random.randint(0,GAME_ROWS - 1)
        if[fx,fy] not in snake:
            return fx,fy

def spawn_bonus_food():

    global bonus_food_x
    global bonus_food_y

    while True:

        fx = random.randint(0, (WIDTH // CELL_SIZE) - 1)
        fy = random.randint(0, ((HEIGHT - HUD_HEIGHT - EVENT_BAR_HEIGHT) // CELL_SIZE) - 1)

        if [fx, fy] not in snake and (fx != food_x or fy != food_y):
            bonus_food_x = fx
            bonus_food_y = fy
            break


def reset_game():
    global snake,food_x,food_y
    global direction, next_direction,dx,dy
    global score, game_over
    global paused

    global bonus_food_active
    global bonus_food_last_spawn
    global bonus_food_spawn_time
    global bonus_food_x
    global bonus_food_y

    global death_animation 
    global death_start_time

    snake = [
        [32,15],
        [31,15],
        [30,15]
    ]
    food_x, food_y = spawn_food()
    



    direction = "RIGHT"
    next_direction = "RIGHT"

    dx = 1
    dy = 0

    score = 0
    game_over = False
    paused = False

    death_animation = False
    death_start_time = 0



    bonus_food_active = False
    bonus_food_spawn_time = 0
    bonus_food_last_spawn = pygame.time.get_ticks()

    bonus_food_x = -1
    bonus_food_y = -1

    global SNAKE_SPEED
    SNAKE_SPEED = STARTING_SPEED

    global next_speed_threshold 
    next_speed_threshold = 5

    global show_new_high_score

    show_new_high_score = False

def draw_grid():

    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (40,40,40), (x,0), (x,HEIGHT))

    for y in range(HUD_HEIGHT, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (40,40,40), (0,y), (WIDTH,y))

def draw_snake():

    if not snake:
        return 

    for i, block in enumerate(snake):

        if death_animation:
            color = (255,0,0)
        elif i == 0:
            color = (0,180,0)
        else:
            color = (0,255,0)

        pygame.draw.rect(
            screen,
            color,
            (
                block[0] * CELL_SIZE + 1,
                HUD_HEIGHT + block[1] * CELL_SIZE + 1,
                CELL_SIZE - 2,
                CELL_SIZE - 2
            ),
            border_radius = 6
        )

        pygame.draw.circle(
            screen,
            (180,255,180),
            (
                block[0] * CELL_SIZE + 5,
                HUD_HEIGHT + block[1] * CELL_SIZE + 5
            ),
            3
        )

    if not death_animation:

        head_x = snake[0][0] * CELL_SIZE + 1
        head_y = HUD_HEIGHT + snake[0][1] * CELL_SIZE + 1

        if direction == "RIGHT":

            pygame.draw.circle(screen, (255,255,255), (head_x + 14, head_y + 6),2)
            pygame.draw.circle(screen,(255,255,255), (head_x + 14, head_y + 14), 2)
        elif direction == "LEFT":

            pygame.draw.circle(screen, (255,255,255),
                (head_x+4, head_y+6), 2)

            pygame.draw.circle(screen, (255,255,255),
                (head_x+4, head_y+14), 2)

        elif direction == "UP":

            pygame.draw.circle(screen, (255,255,255),
                ( head_x+6, head_y+4), 2)

            pygame.draw.circle(screen, (255,255,255),
                (head_x+14, head_y+4), 2)
        elif direction == "DOWN":

            pygame.draw.circle(screen, (255,255,255),
                (head_x+6, head_y+14), 2)

            pygame.draw.circle(screen, (255,255,255),
                (head_x+14, head_y+14), 2)
        


def draw_food():

    pulse = abs(math.sin(pygame.time.get_ticks() / 150))

    radius = 8  + int(6 * pulse)


    pygame.draw.circle(
        screen,
        (255,0,0),
        (
            food_x * CELL_SIZE + CELL_SIZE//2,
            HUD_HEIGHT + food_y * CELL_SIZE + CELL_SIZE//2,
            
        ),
        radius
    )

def draw_bonus_food():

    if not bonus_food_active:
        return

    radius = CELL_SIZE // 2 + 6 + int(3 * abs(math.sin(pygame.time.get_ticks() / 200)))

    pygame.draw.circle(
        screen,
        (0, 150, 255),
        (
            bonus_food_x * CELL_SIZE + CELL_SIZE // 2,
            HUD_HEIGHT + bonus_food_y * CELL_SIZE + CELL_SIZE // 2
        ),
        radius
    )

def draw_score():

    score_surface = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(score_surface, (10,10))

def draw_hud():
    pygame.draw.rect(screen,(35,35,35),(0,0,WIDTH,HUD_HEIGHT))
    pygame.draw.line(screen,(255,255,255),(0,HUD_HEIGHT),(WIDTH,HUD_HEIGHT),2)
    score_text = (font.render(f"Score:{score}",True,(255,255,255)))

    high_score_text = font.render(
        f"High Score : {high_score}",
        True,
        (255,255,255)
    )
    difficulty_text = font.render(
        f"Difficulty : {selected_difficulty}",
        True,
        (255,255,255)
    )

    pause_text = font.render(
        "ESC : Pause",
        True,
        (255,255,255)
    )

    screen.blit(high_score_text, (20,30))
    screen.blit(score_text,(350,30))
    screen.blit(difficulty_text, (580,30))
    screen.blit(pause_text, (1000,30))

def draw_event_bar():

    pygame.draw.rect(
        screen,
        (35,35,35),
        (0, HEIGHT - EVENT_BAR_HEIGHT, WIDTH, EVENT_BAR_HEIGHT)
    )

    pygame.draw.line(
        screen,
        (255,255,255),
        (0, HEIGHT - EVENT_BAR_HEIGHT),
        (WIDTH, HEIGHT - EVENT_BAR_HEIGHT),
        2
    )


    global bonus_event_message


    if pygame.time.get_ticks() < bonus_event_timer:

        text = font.render(
            bonus_event_message,
            True,
            (255,215,0)
        )

    elif bonus_food_active:

        time_left = max(
            0,
            5 - (pygame.time.get_ticks() - bonus_food_spawn_time)//1000
        )

        text = font.render(
            f" Mighty Berry Active, Disappearing in: {time_left}s",
            True,
            (0,150,255)
        )

    else:

        time_left = max(
            0,
            20 - (pygame.time.get_ticks() - bonus_food_last_spawn)//1000
        )

        text = font.render(
            f"⭐ Mighty Berry Appearing in : {time_left}s",
            True,
            (0,150,255)
        )


    screen.blit(
        text,
        (
            20,
            HEIGHT - EVENT_BAR_HEIGHT + 15
        )
    )

def draw_game_over():

    if game_over:

        over_surface = font.render(
            "Game Over - Press R to Restart",
            True,
            (255,0,0)
        )

        rect = over_surface.get_rect(
            center=(WIDTH//2, HEIGHT//2)
        )

        screen.blit(over_surface, rect)
        if show_new_high_score:

            text = title_font.render(
                " NEW HIGH SCORE!",
                True,
                (255,215,0)
            )

            rect = text.get_rect(
                center=(WIDTH//2, HEIGHT//2 - 60)
            )

            screen.blit(text, rect)

    if not game_over:
        return 

def draw_new_high_score():

    if new_high_score:

        text = font.render(
            "🏆 NEW HIGH SCORE!",
            True,
            (255,215,0)
        )

        rect = text.get_rect(
            center=(WIDTH//2, HEIGHT//2)
        )

        screen.blit(text, rect)

def draw_main_menu():

    title = font.render("SNAKE GAME", True, (255,255,255))
    screen.blit(title, title.get_rect(center=(WIDTH//2, 150)))

    pygame.draw.rect(screen, (60,60,60), play_button)
    pygame.draw.rect(screen, (60,60,60), settings_button)
    pygame.draw.rect(screen, (60,60,60), quit_button)

    play_text = font.render("Play", True, (255,255,255))
    settings_text = font.render("Settings", True, (255,255,255))
    quit_text = font.render("Quit", True, (255,255,255))

    screen.blit(play_text, play_text.get_rect(center=play_button.center))
    screen.blit(settings_text, settings_text.get_rect(center=settings_button.center))
    screen.blit(quit_text, quit_text.get_rect(center=quit_button.center))

def draw_game():
    draw_hud()
    #draw_grid()
    draw_food()
    draw_bonus_food()
    draw_snake()
    draw_event_bar()
    draw_game_over()
    draw_new_high_score()

    #if not bonus_food_active:

        #@time_left = max(
            #0,
            #20 - (pygame.time.get_ticks() - bonus_food_last_spawn) // 1000
        #)

        #timer_text = font.render(
            #f"Next Bonus : {time_left}s",
            #True,
            #(0,150,255)
        #)

        #screen.blit(
            #Timer_text,
            #(
                #WIDTH - timer_text.get_width() - 20,
                #HEIGHT - timer_text.get_height() - 20
            #)
        #)


def draw_menu():

    title_surface = font.render("SNAKE GAME", True, (255,255,255))
    title_rect = title_surface.get_rect(center=(WIDTH//2, HEIGHT//2 - 120))
    screen.blit(title_surface, title_rect)

    pygame.draw.rect(screen, (60,60,60), easy_button)
    pygame.draw.rect(screen, (60,60,60), medium_button)
    pygame.draw.rect(screen, (60,60,60), hard_button)
    pygame.draw.rect(screen, (60,60,60), difficulty_back_button)

    easy_text = font.render("Easy", True, (255,255,255))
    screen.blit(easy_text, easy_text.get_rect(center=easy_button.center))

    medium_text = font.render("Medium", True, (255,255,255))
    screen.blit(medium_text, medium_text.get_rect(center=medium_button.center))

    hard_text = font.render("Hard", True, (255,255,255))
    screen.blit(hard_text, hard_text.get_rect(center=hard_button.center))

    back_text = font.render("Back", True, (255,255,255))
    screen.blit(back_text, back_text.get_rect(center = difficulty_back_button.center))

def draw_settings_menu():

    title = font.render("SETTINGS", True, (255,255,255))
    screen.blit(title, title.get_rect(center=(WIDTH//2,120)))

    

    pygame.draw.rect(screen,(60,60,60),difficulty_button)
    pygame.draw.rect(screen,(60,60,60),back_button)

    difficulty_text = (font.render(f"Difficulty:{selected_difficulty}",True,(255,255,255)))
    screen.blit(difficulty_text, difficulty_text.get_rect(center = difficulty_button.center))
    

    screen.blit(font.render("Back",True,(255,255,255)),
                font.render("Back",True,(255,255,255)).get_rect(center=back_button.center))

def handle_events():
    global running
    global in_menu
    global current_menu
    global STARTING_SPEED
    global next_direction
    global selected_difficulty
    global paused

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if paused and event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = event.pos

            if resume_button.collidepoint(mouse_pos):
                paused = False
                continue

            elif restart_button.collidepoint(mouse_pos):
                reset_game()
                paused = False
                continue

            elif main_menu_button.collidepoint(mouse_pos):
                paused = False
                in_menu = True
                current_menu = MAIN_MENU
                continue

            elif pause_quit_button.collidepoint(mouse_pos):
                running = False
                continue

        if event.type == pygame.MOUSEBUTTONDOWN and in_menu:

            mouse_pos = event.pos

            if current_menu == MAIN_MENU:

            

                if play_button.collidepoint(mouse_pos):
                    in_menu = False
                    reset_game()

                elif settings_button.collidepoint(mouse_pos):
                    current_menu = MENU_SETTINGS

                elif quit_button.collidepoint(mouse_pos):
                    running = False

            elif current_menu == MENU_SETTINGS:

                if difficulty_button.collidepoint(mouse_pos):
                    current_menu = MENU_DIFFICULTY

                elif back_button.collidepoint(mouse_pos):
                    current_menu = MAIN_MENU

            elif current_menu == MENU_DIFFICULTY:

        
                if easy_button.collidepoint(mouse_pos):
                    selected_difficulty = "Easy"
                    STARTING_SPEED = DIFFICULTIES["Easy"]
                    current_menu = MENU_SETTINGS
        
                    
                elif medium_button.collidepoint(mouse_pos):
                    selected_difficulty = "Medium"
                    STARTING_SPEED = DIFFICULTIES["Medium"]
                    current_menu = MENU_SETTINGS

                    
        
                elif hard_button.collidepoint(mouse_pos):
                    selected_difficulty = "Hard"
                    STARTING_SPEED = DIFFICULTIES["Hard"]
                    current_menu = MENU_SETTINGS


                elif difficulty_back_button.collidepoint(mouse_pos):
                    current_menu = MENU_SETTINGS
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE and not in_menu:
                paused = not paused
        
            if event.key == pygame.K_r and game_over:
                reset_game()
        
            if event.key == pygame.K_RIGHT and direction != "LEFT":
                next_direction = "RIGHT"
                        
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                next_direction = "LEFT"
                        
            elif event.key == pygame.K_UP and direction != "DOWN":
                next_direction = "UP"
                        
            elif event.key == pygame.K_DOWN and direction != "UP":
                next_direction = "DOWN"

pygame.time.get_ticks()

#if death_animation:

    #print(current_time - death_start_time)
    #if current_time - death_start_time >= 700:
        #death_animation = False
        #game_over = True


if bonus_food_active:

    if current_time - bonus_food_spawn_time >= 5000:
        bonus_food_active = False

def draw_pause_menu():
    title = font.render("PAUSED", True, (255,255,255)) 
    screen.blit(title, title.get_rect(center = (WIDTH//2, 100)))      

    pygame.draw.rect(screen,(60,60,60), resume_button)
    pygame.draw.rect(screen, (60,60,60), restart_button)
    pygame.draw.rect(screen, (60,60,60), main_menu_button)
    pygame.draw.rect(screen, (60,60,60), pause_quit_button)

    screen.blit(
        font.render("Resume", True, (255,255,255)),
        font.render("Resume", True,(255,255,255)).get_rect(center = resume_button.center)
    )

    screen.blit(
        font.render("Restart", True, (255,255,255)),
        font.render("Restart", True, (255,255,255)).get_rect(center=restart_button.center)
    )

    screen.blit(
        font.render("Main Menu", True, (255,255,255)),
        font.render("Main Menu", True, (255,255,255)).get_rect(center=main_menu_button.center)
    )

    screen.blit(
        font.render("Quit", True, (255,255,255)),
        font.render("Quit", True, (255,255,255)).get_rect(center=pause_quit_button.center)
    )

        

frame_count = 0

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake Game")




clock = pygame.time.Clock()

reset_game()

running = True

while running:


    handle_events()

    current_time = pygame.time.get_ticks()

    if death_animation:

        if current_time - death_start_time >= 700:
            death_animation = False
            #game_over = True


    if not bonus_food_active:

        if current_time - bonus_food_last_spawn >= 20000:
            bonus_food_active = True
            bonus_food_spawn_time = current_time
            bonus_food_last_spawn = current_time
            spawn_bonus_food()

    if bonus_food_active:

        if current_time - bonus_food_spawn_time >= 5000:
            bonus_food_active = False

    
    frame_count += 1

    if (frame_count >= SNAKE_SPEED and not game_over and not paused and not death_animation):

        direction = next_direction

        if direction == "RIGHT":
            dx = 1
            dy = 0

        elif direction == "LEFT":
            dx = -1
            dy = 0

        elif direction == "UP":
            dx = 0
            dy = -1

        elif direction == "DOWN":
            dx = 0
            dy = 1

        head_x = snake[0][0]
        head_y = snake[0][1]

        new_head = [
            head_x + dx,
            head_y + dy
        ]

        #snake.insert(0, new_head)

        #if snake[0]in snake[1:]:
            #death_animation = True
            #death_start_time = pygame.time.get_ticks()

        if (
            new_head[0] < 0 or
            new_head[0] >= GAME_COLS or
            new_head[1] < 0 or
            new_head[1] >= GAME_ROWS
            or new_head in snake
        ):
            death_animation = True
            death_start_time = pygame.time.get_ticks()
            game_over = True

        if death_animation:
            frame_count = 0
            continue

        else:
            snake.insert(0,new_head)
        #if death_animation:
            #frame_count = 0
            #continue

        ate_food = False

        if snake[0][0] == food_x and snake[0][1] == food_y:
            ate_food = True
            score += 1

            food_x,food_y = spawn_food()

        if bonus_food_active:

            if snake[0][0] == bonus_food_x and snake[0][1] == bonus_food_y:
                bonus_food_last_spawn = pygame.time.get_ticks()

                bonus_food_active = False

                score += 5

                for _ in range(5):
                    snake.append(snake[-1][:])

        if score > high_score:
            high_score = score

            with open("highscore.txt", "w") as file:
                file.write(str(high_score))

            show_new_high_score = True
            
            if score >= next_speed_threshold and SNAKE_SPEED > 2:
                SNAKE_SPEED = SNAKE_SPEED * 0.9
                next_speed_threshold *= 2

            food_x, food_y = spawn_food()

        if not ate_food:
            snake.pop()
        frame_count = 0

    screen.fill((0,0,0))


    if in_menu:

        if current_menu == MAIN_MENU:
            draw_main_menu()

        elif current_menu == MENU_SETTINGS:
            draw_settings_menu()
        elif current_menu == MENU_DIFFICULTY:
            draw_menu()

    else:

        draw_game()

        if paused:
            draw_pause_menu()

    # Hide the message after 2 seconds
    if new_high_score:

        if pygame.time.get_ticks() - high_score_timer > 2000:
            new_high_score = False

        
    pygame.display.flip()

    


    clock.tick(60)


pygame.quit()
sys.exit()
