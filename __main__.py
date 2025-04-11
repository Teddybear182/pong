import pygame as pg
import sys
import os

#made by Fyodor Belousov

WIDTH, HEIGHT = 600, 400
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_radius = 20
ball_speed = 5

ball_speed_x = ball_speed
ball_speed_y = ball_speed

platform_width = 20
platform_height = 100

left_platform_x = 10
left_platform_y = HEIGHT // 2 - platform_height // 2

right_platform_x = WIDTH - 25
right_platform_y = HEIGHT // 2 - platform_height // 2

white = (255, 255, 255)
black = (0, 0, 0)

pg.init()
pg.font.init()
pg.display.set_caption("Ping Pong")
screen = pg.display.set_mode((WIDTH, HEIGHT))

score_left = 0
score_right = 0

def reset_ball():
  return WIDTH // 2, HEIGHT // 2, ball_speed, ball_speed

while(True):
  pg.time.Clock().tick(60)
  screen.fill(black)
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()
  keys = pg.key.get_pressed()
  if keys[pg.K_w] and left_platform_y > 0:
    left_platform_y -= 5
  if keys[pg.K_s] and left_platform_y < HEIGHT - platform_height:
    left_platform_y += 5
  if keys[pg.K_UP] and right_platform_y > 0:
    right_platform_y -= 5
  if keys[pg.K_DOWN] and right_platform_y < HEIGHT - platform_height:
    right_platform_y += 5
  
  ball_x += ball_speed_x
  ball_y += ball_speed_y

  if (ball_x - ball_radius < left_platform_x and (left_platform_y < ball_y < left_platform_y + platform_height)):
    ball_speed_x = -ball_speed_x
  if (right_platform_x < ball_x + ball_radius < right_platform_x + platform_width and right_platform_y < ball_y + ball_radius < right_platform_y + platform_height):
    ball_speed_x = -ball_speed_x


  if ball_x < 0 or ball_x > WIDTH:
    ball_speed_x = -ball_speed_x

  if ball_y < 0 or ball_y > HEIGHT:
    ball_speed_y = -ball_speed_y

  if ball_x < 0:
    score_right += 1
    ball_x, ball_y, ball_speed_x, ball_speed_y = reset_ball()
  elif ball_x > WIDTH:
    score_left += 1
    ball_x, ball_y, ball_speed_x, ball_speed_y = reset_ball()
  
  pg.draw.rect(screen, white, (left_platform_x, left_platform_y, platform_width, platform_height))
  pg.draw.rect(screen, white, (right_platform_x, right_platform_y, platform_width, platform_height))
  pg.draw.ellipse(screen, white, (ball_x, ball_y, ball_radius, ball_radius))
  screen.blit(pg.font.SysFont("Arial", 30).render(str(score_left), True, white), (WIDTH // 2 - 20, HEIGHT - HEIGHT))
  screen.blit(pg.font.SysFont("Arial", 30).render(str(score_right), True, white), (WIDTH // 2 + 20, HEIGHT - HEIGHT))

  pg.display.flip()
  pg.display.update()
