import pygame
import random
import json
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer for sound

# Game Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BASE_TIME_LIMIT = 20  # Base time limit in seconds

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
plane_img = pygame.image.load("plane-Photoroom.png")
meteorite_img = pygame.image.load("meteorite-Photoroom.png")
gun_img = pygame.image.load("gune-Photoroom.png")
background_img = pygame.image.load("eart.jpg")

# Load sounds
shoot_sound = pygame.mixer.Sound("burst fire.mp3")
explosion_sound = pygame.mixer.Sound("rumble.flac")

# Resize images
plane_img = pygame.transform.scale(plane_img, (80, 80))
meteorite_img = pygame.transform.scale(meteorite_img, (50, 50))
gun_img = pygame.transform.scale(gun_img, (20, 40))
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyber Shooter - Time Attack")

# Fonts
font = pygame.font.Font(None, 36)

# Leaderboard file
LEADERBOARD_FILE = "leaderboard.json"

def get_player_name():
    name = ""  # ตัวแปรสำหรับเก็บชื่อผู้เล่น
    input_active = True  # ใช้ตรวจสอบว่าอยู่ในโหมดการป้อนข้อมูลหรือไม่
    while input_active:
        screen.fill(BLACK)  # เติมพื้นหลังให้เป็นสีดำ
        text = font.render(f"Enter Name: {name}", True, WHITE)  # แสดงข้อความให้ผู้เล่นกรอกชื่อ
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))  # วางข้อความตรงกลาง
        pygame.display.flip()  # อัพเดตหน้าจอ
        for event in pygame.event.get():  # ตรวจสอบเหตุการณ์ที่เกิดขึ้น
            if event.type == pygame.QUIT:  # ถ้าผู้เล่นปิดหน้าต่าง
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:  # ถ้ามีการกดปุ่ม
                if event.key == pygame.K_RETURN and name:  # ถ้ากด Enter และมีการกรอกชื่อแล้ว
                    return name  # ส่งคืนชื่อที่กรอก
                elif event.key == pygame.K_BACKSPACE:  # ถ้ากด Backspace
                    name = name[:-1]  # ลบตัวอักษรสุดท้าย
                else:
                    name += event.unicode  # เพิ่มตัวอักษรใหม่ที่ผู้เล่นกรอก

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = plane_img  # กำหนดภาพของผู้เล่น
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))  # กำหนดตำแหน่งของผู้เล่น
        self.speed = 5  # ความเร็วในการเคลื่อนที่
        self.fire_rate = 1  # อัตราการยิง
        self.shield = 0  # จำนวนเกราะของผู้เล่น
    
    def update(self):
        keys = pygame.key.get_pressed()  # ตรวจสอบปุ่มที่ถูกกด
        if keys[pygame.K_LEFT] and self.rect.left > 0:  # ถ้ากดปุ่มซ้ายและไม่เกินขอบซ้าย
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:  # ถ้ากดปุ่มขวาและไม่เกินขอบขวา
            self.rect.x += self.speed

class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = meteorite_img  # กำหนดภาพของกล่อง
        self.rect = self.image.get_rect(topleft=(x, y))  # กำหนดตำแหน่งของกล่อง

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = gun_img  # กำหนดภาพของกระสุน
        self.rect = self.image.get_rect(center=(x, y))  # กำหนดตำแหน่งเริ่มต้นของกระสุน
        self.speed = -7  # ความเร็วของกระสุน
    
    def update(self):
        self.rect.y += self.speed  # เคลื่อนที่กระสุนขึ้น
        if self.rect.bottom < 0:  # ถ้ากระสุนไปถึงขอบบนของหน้าจอ
            self.kill()  # ลบกระสุน

# Initialize upgrade levels
upgrade_levels = {
    "Speed Up": 0,
    "Bullet Size Up": 0,
    "Fire Rate Up": 0,
    "Extra Life": 0,
    "Shield": 0
}

def upgrade_menu():
    upgrades = ["Speed Up", "Bullet Size Up", "Fire Rate Up", "Extra Life", "Shield"]  # รายการการอัปเกรด
    selected = 0  # เลือกตัวเลือกแรก
    while True:
        screen.fill(BLACK)  # เติมพื้นหลังเป็นสีดำ
        for i, upgrade in enumerate(upgrades):  # วนลูปรายการอัปเกรด
            color = WHITE if i == selected else (100, 100, 100)  # เลือกสีสำหรับตัวเลือกที่เลือก
            text = font.render(f"{upgrade} (Level {upgrade_levels[upgrade]})", True, color)  # สร้างข้อความอัปเกรดพร้อมระดับ
            screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 + i * 40))  # แสดงข้อความบนหน้าจอ
        pygame.display.flip()  # อัพเดตหน้าจอ
        for event in pygame.event.get():  # ตรวจสอบเหตุการณ์ที่เกิดขึ้น
            if event.type == pygame.QUIT:  # ถ้าผู้เล่นปิดหน้าต่าง
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:  # ถ้ามีการกดปุ่ม
                if event.key == pygame.K_UP:  # ถ้ากดปุ่มลูกศรขึ้น
                    selected = (selected - 1) % len(upgrades)  # เลือกตัวเลือกก่อนหน้า
                elif event.key == pygame.K_DOWN:  # ถ้ากดปุ่มลูกศรลง
                    selected = (selected + 1) % len(upgrades)  # เลือกตัวเลือกถัดไป
                elif event.key == pygame.K_RETURN:  # ถ้ากด Enter
                    return upgrades[selected]  # ส่งคืนตัวเลือกที่เลือก

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            return json.load(file)
    return []

def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file)

def display_leaderboard(leaderboard, player_name, player_score):
    screen.fill(BLACK)
    title_text = font.render("Leaderboard", True, WHITE)
    screen.blit(title_text, (WIDTH // 2 - 100, 50))
    
    leaderboard.append((player_name, player_score))
    leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)[:10]
    save_leaderboard(leaderboard)
    
    for i, (name, score) in enumerate(leaderboard):
        text = font.render(f"{i + 1}. {name}: {score}", True, WHITE)
        screen.blit(text, (WIDTH // 2 - 100, 100 + i * 30))
    
    pygame.display.flip()
    pygame.time.wait(5000)  # Wait for 5 seconds before closing

def main():
    player_name = get_player_name()  # รับชื่อผู้เล่น
    clock = pygame.time.Clock()  # สร้างอ็อบเจกต์นาฬิกา
    running = True  # สถานะเกมกำลังดำเนินการ
    score = 0  # คะแนนเริ่มต้น
    level = 1  # เลเวลเริ่มต้น
    upgrades_taken = 0  # จำนวนการอัปเกรดที่เลือก
    time_left = BASE_TIME_LIMIT * FPS  # เวลาที่เหลือ (เป็นจำนวนเฟรม)
    player = Player()  # สร้างตัวละครผู้เล่น
    all_sprites = pygame.sprite.Group()  # กลุ่มของสปรายต์ทั้งหมด
    bullets = pygame.sprite.Group()  # กลุ่มของกระสุน
    boxes = pygame.sprite.Group()  # กลุ่มของกล่อง
    all_sprites.add(player)  # เพิ่มผู้เล่นในกลุ่มสปรายต์ทั้งหมด
    
    def spawn_boxes():
        boxes.empty()  # ลบกล่องเก่าทั้งหมด
        num_boxes = 5 + level * 2  # เพิ่มจำนวนกล่องตามเลเวล
        for _ in range(num_boxes):  # สร้างกล่องใหม่ตามเลเวล
            box = Box(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT // 2))
            boxes.add(box)  # เพิ่มกล่องในกลุ่ม
            all_sprites.add(box)  # เพิ่มกล่องในกลุ่มสปรายต์ทั้งหมด
        return num_boxes
    
    num_boxes = spawn_boxes()  # สร้างกล่องใหม่
    
    while running:
        clock.tick(FPS)  # กำหนดอัตราเฟรม
        for event in pygame.event.get():  # ตรวจสอบเหตุการณ์ที่เกิดขึ้น
            if event.type == pygame.QUIT:  # ถ้าผู้เล่นปิดหน้าต่าง
                running = False
            elif event.type == pygame.KEYDOWN:  # ถ้ามีการกดปุ่ม
                if event.key == pygame.K_SPACE:  # ถ้ากด Spacebar
                    bullet = Bullet(player.rect.centerx, player.rect.top)  # สร้างกระสุน
                    bullets.add(bullet)  # เพิ่มกระสุนในกลุ่ม
                    all_sprites.add(bullet)  # เพิ่มกระสุนในกลุ่มสปรายต์ทั้งหมด
                    shoot_sound.play()  # เล่นเสียงยิง
                elif event.key == pygame.K_r and time_left <= 0:  # ถ้ากด R หลังจากที่เวลาหมด
                    main()  # เริ่มเกมใหม่
                    return
        all_sprites.update()  # อัพเดตตำแหน่งของสปรายต์
        
        for bullet in bullets:  # สำหรับกระสุนแต่ละตัว
            hits = pygame.sprite.spritecollide(bullet, boxes, True)  # ตรวจสอบการชนกับกล่อง
            for hit in hits:
                score += 10  # เพิ่มคะแนน
                bullet.kill()  # ลบกระสุน
                explosion_sound.play()  # เล่นเสียงระเบิด
        
        if not boxes:  # ถ้าไม่มีกล่องแล้ว
            level += 1  # เพิ่มเลเวล
            upgrades_taken += 1  # เพิ่มจำนวนการอัปเกรด
            upgrade = upgrade_menu()  # แสดงเมนูการอัปเกรด
            upgrade_levels[upgrade] += 1  # เพิ่มระดับการอัปเกรด
            if upgrade == "Speed Up":
                player.speed += 1  # เพิ่มความเร็วผู้เล่น
            elif upgrade == "Bullet Size Up":
                Bullet.image = pygame.transform.scale(gun_img, (30, 60))  # เพิ่มขนาดกระสุน
            elif upgrade == "Fire Rate Up":
                player.fire_rate += 1  # เพิ่มอัตราการยิง
            elif upgrade == "Extra Life":
                time_left += 10 * FPS  # เพิ่มเวลา
            elif upgrade == "Shield":
                player.shield += 1  # เพิ่มเกราะ
            time_left = BASE_TIME_LIMIT * FPS + num_boxes * 2 * FPS  # รีเซ็ตเวลาโดยเพิ่มตามจำนวนกล่อง
            num_boxes = spawn_boxes()  # สร้างกล่องใหม่
        
        time_left -= 1  # ลดเวลาลง
        screen.blit(background_img, (0, 0))  # วางภาพพื้นหลัง
        all_sprites.draw(screen)  # วาดสปรายต์ทั้งหมด
        
        # แสดงข้อความต่างๆ บนหน้าจอ
        score_text = font.render(f"{player_name} Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        time_text = font.render(f"Time: {max(0, time_left // FPS)}", True, WHITE)
        screen.blit(time_text, (WIDTH - 120, 10))
        level_text = font.render(f"Level: {level}", True, WHITE)
        screen.blit(level_text, (WIDTH // 2 - 50, 10))
        upgrade_text = font.render(f"Upgrades Taken: {upgrades_taken}", True, WHITE)
        screen.blit(upgrade_text, (WIDTH // 2 - 50, 40))
        
        if time_left <= 0:  # ถ้าเวลาหมด
            game_over_text = font.render(f"Game Over! Score: {score} (Press R to Restart)", True, WHITE)
            screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2))  # แสดงข้อความ Game Over
            pygame.display.flip()  # อัพเดตหน้าจอ
            pygame.time.wait(2000)  # Wait for 2 seconds before showing leaderboard
            leaderboard = load_leaderboard()
            display_leaderboard(leaderboard, player_name, score)
            running = False
        
        pygame.display.flip()  # อัพเดตหน้าจอ
    
    pygame.quit()  # ปิด pygame

if __name__ == "__main__":
    main()  # เรียกใช้ฟังก์ชันหลัก
