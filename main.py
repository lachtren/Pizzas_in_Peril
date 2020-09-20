import pygame
import time

pygame.init()
delivery_sound = pygame.mixer.Sound("C:/Users/Trenton/.spyder-py3/pizzas in peril/sounds/doorbell.wav")
deliver_image = pygame.image.load("C:/Users/Trenton/.spyder-py3/pizzas in peril/images/pizza_delivered.png")
gameIcon = pygame.image.load('C:/Users/Trenton/.spyder-py3/pizzas in peril/images/game_icon.png')
level_select_bg = pygame.image.load('C:/Users/Trenton/.spyder-py3/pizzas in peril/images/level_select.png')
level_5_bg = pygame.image.load('C:/Users/Trenton/.spyder-py3/pizzas in peril/images/level_5.png')
level_4_bg = pygame.image.load('C:/Users/Trenton/.spyder-py3/pizzas in peril/images/level_4.png')
level_1_bg = pygame.image.load('C:/Users/Trenton/.spyder-py3/pizzas in peril/images/level_1.png')
level_2_bg = pygame.image.load('C:/Users/Trenton/.spyder-py3/pizzas in peril/images/level_2.png')
house_image = pygame.image.load('C:/Users/Trenton/.spyder-py3/pizzas in peril/images/house.png')
player_image = pygame.image.load('C:/Users/Trenton/.spyder-py3/pizzas in peril/images/pizza_image.png')
pygame.display.set_icon(gameIcon)
death_sound = pygame.mixer.Sound('C:/Users/Trenton/.spyder-py3/pizzas in peril/sounds/splat.wav')
pygame.mixer.music.load('C:/Users/Trenton/.spyder-py3/pizzas in peril/sounds/city_sounds.wav')


mazes = [
    {'blocks':[(0, 440, 320, 160)
    ,(480, 440, 320, 160)
    ,(320, 560, 160, 40)
    ,(0, 0, 40, 440)
    ,(40, 0, 760, 40)
    ,(760, 40, 40, 560)
    ,(80, 360, 280, 40)
    ,(440, 360, 280, 40)
    ,(80, 80, 40, 60)
    ,(80, 280, 40, 80)
    ,(680, 80, 40, 60)
    ,(600, 280, 120, 80)
    ,(120, 80, 200, 40)
    ,(480, 80, 200, 40)
    ,(280, 120, 40, 40)
    ,(480, 120, 40, 40)
    ,(360, 200, 80, 40)
    ,(440, 280, 40, 40)
    ,(320, 120, 160, 40)
    ,(320, 280, 40, 40)
    ,(120, 280, 80, 80)
    ,(240, 120, 40, 40)
    ,(80, 80, 200, 80)
    ,(80, 200, 200, 40)
    ,(240, 280, 120, 40)
    ,(240,200,80,80)
    ,(40,200,40,40)
    ,(440, 120, 280, 40)
    ,(480, 200, 240, 40)
    ,(480, 240, 80, 80)
    ,(720, 200, 40, 40)
    ,(360,360,80,40)
             ],
         'start': (390,500),
         'finish': (370,50),
         'image': level_1_bg
         },
    {'blocks':[(0, 440, 320, 160)
    ,(480, 440, 320, 160)
    ,(320, 560, 160, 40)
    ,(0, 0, 40, 440)
    ,(40, 0, 760, 40)
    ,(760, 40, 40, 560)
    ,(80, 360, 280, 40)
    ,(440, 360, 280, 40)
    ,(80, 80, 40, 160)
    ,(80, 280, 40, 80)
    ,(680, 80, 40, 160)
    ,(600, 280, 120, 80)
    ,(120, 80, 200, 40)
    ,(480, 80, 200, 40)
    ,(280, 120, 40, 200)
    ,(480, 120, 40, 200)
    ,(360, 200, 80, 40)
    ,(440, 280, 40, 40)
    ,(320, 120, 160, 40)
    ,(320, 280, 40, 40)
    ,(120, 280, 80, 80)
    ,(240, 120, 40, 200)
    ,(120, 120, 120, 120)
    ,(520, 120, 160, 120)
    ,(520, 240, 40, 80)
             ],
         'start': (390,500),
         'finish': (370,50),
         'image': level_2_bg
     
     },
    {
     },
    {'blocks':[(0, 0, 40, 600)
    ,(40, 0, 600, 40)
    ,(120, 0, 40, 120)
    ,(80, 80, 40, 40)
    ,(0, 240, 120, 40)
    ,(80, 160, 80, 40)
    ,(80, 320, 120, 40)
    ,(160, 280, 40, 40)
    ,(80, 400, 120, 40)
    ,(160, 440, 120, 40)
    ,(240, 480, 40, 40)
    ,(160, 480, 40, 120)
    ,(0, 560, 800, 40)
    ,(760, 80, 40, 480)
    ,(720, 80, 40, 40)
    ,(320, 440, 80, 80)
    ,(240, 320, 40, 80)
    ,(200, 200, 40, 80)
    ,(240, 240, 120, 40)
    ,(320, 280, 40, 120)
    ,(360, 360, 80, 40)
    ,(320, 40, 40, 160)
    ,(280, 120, 40, 80)
    ,(240, 80, 40, 80)
    ,(200, 120, 40, 40)
    ,(440, 480, 40, 80)
    ,(480, 520, 120, 40)
    ,(400, 240, 40, 80)
    ,(400, 80, 40, 120)
    ,(440, 80, 40, 40)
    ,(520, 80, 40, 80)
    ,(560, 120, 40, 40)
    ,(480, 160, 40, 80)
    ,(520, 200, 80, 40)
    ,(480, 280, 80, 40)
    ,(480, 320, 40, 40)
    ,(480, 360, 200, 40)
    ,(440, 400, 80, 40)
    ,(520, 440, 40, 40)
    ,(640, 400, 40, 40)
    ,(600, 440, 120, 40)
    ,(640, 480, 40, 40)
    ,(720, 520, 40, 40)
    ,(600, 40, 40, 80)
    ,(640, 80, 40, 120)
    ,(680, 160, 40, 160)
    ,(640, 240, 40, 80)
    ,(600, 280, 40, 40)
    ,(720, 360, 40, 40)],
         'start': (50,500),
         'finish': (730,15),
         'image': level_4_bg
         },
    { 'blocks':[(0, 0, 800, 40),
    (0, 40, 40, 600),
    (40,560,760,40),
    (140,100,40,460),
    (40,410,50,30),
    (90,300,50,30),
    (40,40,50,200),
    (240,40,40,480),
    (340,420,40,140),
    (280,320,400,40),
    (450,360,40,150),
    (550,420,40,140),
    (640,360,40,150),
    (760,0,40,560),
    (325, 225, 500, 40),
    (280, 140, 380, 40),
    (520, 40, 40, 100)
        ],
         'start': (50,520),
         'finish': (570,80),
         'image': level_5_bg
     }
         
         ]

def main():
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Pizzas in Peril")
    intro_screen = pygame.image.load('C:/Users/Trenton/.spyder-py3/pizzas in peril/images/pizza_final.png')
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
                    game(screen, mazes[selected_l-1], selected_d)
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
    base_vel = 1.5+ .8*diff
    y_velocity = 0
    x_velocity = 0        
    
    while True:
        FPS = 120
        fpsClock = pygame.time.Clock()
        
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
        fpsClock.tick(FPS)    
    
if __name__ == "__main__":
    main()
