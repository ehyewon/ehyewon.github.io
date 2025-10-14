import tkinter as tk
from PIL import ImageTk, Image

def key_press(event):
    if event.keysym == 'space':
        start_game()

root = tk.Tk()
root.title("Game Start")

window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

frame = tk.Frame(root)
frame.pack(pady=50)

image = Image.open("start_image.png")
image = image.resize((500, 300), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(frame, image=photo)
image_label.pack()

text_label = tk.Label(frame, text="Press Space Bar to Start", font=("Arial", 24))
text_label.pack(pady=60)

def key_press(event):
    if event.keysym == 'space':
        root.destroy()

root.bind("<space>", key_press)

root.mainloop()

import pygame
import random
import os

pygame.init()

score = 0
FPS = 60
clock = pygame.time.Clock()


screenWidth = 1300
screenHeight = 700
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Kill the Monster")

background1 = pygame.image.load("tree.png")
background2 = pygame.image.load("castle.png")
background3 = pygame.image.load("hell.png")
background4 = pygame.image.load("python.png")
background_list = [background1, background2, background3, background4]
current_background = 0

character = pygame.image.load("hi.png")
character_size = character.get_rect().size
character_right = pygame.image.load("hi.png")
character_left = pygame.transform.flip(character_right, True, False)
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screenWidth / 2) - (character_width / 6)
character_y_pos = screenHeight - character_height

monster1 = pygame.image.load("slime1.png")
monster2 = pygame.image.load("slime2.png")
monster3 = pygame.image.load("slime3.png")
monster_list = [monster1, monster2, monster3]
monsters = []
monster4 = pygame.image.load("iron.png")
monster5 = pygame.image.load("devil.png")
monster6 = pygame.image.load("hong.png")


bullet = pygame.image.load("bullet.png")
bullet_width = 40  
bullet_height = 20  
bullet = pygame.transform.scale(bullet, (bullet_width, bullet_height))
bullet_x_pos = 0
bullet_y_pos = 0
bullet_speed = 10
bullet_state = "ready"

font_path = os.path.join("폰트_파일_경로.ttf")

pygame.font.init()
game_font = pygame.font.Font(font_path, 36)

life = 3
life_text = game_font.render("Life: {}".format(life), True, (255, 255, 255))
life_text_rect = life_text.get_rect()
life_text_rect.topleft = (10, 10)

def render_life_text():
    life_text = game_font.render("Life: {}".format(life), True, (255, 255, 255))
    life_text_rect = life_text.get_rect()
    life_text_rect.topleft = (10, 10)
    screen.blit(life_text, life_text_rect)

    
character_speed = 5
character_jump = False
jump_count = 12


spawn_interval = 3000  
last_spawn_time = pygame.time.get_ticks()  
monster_count1 = 0  
monster_count2 = 0
monster_count3 = 0
monster_count4 = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    if character_x_pos > screenWidth and monster_count1 >= 10:
        character_x_pos = -character_width
        current_background = (current_background + 1) % len(background_list)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if character_x_pos > 0:  
            character_x_pos -= character_speed
            character = character_left  

    if keys[pygame.K_RIGHT]:
        character_x_pos += character_speed
        character = character_right  

    if keys[pygame.K_UP] and not character_jump:
        character_jump = True

    if keys[pygame.K_SPACE]:
        if bullet_state == "ready":
            bullet_x_pos = character_x_pos + character_width / 2 - bullet_width / 2
            bullet_y_pos = character_y_pos + character_height / 2 - bullet_height / 2
            bullet_state = "fire"
            if keys[pygame.K_LEFT]:
                bullet_speed = -15
            else:
                bullet_speed = 15

    if character_jump:
        if jump_count >= -12:
            neg = 1
            if jump_count < 0:
                neg = -1
            character_y_pos -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            character_jump = False
            jump_count = 12
            
    current_time = pygame.time.get_ticks()

    

    if current_background == 0 and monster_count1 < 10 and current_time - last_spawn_time > spawn_interval:
        last_spawn_time = current_time
        monster_x_pos = screenWidth
        monster_y_pos = screenHeight - monster1.get_height()  
        monster = {
            "image": random.choice(monster_list),
            "x": monster_x_pos,
            "y": monster_y_pos,
            "speed": random.randint(4, 6),
            "collision_count": 0
        }
        monsters.append(monster)
        monster_count1 += 1

        

    if current_background == 1 and monster_count2 < 5 and current_time - last_spawn_time > spawn_interval:
        last_spawn_time = current_time
        monster_x_pos = screenWidth
        monster_y_pos = screenHeight - monster4.get_height() 
        monster = {
            "image": monster4,
            "x": monster_x_pos,
            "y": monster_y_pos,
            "speed":random.randint(2, 6),
            "collision_count": 0
        }
        monsters.append(monster)
        monster_count2 += 1

    if current_background == 2 and monster_count3 < 3 and current_time - last_spawn_time > spawn_interval:
        last_spawn_time = current_time
        monster_x_pos = screenWidth
        monster_y_pos = screenHeight - monster5.get_height() 
        monster = {
            "image": monster5,
            "x": monster_x_pos,
            "y": monster_y_pos,
            "speed": random.randint(2, 6),
            "collision_count": 0
        }
        monsters.append(monster)
        monster_count3 += 1
        
    if current_background == 3 and monster_count4 < 1 and current_time - last_spawn_time > spawn_interval:
        last_spawn_time = current_time
        monster_x_pos = screenWidth
        monster_y_pos = screenHeight - monster6.get_height()  
        monster = { 
        "image": monster6,
        "x": monster_x_pos,
        "y": monster_y_pos,
        "speed": 2,
        "collision_count": 0
        }
        monsters.append(monster)
        monster_count4 += 1


    clock.tick(FPS)

    screen.blit(background_list[current_background], (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))

    for monster in monsters:
        screen.blit(monster["image"], (monster["x"], monster["y"]))

        monster["x"] -= monster["speed"]

        if monster["x"] + monster["image"].get_width() < 0 or monster["x"] > screenWidth:
            monster["x"] = screenWidth

    for monster in monsters:
        screen.blit(monster["image"], (monster["x"], monster["y"]))
        monster["x"] -= monster["speed"]
        if monster["x"] + monster["image"].get_width() < 0 or monster["x"] > screenWidth:
            monster["x"] = screenWidth


        monster_rect = pygame.Rect(monster["x"], monster["y"], monster["image"].get_width(), monster["image"].get_height())
        bullet_rect = pygame.Rect(bullet_x_pos, bullet_y_pos, bullet_width, bullet_height)
        if monster_rect.colliderect(bullet_rect):
            monster["collision_count"] += 1
            if current_background == 0 and monster["collision_count"] >= 2:
                monsters.remove(monster)
            elif current_background == 1 and monster["collision_count"] >= 5:
                monsters.remove(monster)
            elif current_background == 2 and monster["collision_count"] >= 9:
                monsters.remove(monster)
            elif current_background == 3 and monster["collision_count"] >= 300:
                monsters.remove(monster)
                game_over_image = pygame.image.load("youwin.png")
                screen.blit(game_over_image, (0, 0))
                pygame.display.flip()
            bullet_state = "ready"
            bullet_x_pos = 0  
            bullet_y_pos = 0  
    if bullet_state == "fire":
        screen.blit(bullet, (bullet_x_pos, bullet_y_pos))
        bullet_x_pos += bullet_speed
        if bullet_x_pos > screenWidth or bullet_x_pos < 0:
            bullet_state = "ready"


    character_rect = pygame.Rect(character_x_pos, character_y_pos, character_width, character_height)
    collision = False  
    for monster in monsters:
        monster_rect = pygame.Rect(monster["x"], monster["y"], monster["image"].get_width(), monster["image"].get_height())
        if character_rect.colliderect(monster_rect):
            collision = True
            break

    render_life_text()  

         
    
    if collision:
        life -= 1
        if life == 0:
            game_over_image = pygame.image.load("gameover.png")
            screen.blit(game_over_image, (0, 0))
            pygame.display.flip()
            pygame.time.delay(2000)  
            running = False  
        else:
            character_x_pos = (screenWidth / 2) - (character_width / 6)  
            if current_background == 3:  
                for monster in monsters:
                     if monster["image"] == monster6:
                        monster["x"] = screenWidth  
            else:
                monsters.clear()  
            


    life_text_surface = game_font.render("Life: {}".format(life), True, (255, 255, 255)) # 목숨 텍스트 렌더링
    screen.blit(life_text_surface, (10, 10))  


    pygame.display.flip()

    

pygame.quit()
