# Sky Scaper is a fast-paced endless 2D sidescrolling platformer 
# where you flip the gravity to land on buildings and dash through
# obstacles. Survive to gain more points. Game and Music By Brian Liu

import simplegui
import random
import math


# Image URLs =======================================================================================================================================

PLAYER_RUNNING_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/852231553772814397/adventurer-Sheet_2.png")
PLAYER_RUNNING_IMG_PRIME = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/852242187788746772/adventurer-Sheet_1_1.png")
PLAYER_JUMPING_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/852238679388323910/adventurer-Sheet_3.png")
PLAYER_DASH_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/852295974033686549/adventurer-Sheet_4.png")
TRASH_IMG = simplegui.load_image("https://www.pngix.com/pngfile/big/99-992611_garbage-png-pile-of-trash-png-transparent-png.png")
BKGD_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/849399454800150548/Untitled_3.jpg")
BOXES_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/854041374155341855/istockphoto-813979758-612x612_1.png")
BOXES_IMG_PRIME = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/854042283490017280/istockphoto-813979758-612x612_2.png")
APARTMENT1_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/847685332601929728/1192932Fn8bvQXa_3.png")
APARTMENT2_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/844972406127853639/971c5c04c4d6e24379e4cd9d87c3c318.png")
APARTMENT3_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/849327433923821618/2d5yxil94ctz_1_1.png")
APARTMENT4_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/851877591899308052/pixel-art-house-background-games-design-59174865_3.png")
APARTMENT1_IMG_PRIME = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/849326987780947968/1192932Fn8bvQXa_4.png")
APARTMENT2_IMG_PRIME = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/849395510950363196/971c5c04c4d6e24379e4cd9d87c3c318_1_1.png")
APARTMENT3_IMG_PRIME = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/849347095226875904/2d5yxil94ctz_1_1_1.png")
APARTMENT4_IMG_PRIME = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/851876596322795560/pixel-art-house-background-games-design-59174865_2.png")
SPAWN_BUILDING_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/849700262217777162/971c5c04c4d6e24379e4cd9d87c3c318_2_2.png")


CONSTRUCTION_BARRIER_IMG = simplegui.load_image("https://www.searchpng.com/wp-content/uploads/2018/12/under-construction-png-715x206.png")
CONSTRUCTION_BARRIER_IMG_PRIME = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/852956484865228830/under-construction-png-715x206.png")

TITLE_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/853474434647588884/Untitled.png")
PLAY_BUTTON_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/854756531664977940/resized-image-Promo_1.jpeg")
CONTROLS_BUTTON_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/854757097945694238/resized-image-Promo_3.jpeg")
ABOUT_BUTTON_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/854760450875719700/resized-image-Promo_6.jpeg")
ABOUT_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/855118136448516146/Untitled_7.png")
PLAY_AGAIN_BUTTOM_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/853733066014064660/Untitled_7.jpg")

DEATH_SCREEN_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/854402497363181608/Untitled_9.jpg")
HOME_BUTTON_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/854609781493858314/Untitled_11.jpg")
CONTROLS_IMG = simplegui.load_image("https://cdn.discordapp.com/attachments/676641018665238539/854606816679428097/Untitled_3.png")

# Game Music =================================================================================================================

GAME_MUSIC = simplegui.load_sound("https://cdn.discordapp.com/attachments/676641018665238539/1193059477092573234/71322_BeepBox-Song.mp3?ex=65ab5639&is=6598e139&hm=f9bbb918c1c7db0158e520517ecefa641c7466e0261f4b9e8ca6e2ade7eb4d1b&")
MENU_MUSIC = simplegui.load_sound("https://cdn.discordapp.com/attachments/676641018665238539/854852629741568000/mix_4m27s_audio-joiner.com_1.mp3")
DEATH_MUSIC = simplegui.load_sound("https://cdn.discordapp.com/attachments/676641018665238539/854864479149096970/BeepBox-Song_7.mp3")


# IMG File dictionary  =======================================================================================================
COLS = 6
ROWS = 1

IMGS = {TITLE_IMG:[510,141],
        PLAY_BUTTON_IMG:[350,85],
        CONTROLS_BUTTON_IMG:[350,85],
        PLAY_AGAIN_BUTTOM_IMG:[450,110],
        ABOUT_BUTTON_IMG:[350,85],
        ABOUT_IMG:[1300,744],
        PLAYER_RUNNING_IMG:[[300/COLS/2,28/ROWS/2],[300/COLS,28/ROWS]],
        PLAYER_RUNNING_IMG_PRIME:[[300/COLS/2,28/ROWS/2],[300/COLS,28/ROWS]],
        PLAYER_JUMPING_IMG:[[200/4/2,31/ROWS/2],[300/4,31/ROWS]],
        PLAYER_DASH_IMG:[[200/8,17/2],[200/4,16/1]],
        BKGD_IMG:[2600,744],
        TRASH_IMG:[399,180],
        APARTMENT1_IMG:[378,280],
        APARTMENT2_IMG:[292,90],
        APARTMENT3_IMG:[100,189],
        APARTMENT4_IMG:[754,729],
        APARTMENT1_IMG_PRIME:[378,280],
        APARTMENT2_IMG_PRIME:[292,90],
        APARTMENT3_IMG_PRIME:[100,189],
        APARTMENT4_IMG_PRIME:[754,729],
        SPAWN_BUILDING_IMG:[349,148],
        CONSTRUCTION_BARRIER_IMG:[715,206],
        CONSTRUCTION_BARRIER_IMG_PRIME:[715,200],
        BOXES_IMG:[496,290],
        BOXES_IMG_PRIME:[496,290],
        HOME_BUTTON_IMG:[100,100],
        DEATH_SCREEN_IMG:[1300,744],
        CONTROLS_IMG:[1300,744]}
        

# Global Variables =========================================================================================================
    
    
#Canvas size
FRAME_WIDTH = 1300
FRAME_HEIGHT = 744
#Size of player on canvas
PLAYER_SIZE = [80,60]
PLAYER_SPEED = 2
#Background
BKGD_WIDTH = 2600
BKGD_HEIGHT = 744

background_pos = [0, BKGD_HEIGHT/2]


CENTER = 372
GRAVITY = .6
DASH_DISTANCE = 300

player_location = [200,620]
trash_list = []
building_list = []
obstacles_list = []

building_up = True

time = 0

current_points = 0
OBSTACLE_POINTS = 200


MENU = 0
GAME = 1
DEATH = 2
CONTROLS = 3
ABOUT = 4
# Default Game State
game_state = MENU
# game_state = 1 In Game


# Helper functions ========================================================================================================
def new_game():
    global player, spawn_apartment, spawn_apartment2, game_state, scroll_speed, building_up, time, music
    game_state = GAME
    
    time = 0
    
    scroll_speed = 14.5
    player = Character(PLAYER_RUNNING_IMG, PLAYER_SIZE,[200,600])
    spawn_apartment = Shaped_Building(SPAWN_BUILDING_IMG,[900,315],[600,590],IMGS[SPAWN_BUILDING_IMG],692,754)
    spawn_apartment2 = Building(APARTMENT4_IMG_PRIME,[400,300],[1450,0],IMGS[APARTMENT4_IMG_PRIME])
    # Ingame music
    GAME_MUSIC.rewind()
    GAME_MUSIC.play()
    
    for building in building_list:
            building_list.remove(building)
    for obstacle in obstacles_list:
            obstacles_list.remove(obstacle)
    
    building_up = True
    game_state == 1
# Checks if something is offscreen
def offscreen(pos):
    off = False
    if pos[0] < -500 :
        off = True
    if pos[1] < 0 :
        off = True
    return off

def collision_surface(building):
    player.falling = False
    if player.pos[1] > 372:
       player.pos[1] = building.top - player.height
       player.vel[1] = 0
    elif player.pos[1] < 372:
       player.pos[1] = building.bottom + player.height
       player.vel[1] = 0
        
def character_animation(COLS, ROWS):
    center1 = IMGS[PLAYER_RUNNING_IMG][0]
    width,height = IMGS[PLAYER_RUNNING_IMG][1]
    col = math.floor(player.time%COLS)
    row = 0
    tile_center = [center1[0] + col*width,
                  center1[1] + row*height]
def spawn_button():
    global play, controls, play_again, home, about
    play = Button(PLAY_BUTTON_IMG, [FRAME_WIDTH/2, 350], IMGS[PLAY_BUTTON_IMG][0],IMGS[PLAY_BUTTON_IMG][1])
    controls = Button(CONTROLS_BUTTON_IMG, [FRAME_WIDTH/2, 463], IMGS[CONTROLS_BUTTON_IMG][0],IMGS[CONTROLS_BUTTON_IMG][1])
    play_again = Button(PLAY_AGAIN_BUTTOM_IMG, [FRAME_WIDTH/2, 500], IMGS[PLAY_AGAIN_BUTTOM_IMG][0],IMGS[PLAY_AGAIN_BUTTOM_IMG][1])
    home = Button(HOME_BUTTON_IMG, [1220, 664], IMGS[HOME_BUTTON_IMG][0],IMGS[HOME_BUTTON_IMG][1])
    about = Button(ABOUT_BUTTON_IMG, [FRAME_WIDTH/2, 570], IMGS[ABOUT_BUTTON_IMG][0],IMGS[ABOUT_BUTTON_IMG][1])

# Classes ========================================================================================
class Character:
    
    def __init__(self, image, size, pos):
        self.img = image
        self.animated = True
        self.time = 0
        self.size = size
        self.pos = pos
        self.vel = [0,0]
       
        
        self.JUMP_SPEED = 27
        self.DASH_SPEED = 30
        self.time = 0
        self.hp = 3
        self.falling = True
        self.dashing = False
        self.dashtime = 0
        self.points = 0
        
    def draw(self, canvas):
        
        self.width = self.size[0]/2
        self.height = self.size[1]/2
        
        if self.animated:
            
            if self.pos[1] > 372:
                center1 = IMGS[PLAYER_RUNNING_IMG][0]
                width,height = IMGS[PLAYER_RUNNING_IMG][1]
                col = math.floor(self.time%COLS)
                row = 0
                tile_center = [center1[0] + col*width,
                            center1[1] + row*height]
                canvas.draw_image(PLAYER_RUNNING_IMG,
                                tile_center, 
                                IMGS[PLAYER_RUNNING_IMG][1],
                                self.pos, 
                                self.size)
                
                
            elif self.pos[1] < 372:
                center1 = IMGS[PLAYER_RUNNING_IMG_PRIME][0]
                width,height = IMGS[PLAYER_RUNNING_IMG_PRIME][1]
                col = math.floor(self.time%COLS)
                row = 0
                tile_center = [center1[0] + col*width,
                            center1[1] + row*height]
                canvas.draw_image(PLAYER_RUNNING_IMG_PRIME,
                                tile_center, 
                                IMGS[PLAYER_RUNNING_IMG_PRIME][1],
                                self.pos, 
                                self.size)
            
            
    def update(self):
        
        if self.animated: 
            self.time += .2
            
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        # Player Gravity
        if self.falling:
            if self.pos[1] > CENTER:			
                self.vel[1] += GRAVITY
            elif self.pos[1] < CENTER:
                self.vel[1] -= GRAVITY
            if self.pos[1] >= 744: #Back to ground
                self.vel[1] = 0
            if self.pos[1] < 10:
                self.vel[1] = 0
                
        # Player Dash Counter
        if self.dashing:
            self.dashtime += 1
                
        # Player Dash Return
        
        if self.pos[0] >= DASH_DISTANCE:
                self.dashing = False
                self.vel[0] -= 10    
        if self.pos[0] <= player_location[0]:
                self.dashing = False
                self.vel[0] = 0
                self.pos[0] = player_location[0]
                self.dashtime = 0
               
        
        self.left = self.pos[0] - self.size[0]/2
        self.right = self.pos[0] + self.size[0]/2
        self.top = self.pos[1] - self.size[1]/2
        self.bottom = self.pos[1] + self.size[1]/2
        
        
    # Character Jump        
    def jump(self):
        if not self.falling:
            if self.pos[1] > CENTER:
                self.vel[1] = -self.JUMP_SPEED
            elif self.pos[1] < CENTER:
                self.vel[1] = self.JUMP_SPEED
                
    # Character Dash        
    def dash(self):
        if self.pos[0] <= player_location[0] and not self.dashing and not self.falling:
            self.dashing = True
            self.vel[0] += self.DASH_SPEED
            
            
    # Checks if has collided
    def has_collided(self, other):
        in_width = self.right >= other.left #self.left - other.size[0]/2 <= other.pos[0] and other.pos[0] <= self.right + other.size[0]/2
        in_height = self.bottom >= other.top #self.top - other.size[1]/2 <= other.pos[1] <= self.bottom + other.size[1]/2
        return in_width and in_height

    #side collision
    def has_collided_side(self, building):
        next_x = self.right - building.vel[0]
        in_x = self.right <= building.left <= next_x
        in_y = self.bottom  >= building.top and self.top <= building.bottom
        return in_x and in_y
    
    # Checks if has collided with top
    def has_collided_top(self, building):
        next_y = self.bottom + self.vel[1]
        in_x = self.left - building.size[0]/2 <= building.pos[0] and building.pos[0] <= self.right + building.size[0]/2
        in_y = self.bottom <= building.top and building.top <= next_y
        return in_x and in_y
    
    # Checks if has collided with Bottom
    def has_collided_bot(self, building):
        next_y = self.top + self.vel[1]
        in_x = self.left - building.size[0]/2 <= building.pos[0] and building.pos[0] <= self.right + building.size[0]/2
        in_y = self.top >= building.bottom and building.bottom >= next_y 
        return in_x and in_y
    
# Obstacle Class    
class Obstacle:
    def __init__(self, image, size, position, original_size):
        self.img = image
        self.size = size
        self.pos = position
        self.vel = [-scroll_speed,0]
        self.og = original_size
        self.width = self.size[0]/2
        self.height = self.size[1]/2
        
        
    def draw(self, canvas):
        canvas.draw_image(self.img,
                          [self.og[0]/2,self.og[1]/2],
                          [self.og[0],self.og[1]],
                          self.pos,
                          self.size)
        
    def update(self):
        self.pos[0] += self.vel[0]
        self.left = self.pos[0] - self.size[0] / 2
        self.right = self.pos[0] + self.size[0] / 2
        self.top = self.pos[1] - self.size[1] / 2
        self.bottom = self.pos[1] + self.size[1] / 2


    
# Building Class        

class Building:
    def __init__(self, image, size, position, original_size):
        self.img = image
        self.size = size
        self.pos = position
        self.vel = [-scroll_speed,0]
        self.og = original_size
        self.width = self.size[0]/2
        self.height = self.size[1]/2
        
    def draw(self, canvas):
        canvas.draw_image(self.img, 
                          [self.og[0]/2,self.og[1]/2], 
                          [self.og[0],self.og[1]], 
                          self.pos, 
                          self.size)
             
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        
        self.left = self.pos[0] - self.size[0] / 2
        self.right = self.pos[0] + self.size[0] / 2
        self.top = self.pos[1] - self.size[1] / 2
        self.bottom = self.pos[1] + self.size[1] / 2

# Shaped Buildings Class        
class Shaped_Building:
    def __init__(self, image, size, position, original_size, top, bottom):
        self.img = image
        self.size = size
        self.pos = position
        self.vel = [-scroll_speed,0]
        self.og = original_size
        self.top = top
        self.bottom = bottom
        
    def draw(self, canvas):
        canvas.draw_image(self.img, 
                          [self.og[0]/2,self.og[1]/2], 
                          [self.og[0],self.og[1]], 
                          self.pos, 
                          self.size)    
        
        self.left = self.pos[0] - self.size[0]/2
        self.right = self.pos[0] + self.size[0]/2
        self.top = self.top
        self.bottom = self.bottom
        self.width = self.bottom - self.pos[1]
        self.height = self.pos[1] - self.top

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]    
        self.left += self.vel[0]
        self.right += self.vel[0]
        
class Button:
    def __init__(self, image, location, width, height):
        self.image = image
        self.pos = location
        self.width = width
        self.height = height
        
    def draw(self, canvas):
        canvas.draw_image(self.image, 
                          (self.width/2, self.height/2), 
                          (self.width, self.height),
                          self.pos,
                          (self.width, self.height))
        
    def is_selected(self, mouse_pos):
        left = self.pos[0] - self.width/2
        right = self.pos[0] + self.width/2
        top = self.pos[1] - self.height/2
        bottom = self.pos[1] + self.height/2
        in_x = mouse_pos[0] >= left and mouse_pos[0] <= right
        in_y = mouse_pos[1] >= top and mouse_pos[1] <= bottom
        return in_x and in_y    
        
        
# Handler to draw on canvas
def draw(canvas):
    global game_state, current_points, building_up, time, scroll_speed
    
    if game_state == MENU:
        
        MENU_MUSIC.play()
        canvas.draw_image(BKGD_IMG,
                     [BKGD_WIDTH/2,BKGD_HEIGHT/2],
                     [BKGD_WIDTH, BKGD_HEIGHT],
                     background_pos,
                     [BKGD_WIDTH, BKGD_HEIGHT])
    
        background_pos[0] += -5
        background_pos[0] %= BKGD_WIDTH/2
        
        canvas.draw_image(TITLE_IMG,
                     [IMGS[TITLE_IMG][0]/2,IMGS[TITLE_IMG][1]/2],
                     IMGS[TITLE_IMG],
                     [640,200],
                     IMGS[TITLE_IMG])
        
        # Homescreen Buttons
        play.draw(canvas)
        controls.draw(canvas)
        about.draw(canvas)
        
        
    if game_state == CONTROLS:
        
        canvas.draw_image(BKGD_IMG,
                     [BKGD_WIDTH/2,BKGD_HEIGHT/2],
                     [BKGD_WIDTH, BKGD_HEIGHT],
                     background_pos,
                     [BKGD_WIDTH, BKGD_HEIGHT])
        background_pos[0] += -5
        background_pos[0] %= BKGD_WIDTH/2
        
        canvas.draw_image(CONTROLS_IMG,
                     [FRAME_WIDTH/2,FRAME_HEIGHT/2],
                     [FRAME_WIDTH,FRAME_HEIGHT],
                     [FRAME_WIDTH/2,FRAME_HEIGHT/2],
                     [FRAME_WIDTH,FRAME_HEIGHT])
        
        home.draw(canvas)
        
    if game_state ==  ABOUT:
        
        canvas.draw_image(BKGD_IMG,
                     [BKGD_WIDTH/2,BKGD_HEIGHT/2],
                     [BKGD_WIDTH, BKGD_HEIGHT],
                     background_pos,
                     [BKGD_WIDTH, BKGD_HEIGHT])
        
        background_pos[0] += -5
        background_pos[0] %= BKGD_WIDTH/2
        
        canvas.draw_image(ABOUT_IMG,
                     [FRAME_WIDTH/2,FRAME_HEIGHT/2],
                     [FRAME_WIDTH,FRAME_HEIGHT],
                     [FRAME_WIDTH/2,FRAME_HEIGHT/2],
                     [FRAME_WIDTH,FRAME_HEIGHT])
        
        home.draw(canvas)
        
    
    if game_state == GAME:
        MENU_MUSIC.pause()
        time += 1
        player.points += (2)
    # Scrolling Background
        scroll_speed += 0.0005
        canvas.draw_image(BKGD_IMG,
                         [BKGD_WIDTH/2,BKGD_HEIGHT/2],
                         [BKGD_WIDTH, BKGD_HEIGHT],
                         background_pos,
                         [BKGD_WIDTH, BKGD_HEIGHT])

        background_pos[0] += -scroll_speed
        background_pos[0] %= BKGD_WIDTH/2
        

        player.update()
        if time >= 30:
            if time % 33 == 0:
                # All of the buildings
                apartment1 = Building(APARTMENT1_IMG, [350,130], [1500,700],IMGS[APARTMENT1_IMG])
                apartment2 = Shaped_Building(APARTMENT2_IMG,[700,130],[1600,690],IMGS[APARTMENT2_IMG],704,754)
                apartment3 = Building(APARTMENT3_IMG,[300,270],[1500,710],IMGS[APARTMENT3_IMG])
                apartment4 = Building(APARTMENT4_IMG,[500,300],[1650,744],IMGS[APARTMENT4_IMG])
                apartment1prime = Building(APARTMENT1_IMG_PRIME, [350,130], [1500,44], IMGS[APARTMENT1_IMG_PRIME])
                apartment2prime = Shaped_Building(APARTMENT2_IMG_PRIME, [700,130],[1600,54], IMGS[APARTMENT2_IMG_PRIME], -10,40)
                apartment3prime = Building(APARTMENT3_IMG_PRIME, [300,270], [1500,34], IMGS[APARTMENT3_IMG_PRIME])
                apartment4prime = Building(APARTMENT4_IMG_PRIME,[500,300],[1650,0],IMGS[APARTMENT4_IMG_PRIME])

                apartments_list_up = [apartment1, apartment2, apartment3, apartment4]
                apartments_list_down = [apartment1prime,apartment2prime, apartment3prime,apartment4prime]
                # Order of spawning 
                if building_up == True:
                    apartment = random.choice(apartments_list_up)
                    building_list.append(apartment)
                    building_up = False

                elif building_up == False:
                    apartment = random.choice(apartments_list_down)
                    building_list.append(apartment)
                    building_up = True


        # Spawning Apartment Location
        
        spawn_apartment.draw(canvas)
        spawn_apartment.update()   
        spawn_apartment2.draw(canvas)
        spawn_apartment2.update()

        
        player.falling = True       
        for building in building_list:
                 
            building.draw(canvas)
            building.update()
            
            if isinstance(building, Shaped_Building):
                if time % 25 == 0:
                    if building.pos[0] >= 1100:
                        spawn_area = random.randrange(100,150)
                        construction_barrier = Obstacle(CONSTRUCTION_BARRIER_IMG, [140,30],[building.pos[0] + spawn_area ,building.top - 15], IMGS[CONSTRUCTION_BARRIER_IMG])
                        construction_barrier_prime = Obstacle(CONSTRUCTION_BARRIER_IMG_PRIME, [140,30],[building.pos[0] + spawn_area ,building.bottom + 15], IMGS[CONSTRUCTION_BARRIER_IMG_PRIME])
                        boxes = Obstacle(BOXES_IMG, [200,70],[building.pos[0] + spawn_area , building.top - 35], IMGS[BOXES_IMG])
                        boxes_prime = Obstacle(BOXES_IMG_PRIME, [200,70],[building.pos[0] + spawn_area , building.bottom + 35], IMGS[BOXES_IMG_PRIME])
                        obstacle_list = [construction_barrier,construction_barrier_prime, boxes, boxes_prime]
                        obstacle = random.choice(obstacle_list)
                        obstacles_list.append(obstacle) 
                               
            if player.has_collided_top(building):
                collision_surface(building)
            if player.has_collided_bot(building):
                collision_surface(building)
            if player.has_collided_side(building):
                game_state = 2
                
        for building in building_list:
            if offscreen(building.pos):
                building_list.remove(building)
                
        if player.has_collided_top(spawn_apartment):
            collision_surface(spawn_apartment)
        if player.has_collided_bot(spawn_apartment2):
            collision_surface(spawn_apartment2)
        if player.has_collided_side(spawn_apartment2):
                game_state = 2

        if player.pos[1] <= 17 or player.pos[1] >= 743:
            player.vel[1] = 0
            game_state = 2
        
        for obstacle in obstacles_list:
                obstacle.draw(canvas)
                obstacle.update()
                if offscreen(obstacle.pos):
                    obstacles_list.remove(obstacle)
                if player.has_collided(obstacle) :
                    if 0 < player.dashtime and player.dashtime < 4:
                        obstacles_list.remove(obstacle)
                        player.points += OBSTACLE_POINTS
                    else:
                        game_state = DEATH
        # Obstacle spawning


        player.draw(canvas)
        
        if (player.points//1) % 10 == 0:
            current_points = player.points
        canvas.draw_text('Score: ' + str(current_points), (40, 50), 30, 'White')
        
        
    if game_state == DEATH:
        
        GAME_MUSIC.pause()
        
        DEATH_MUSIC.play()
        
        for building in building_list:
            building_list.remove(building)
        for obstacle in obstacles_list:
            obstacles_list.remove(obstacle)
        
        canvas.draw_image(DEATH_SCREEN_IMG,
                     [FRAME_WIDTH/2,FRAME_HEIGHT/2],
                     [FRAME_WIDTH,FRAME_HEIGHT],
                     [FRAME_WIDTH/2,FRAME_HEIGHT/2],
                     [FRAME_WIDTH,FRAME_HEIGHT])
        
        play_again.draw(canvas)
        home.draw(canvas)
        
        canvas.draw_text('Score: ' + str(current_points), (550, 400), 50, 'White')
    # Death Screen
            
# Mouse Handler    
def mouse_click(mouse_position):
    global game_state
    if game_state == MENU:   
        if play.is_selected(mouse_position):
            new_game()
        if controls.is_selected(mouse_position):
            game_state = CONTROLS
        if about.is_selected(mouse_position):
            game_state = ABOUT
            
    if game_state == CONTROLS  or game_state == ABOUT:
        if home.is_selected(mouse_position):
            game_state = MENU
            
            MENU_MUSIC.play()
            GAME_MUSIC.pause()
    if game_state == DEATH:
        if home.is_selected(mouse_position):
            game_state = MENU
            DEATH_MUSIC.rewind()
            MENU_MUSIC.rewind()
            MENU_MUSIC.play()
            GAME_MUSIC.pause()
        
    if game_state == DEATH:
        if play_again.is_selected(mouse_position):
            DEATH_MUSIC.rewind()
            new_game()
            game_state = GAME

#Handler for when keyboard key is pressed    
def key_down(key):
    if key == simplegui.KEY_MAP['space']:
        player.jump()
    if key == simplegui.KEY_MAP['d']:
        player.dash()

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Sky Scaper", FRAME_WIDTH, FRAME_HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)

frame.set_mouseclick_handler(mouse_click)
frame.set_canvas_background("white")
# Start the frame animation
spawn_button()
frame.start()
