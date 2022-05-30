import pygame

pygame.init()

window = pygame.display.set_mode((950, 950))
running = True

radius_x = 2
radius_y = 0.7
coords = (475, 475)
y = 0
y_change = 1
y_dir = 0
x = 0
x_change = 0
x_dir = 0


count = 1
while running:

	if count == 255:
		counting = -1
	elif count == 1:
		counting = 1

	count += counting
	# window.fill((0, 0, 0, 250))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()


	pygame.draw.circle(window, ((100, count, count)), (coords[0] + x, coords[1] + y), 2)
	x += x_change
	y += y_change

	if x_change + x > radius_x:
		x_dir = 0
	elif x_change + x < -radius_x:
		x_dir = 1

	if x_dir == 0:
		x_change -= 0.005
	elif x_dir == 1:
		x_change += 0.005

	if y_change + y > radius_y:
		y_dir = 0
	elif y_change + y < -radius_y:
		y_dir = 1

	if y_dir == 0:
		y_change -= 0.0015
	elif y_dir == 1:
		y_change += 0.0015

	pygame.display.update()
