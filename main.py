import map_data
import pygame

pygame.init()
delivery_sound = pygame.mixer.Sound("C:/Users/Trenton/.spyder-py3/pizzas in peril/data/audio/doorbell.wav")
deliver_image = pygame.image.load("data/images/pizza_delivered.png")
gameIcon = pygame.image.load('data/images/game_icon.png')
level_select_bg = pygame.image.load('data/images/level_select.png')
house_image = pygame.image.load('data/images/house.png')
player_image = pygame.image.load('data/images/pizza_image.png')
pygame.display.set_icon(gameIcon)
death_sound = pygame.mixer.Sound('data/audio/splat.wav')
pygame.mixer.music.load('data/audio/city_sounds.wav')

def main():
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Pizzas in Peril")
    intro_screen = pygame.image.load('data/images/pizza_final.png')
    screen.blit(intro_screen,(0,0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    level_select(screen)
            elif event.type == pygame.QUIT:
                pygame.quit()

def level_select(screen):
    difficulties = ["Easy", "Medium", "Hard"]
    selected_l = 1
    selected_d = 0
    while True: 
        screen.blit(level_select_bg,(0,0))
        font = pygame.font.Font('freesansbold.ttf',85)
        for i in range (1,6):
            if i == selected_l:
                level = font.render(str(i), True, (178,34,34),(30,30,30))       
            else:
                level = font.render(str(i), True, (178,34,34))
            screen.blit(level, (300+(75*i),130))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if selected_l == 1:
                        selected_l = 5
                    else:
                        selected_l-=1
                if event.key == pygame.K_RIGHT:
                    if selected_l == 5:
                        selected_l = 1
                    else:
                        selected_l+=1
                if event.key == pygame.K_1:
                    selected_d = 0
                if event.key == pygame.K_2:
                    selected_d = 1
                if event.key == pygame.K_3:
                    selected_d = 2
                if event.key == pygame.K_SPACE:
                    game(screen, map_data.mazes[selected_l-1], selected_d)
                if event.key == pygame.K_ESCAPE:
                    main()
            elif event.type == pygame.QUIT:
                pygame.quit()
                
        font = pygame.font.Font('freesansbold.ttf',45)
        for i in range (0,3):
            if i == selected_d:
                diff = font.render(difficulties[i], True, (178,34,34), (30,30,30))
            else:
                diff = font.render(difficulties[i], True, (178,34,34))
            screen.blit(diff, (550, 300 + i*50))
        pygame.display.update()

def draw_maze(screen, maze):
    screen.blit(maze['image'],(0,0))
    screen.blit(house_image,(maze['finish']))
    
def get_input():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                return 1
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                return 2
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                return 3
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                return 4
            elif event.key == pygame.K_ESCAPE:
                return 5
        elif event.type == pygame.QUIT:
            pygame.quit()
    return 0

def collision_detect(maze, playerX, playerY, player_size):
    for block in maze['blocks']:
        if (playerX<=block[0]+block[2] and playerX >= block[0]) or (playerX+player_size >= block[0] and playerX+player_size <= (block[0] + block[2])):
            if playerY>= block[1] and playerY<= block[1]+block[3] or (playerY+player_size>= block[1] and playerY+player_size<= block[1]+block[3]):
                delivery_sound.set_volume(.25)
                pygame.mixer.Sound.play(death_sound)
                return True

def finish_detect(maze, playerX, playerY, player_size):
    if (playerX<=maze['finish'][0]+57 and playerX >= maze['finish'][0]) or (playerX+player_size >= maze['finish'][0] and playerX+player_size <= (maze['finish'][0]+57)):
            if playerY>= maze['finish'][1] and playerY<= maze['finish'][1]+53 or (playerY+player_size>= maze['finish'][1] and playerY+player_size<= maze['finish'][1]+53):
                delivery_sound.set_volume(.05)
                pygame.mixer.Sound.play(delivery_sound)
                return True
                
def game(screen,maze,diff):    
    player_size = 22
    playerX = maze['start'][0]
    playerY = maze['start'][1]
    base_vel = 3+ 1.6*diff
    y_velocity = 0
    x_velocity = 0        
    FPS = 60
    fpsClock = pygame.time.Clock()   
    while True:
          
        status = get_input()
        if status == 1: 
            y_velocity = 0
            x_velocity = -1*base_vel
        elif status == 2: 
            y_velocity = base_vel
            x_velocity = 0
        elif status == 3: 
            y_velocity = 0
            x_velocity = base_vel
        elif status == 4: 
            y_velocity = -base_vel
            x_velocity = 0
        elif status == 5:
            level_select(screen)
        playerX = x_velocity + playerX
        playerY = y_velocity + playerY
        draw_maze(screen, maze)
        screen.blit(player_image,(playerX,playerY))
        pygame.display.update()  
        if collision_detect(maze,playerX,playerY,player_size)==True:
            playerX = maze['start'][0]
            playerY = maze['start'][1]
            y_velocity = 0
            x_velocity = 0
            status = 0
        if finish_detect(maze,playerX,playerY,player_size):
            y_velocity = 0
            x_velocity = 0
            screen.blit(deliver_image,(0,0))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            level_select(screen)
                    elif event.type == pygame.QUIT:
                        pygame.quit()
            pygame.quit()
        fpsClock.tick(FPS)    
    
if __name__ == "__main__":
    main()
