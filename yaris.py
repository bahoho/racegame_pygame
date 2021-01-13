import random
import time
import pygame
import sys
from pygame.locals import *

pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
score_color = (139, 189, 139)
time.sleep(1)
font = pygame.font.Font('freesansbold.ttf', 32)
font_sort = pygame.font.Font('freesansbold.ttf', 24)
font_standings = pygame.font.Font('freesansbold.ttf', 64)
font_averagespeed = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Formula', True, white, (139, 148, 116))
background = pygame.image.load("Background.png")
font = pygame.font.SysFont(None, 20)
screen = pygame.display.set_mode((1500, 650))
pygame.display.set_caption("Race Game")
icon = pygame.image.load('wheel.png')
pygame.display.set_icon(icon)
mainClock = pygame.time.Clock()
car2 = pygame.image.load('pitstop_car_3.png')
car4 = pygame.image.load('pitstop_car_4.png')
car5 = pygame.image.load('pitstop_car_5.png')
car6 = pygame.image.load('pitstop_car_6.png')
car7 = pygame.image.load('pitstop_car_7.png')
car9 = pygame.image.load('pitstop_car_9.png')
car10 = pygame.image.load('pitstop_car_10.png')
car11 = pygame.image.load('pitstop_car_11.png')
car12 = pygame.image.load('pitstop_car_12.png')
car13 = pygame.image.load('pitstop_car_13.png')
car14 = pygame.image.load('pitstop_car_14.png')
car15 = pygame.image.load('pitstop_car_15.png')
car16 = pygame.image.load('safetycar.png')
light_start = pygame.image.load('light_start.png')
light_1 = pygame.image.load('light_1.png')
light_2 = pygame.image.load('light_2.png')
light_3 = pygame.image.load('light_3.png')
light_4 = pygame.image.load('light_4.png')
light_5 = pygame.image.load('light_5.png')
f1_back = pygame.image.load('f1_back.png')
pygame.mixer.music.load('startsound.mp3')

running = True


def lights(light_x, light_y):
    screen.blit(f1_back, (0, 0))
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(0)
    pygame.display.update()
    screen.blit(light_1, (light_x, light_y))
    time.sleep(1)
    pygame.display.update()
    screen.blit(light_2, (light_x, light_y))
    time.sleep(1)
    pygame.display.update()
    screen.blit(light_3, (light_x, light_y))
    time.sleep(1)
    pygame.display.update()
    screen.blit(light_4, (light_x, light_y))
    time.sleep(1)
    pygame.display.update()
    screen.blit(light_5, (light_x, light_y))
    time.sleep(1)
    pygame.display.update()
    screen.blit(light_start, (light_x, light_y))
    time.sleep(1)
    pygame.display.update()


def main_menu():
    start = 0
    start = time.process_time()
    lights(1250, 1)
    car1X = car2X = car4X = car5X = car6X = car7X = car9X = car10X = car11X = car12X = car13X = car14X = car15X = 50
    car16X = 0
    carY = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 700, 325]
    backgroundX = 0

    def show_score(x, y):
        standings = font_standings.render("Standings", True, (108, 174, 117))
        screen.blit(standings, (1150, 50))
        score1 = font_standings.render("1. " + str(score_value1), True, score_color)
        screen.blit(score1, (x, y))
        score2 = font_standings.render("2. " + str(score_value2), True, score_color)
        screen.blit(score2, (x, y + 50))
        score3 = font_standings.render("3. " + str(score_value3), True, score_color)
        screen.blit(score3, (x, y + 100))
        score4 = font_standings.render("4. " + str(score_value4), True, score_color)
        screen.blit(score4, (x, y + 150))
        score5 = font_standings.render("5. " + str(score_value5), True, score_color)
        screen.blit(score5, (x, y + 200))
        score6 = font_standings.render("6. " + str(score_value6), True, score_color)
        screen.blit(score6, (x, y + 250))
        average = font_averagespeed.render("Leader average speed: " + str(average_value / 3), True, (193, 204, 153))
        screen.blit(average, (x - 100, y + 350))
        sayac = font_averagespeed.render("Leader time : " + str(time.process_time() - start), True, (245, 166, 91))
        screen.blit(sayac, (x - 100, y + 400))

        team1 = font_sort.render("1.", True, score_color)
        screen.blit(team1, (0, carY[0] + 10))
        team1 = font_sort.render("2.", True, score_color)
        screen.blit(team1, (0, carY[1] + 10))
        team1 = font_sort.render("3.", True, score_color)
        screen.blit(team1, (0, carY[2] + 10))
        team1 = font_sort.render("4.", True, score_color)
        screen.blit(team1, (0, carY[3] + 10))
        team1 = font_sort.render("5.", True, score_color)
        screen.blit(team1, (0, carY[4] + 10))
        team1 = font_sort.render("6.", True, score_color)
        screen.blit(team1, (0, carY[5] + 10))
        team1 = font_sort.render("7.", True, score_color)
        screen.blit(team1, (0, carY[6] + 10))
        team1 = font_sort.render("8.", True, score_color)
        screen.blit(team1, (0, carY[7] + 10))
        team1 = font_sort.render("9.", True, score_color)
        screen.blit(team1, (0, carY[8] + 10))
        team1 = font_sort.render("10.", True, score_color)
        screen.blit(team1, (0, carY[9] + 10))
        team1 = font_sort.render("11.", True, score_color)
        screen.blit(team1, (0, carY[10] + 10))
        team1 = font_sort.render("12.", True, score_color)
        screen.blit(team1, (0, carY[11] + 10))

    while True:

        screen.blit(background, (backgroundX, 0))
        screen.blit(text, (350, 500))
        screen.blit(car2, (car2X, carY[0]))
        screen.blit(car4, (car4X, carY[1]))
        screen.blit(car5, (car5X, carY[2]))
        screen.blit(car6, (car6X, carY[3]))
        screen.blit(car7, (car7X, carY[4]))
        screen.blit(car9, (car9X, carY[5]))
        screen.blit(car10, (car10X, carY[6]))
        screen.blit(car11, (car11X, carY[7]))
        screen.blit(car12, (car12X, carY[8]))
        screen.blit(car13, (car13X, carY[9]))
        screen.blit(car14, (car14X, carY[10]))
        screen.blit(car15, (car15X, carY[11]))
        screen.blit(car16, (car16X, carY[12]))

        if 0 <= car1X <= 1200:
            car1X_change = random.uniform(0.001, 5)
            car1X += car1X_change
            backgroundX -= car1X_change
        if 0 <= car2X <= 1200:
            car2X_change = random.uniform(0.001, 5)
            car2X += car2X_change
        if 0 <= car4X <= 1200:
            car4X_change = random.uniform(0.001, 5)
            car4X += car4X_change
        if 0 <= car5X <= 1200:
            car5X_change = random.uniform(0.001, 5)
            car5X += car5X_change
        if 0 <= car6X <= 1200:
            car6X_change = random.uniform(0.001, 5)
            car6X += car6X_change
        if 0 <= car7X <= 1200:
            car7X_change = random.uniform(0.001, 5)
            car7X += car7X_change
        if 0 <= car9X <= 1200:
            car9X_change = random.uniform(0.001, 5)
            car9X += car9X_change
        if 0 <= car10X <= 1200:
            car10X_change = random.uniform(0.001, 5)
            car10X += car10X_change
        if 0 <= car11X <= 1200:
            car11X_change = random.uniform(0.001, 5)
            car11X += car11X_change
        if 0 <= car12X <= 1200:
            car12X_change = random.uniform(0.001, 5)
            car12X += car12X_change
        if 0 <= car13X <= 1200:
            car13X_change = random.uniform(0.001, 5)
            car13X += car13X_change
        if 0 <= car14X <= 1200:
            car14X_change = random.uniform(0.001, 5)
            car14X += car14X_change
        if 0 <= car15X <= 1450:  # fastest car for timing
            car15X_change = random.uniform(3, 5)
            car15X += car15X_change
        if 0 <= car16X <= 1200:  # medical car
            car16X_change = random.uniform(0.001, 1)
            car16X += car16X_change
        if car15X >= 1360:
            time.sleep(2)
            return main_menu()

        cars = {"1.Team": car1X, "2.Team": car2X, "4.Team": car4X, "5.Team": car5X, "6.Team": car6X,
                "7.Team": car7X, "9.Team": car9X, "10.Team": car10X, "11.Team": car11X, "12.Team": car12X,
                "13.Team": car13X, "14.Team": car14X, "Safety Car": car16X}

        a = dict(enumerate(sorted(cars, key=lambda x: int(cars[x]), reverse=True), 1))
        b = list(a.values())

        topspeed = sorted(
            [car1X, car2X, car4X, car5X, car6X, car7X, car9X, car10X, car11X, car12X, car13X, car14X, car15X,
             car16X])
        topspeed_new = topspeed
        score_value1 = b[0]
        score_value2 = b[1]
        score_value3 = b[2]
        score_value4 = b[3]
        score_value5 = b[4]
        score_value6 = b[5]
        average_value = topspeed_new[0]
        show_score(1150, 150)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        mainClock.tick(60)


main_menu()
