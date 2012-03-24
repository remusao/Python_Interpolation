import pygame
import functools

SCREEN_WIDTH = 1640
SCREEN_HEIGHT = 980

def lagrange(points, x):

  res = 0.0

  for i in xrange(0, len(points)):
    tmp = float(points[i][1])
    try:
      for j in xrange(0, len(points)):
        if i == j:
          continue
        tmp *= float(x - points[j][0]) / float(points[i][0] - points[j][0])
      res += tmp
    except:
      pass

  return int(res)




def interpol(points):

  result = []
  lagrange_compute = functools.partial(lagrange, points)

  for i in xrange(0, SCREEN_WIDTH, 2):
    result.append((i, lagrange_compute(i)))

  return result


def main():

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  running = 1

  points = []


  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = 0
      elif event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        points.append((x, y))
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        running = 0

    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (100, 0, 0), (0, SCREEN_HEIGHT / 2), (SCREEN_WIDTH, SCREEN_HEIGHT / 2), 1)
    pygame.draw.line(screen, (100, 0, 0), (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT), 1)
    if len(points) > 1:
      pygame.draw.lines(screen, (0, 255, 0), False, interpol(points), 1)
    pygame.display.flip()


if __name__ == '__main__':
  main()