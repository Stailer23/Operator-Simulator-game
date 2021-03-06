import pygame
import math
import random

window_size_x = 20
window_size_y = 20
cells_size = 36

WIDTH = window_size_x * cells_size + 1
HEIGHT = window_size_y * cells_size + 1
FPS = 30
Level_of_enemy = 1

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
dark_green = (0, 100, 0)
yellow = (255, 255, 0)
pink = (255, 0, 255)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Opeartor_Simulator")
clock = pygame.time.Clock()


def Draw_Window():
    mouse_pos = pygame.mouse.get_pos()
    pos_x = math.floor(mouse_pos[0] / cells_size) * cells_size
    pos_y = math.floor(mouse_pos[1] / cells_size) * cells_size
    pygame.draw.rect(window, dark_green, [pos_x, pos_y, cells_size, cells_size])
    for Line in range(window_size_x + 1):
        pygame.draw.line(window, black, [Line * cells_size, 0], [Line * cells_size, HEIGHT * cells_size])
    for Line in range(window_size_y + 1):
        pygame.draw.line(window, black, [0, Line * cells_size], [WIDTH, Line * cells_size])


class Tower:
    def __init__(self, x, y, size, color, damage, fire_rate, price, radius):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.damage = damage
        self.fire_rate = fire_rate
        self.fire_rate_tick = 0
        self.price = price
        self.radius = radius

    def Draw(self):
        pygame.draw.circle(window, self.color, [self.x, self.y], self.size)

    # def Delete(self, x, y):



class GSM_Tower(Tower):
    def Attacking(self):
        d={}
        for i in range(len(enemies)):
            if enemies[i].color == blue:
                a = Calculating(self.x, self.y, enemies[i].x, enemies[i].y)
                d[i]=a[2]
                for key, val in d.items():
                    if d[key] == min(d.values()):
                            if d[key] <= self.radius:
                                    pygame.draw.line(window, green, [self.x, self.y], [enemies[key].x, enemies[key].y])
                                    enemies[key].health -= 0.3


class UMTS_Tower(Tower):
    def Attacking(self):
        d={}
        for i in range(len(enemies)):
            if enemies[i].color == blue:
                a = Calculating(self.x, self.y, enemies[i].x, enemies[i].y)
                d[i]=a[2]
            for key, val in d.items():
                if d[key] == min(d.values()):
                        if d[key] <= self.radius:
                                pygame.draw.line(window, red, [self.x, self.y], [enemies[key].x, enemies[key].y])
                                enemies[key].health -= 0.7


class LTE_Tower(Tower):
    def Attacking(self):
        d={}
        for i in range(len(enemies)):

            a = Calculating(self.x, self.y, enemies[i].x, enemies[i].y)
            d[i]=a[2]
        for key, val in d.items():
            if d[key] == min(d.values()):
                # for k in range(2):
                    if d[key] <= self.radius:
                        if enemies[key].color == blue:
                            pygame.draw.line(window, yellow, [self.x, self.y], [enemies[key].x, enemies[key].y])
                            enemies[key].health -= 1.2

class Enemy():
    def __init__(self, x, y, Health, speed, size, color, reward):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.health = Health
        self.speed = speed
        self.point = 0
        self.reward = reward

    def Draw(self):
        pygame.draw.circle(window, self.color, [self.x, self.y], self.size)

    def Move(self):
        a = Calculating(self.x, self.y, enemy_points[self.point][0], enemy_points[self.point][1])
        self.x += self.speed * a[0]
        self.y += self.speed * a[1]
        if a[2] <= self.speed:
            self.point += 1
            if self.point == len(enemy_points):
                enemies.remove(self)
                if self.color == blue:
                    player.health-=1

class Player:
    def __init__(self, Money, Health):
        self.money = Money
        self.health = Health

Map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 1, 1, 1, 1, 1, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 1, 1, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 1, 1, 1, 1, 1, 1, 1, 1, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1, 1, 1, 1, 1, 9, 10],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

enemy_way = []
enemy_points = []
towers = []
enemies = []
enemies_good=[]


def Create_enemy_way():
    for i in range(len(Map)):
        for j in range(len(Map[0])):
            if Map[i][j] != 0:
                enemy_way.append([j * cells_size, i * cells_size, cells_size, cells_size])



def Create_enemy_points(points_count):
    point = 2
    for k in range(points_count):
        for i in range(len(Map)):
            for j in range(len(Map[0])):
                if Map[i][j] == point:
                    enemy_points.append([j * cells_size + cells_size / 2, i * cells_size + cells_size / 2])
                    point += 1



def Draw_Enemy_way(color):
    for way in enemy_way:
        pygame.draw.rect(window, color, way)


def Creating_Tower():
    mouse_pos = pygame.mouse.get_pos()
    pos_x = math.floor(mouse_pos[0] / cells_size) * cells_size
    pos_y = math.floor(mouse_pos[1] / cells_size) * cells_size
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1] and Checking_Towers_Building(pos_x, pos_y) and player.money - 10 >= 0:
        towers.append(GSM_Tower(pos_x + cells_size / 2, pos_y + cells_size / 2, 10, green, 5, 0.5, 10, 200))
        player.money -= 10
    if keys[pygame.K_2] and Checking_Towers_Building(pos_x, pos_y) and player.money - 15 >= 0:
        towers.append(UMTS_Tower(pos_x + cells_size / 2, pos_y + cells_size / 2, 10, yellow, 5, 3, 15, 150))
        player.money -= 15
    if keys[pygame.K_3] and Checking_Towers_Building(pos_x, pos_y) and player.money - 20 >= 0:
        towers.append(LTE_Tower(pos_x + cells_size / 2, pos_y + cells_size / 2, 10, red, 0, 3, 20, 100))
        player.money -= 20

cnt = 1
def Creating_Enemy(speed, size, color, reward, cnt):

    for i in range(cnt):

        x = enemy_points[0][0] - 200 - (2*i) * 20 - 5
        y = enemy_points[0][1]
        hp = (Level_of_enemy*0.1) * random.randint(50,3000)
        enemies.append(Enemy(x, y, hp, speed, size, color, reward))

def Checking_Towers_Building(x, y):
    x += cells_size / 2
    y += cells_size / 2
    if len(towers) > 0:
        for tower in towers:
            if tower.x == x and tower.y == y:
                return False
    for way in enemy_way:
        if way[0] + cells_size / 2 == x and way[1] + cells_size / 2 == y:
            return False
    return True


def Checking_enemy_death():
    global Level_of_enemy
    for enemy in enemies:
        if enemy.health <= 0:
            enemies_good.append(enemy)
            enemy.health = 10
            enemy.color = green
            player.money += enemy.reward
            enemy.reward = 0

    if len(enemies) == 0:
        Level_of_enemy += 1
        global cnt
        cnt+=1
        Creating_Enemy(2, 10, blue, 10 * (Level_of_enemy*0.5), cnt)


def Checking_player_death():
    if player.health <= 0:
        global run
        run = False


def Calculating(x1, y1, x2, y2):
    vec_x = x2 - x1
    vec_y = y2 - y1
    dist = math.sqrt(vec_x ** 2 + vec_y ** 2)
    norm_vec_x = vec_x / dist
    norm_vec_y = vec_y / dist
    angle = math.atan2(norm_vec_y, norm_vec_x)
    return norm_vec_x, norm_vec_y, dist, angle


def Main():
    Draw_Window()
    Draw_Enemy_way(dark_green)
    Creating_Tower()
    for tower in towers:
        tower.Draw()
        tower.Attacking()
    for enemy in enemies:
        enemy.Move()
        enemy.Draw()
    Checking_enemy_death()
    Checking_enemy_death()
    Checking_player_death()


f2 = pygame.font.SysFont('serif', 36)

Create_enemy_way()
Create_enemy_points(10)
Creating_Enemy(2, 10, blue, 10, cnt)
player = Player(100, 10)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(black)
    Main()
    money = f2.render(str(player.money), False, yellow)
    health = f2.render(str(player.health), False, red)
    window.blit(money, (10, 10))
    window.blit(health, (10, 40))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()