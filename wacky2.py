import pygame

pygame.init()

window = pygame.display.set_mode((950, 600))
running = True

radius = 200
coords = (100, 100)
y = 25
y_change = 0
y_dir = 0
x = 0
x_change = 0
x_dir = 0

while running:

	# window.fill((0, 0, 0, 250))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()


	pygame.draw.circle(window, (((coords[0] + x) / 3.1, (coords[1] + y) / 2.3, 205)), (coords[0] + x, coords[1] + y), 2)
	x += x_change
	y += y_change

	if x < radius + 120:
		x_dir = 0
	elif x > -radius:
		x_dir = 1

	if x_dir == 0:
		x_change += 0.0001
	elif x_dir == 1:
		x_change -= 0.0001

	if y < radius:
		y_dir = 0
	elif y > -radius:
		y_dir = 1

	if y_dir == 0:
		y_change += 0.0001
	elif y_dir == 1:
		y_change -= 0.0001

	pygame.display.update()
