"""
Original Snake Game code from GeeksforGeeks
Original Code: https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/
Original Author: amnindersingh1414
"""

# importing libraries
import pygame
import time
import random

class snake_game():
	def __init__(self):
		self.snake_speed = 15
		self.window_x = 720
		self.window_y = 480
		self.black = pygame.Color(0, 0, 0)
		self.white = pygame.Color(255, 255, 255)
		self.red = pygame.Color(255, 0, 0)
		self.green = pygame.Color(0, 255, 0)
		self.blue = pygame.Color(0, 0, 255)
		self.snake_position = [100, 50]
		self.snake_body = [
			[100, 50],
			[90, 50],
			[80, 50],
			[70, 50]
		]
		self.fruit_position = [random.randrange(1, (self.window_x//10)) * 10, random.randrange(1, (self.window_y//10)) * 10]
		self.direction = 'RIGHT'
		self.change_to = self.direction
		self.score = 0
		self.game_window = pygame.display.set_mode((self.window_x, self.window_y))
		self.fps = pygame.time.Clock()
		pygame.init()
		pygame.display.set_caption('GeeksforGeeks Snakes')
		self.game_window = pygame.display.set_mode((self.window_x, self.window_y))
		self.fps = pygame.time.Clock()
		self.direction = 'RIGHT'
		self.change_to = self.direction
		self.score = 0

	def show_score(self, choice, color, font, size):
		score_font = pygame.font.SysFont(font, size)
		score_surface = score_font.render('Score : ' + str(self.score), True, color)
		score_rect = score_surface.get_rect()
		self.game_window.blit(score_surface, score_rect)

	def game_over(self):
		my_font = pygame.font.SysFont('times new roman', 50)
		game_over_surface = my_font.render('Your Score is : ' + str(self.score), True, self.red)
		game_over_rect = game_over_surface.get_rect()
		game_over_rect.midtop = (self.window_x/2, self.window_y/4)
		self.game_window.blit(game_over_surface, game_over_rect)
		pygame.display.flip()
		time.sleep(2)
		pygame.quit()
		quit()

	def check_direction(self, direction, change_to):
		if change_to == 'UP' and direction != 'DOWN':
			direction = 'UP'
		if change_to == 'DOWN' and direction != 'UP':
			direction = 'DOWN'
		if change_to == 'LEFT' and direction != 'RIGHT':
			direction = 'LEFT'
		if change_to == 'RIGHT' and direction != 'LEFT':
			direction = 'RIGHT'
		return direction


	def move_snake(self, direction, snake_position):

		if direction == 'UP':
			snake_position[1] -= 10
		elif direction == 'DOWN':
			snake_position[1] += 10
		elif direction == 'LEFT':
			snake_position[0] -= 10
		elif direction == 'RIGHT':
			snake_position[0] += 10

		self.snake_body.insert(0, list(self.snake_position))
		self.snake_body.pop()
		return snake_position

	def check_game_over_states(self, snake_position):
     
		if snake_position[0] < 0 or snake_position[0] > self.window_x-10:
			self.game_over()
		if snake_position[1] < 0 or snake_position[1] > self.window_y-10:
			self.game_over()
   
		for block in self.snake_body[1:]:
			if snake_position[0] == block[0] and snake_position[1] == block[1]:
				print(f"Body: {self.snake_body}, Position:{self.snake_position}, Block:{block}")
				self.game_over()

	def game_draw(self):
		# Draw background color
		self.game_window.fill(self.black)
  
		# Draw snake
		for pos in self.snake_body:
			if pos != [0,0]:
				pygame.draw.rect(self.game_window, self.green, pygame.Rect(pos[0], pos[1], 10, 10))

		# Draw fruit
		pygame.draw.rect(self.game_window, self.red, pygame.Rect(self.fruit_position[0], self.fruit_position[1], 10, 10))
  
		# Draw score
		self.show_score(1, self.white, 'times new roman', 20)
  
	def check_events(self):
		event_list = pygame.event.get()
		for event in event_list:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.change_to = 'UP'
				if event.key == pygame.K_DOWN:
					self.change_to = 'DOWN'
				if event.key == pygame.K_LEFT:
					self.change_to = 'LEFT'
				if event.key == pygame.K_RIGHT:
					self.change_to = 'RIGHT'
	
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

	def check_fruit_collision(self, snake_position, fruit_position):
		if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
			return True
		else:
			return False

	def change_snake_body(self, change):
		if change >= 1:
			for i in range(change):
				self.snake_body.append([0,0])
		elif change <= -1:
			for i in range(abs(change)):
				if len(self.snake_body) > 1:
					self.snake_body.pop()

	def spawn_fruit(self):
		while True:
			self.fruit_position = [random.randrange(1, (self.window_x//10)) * 10, random.randrange(1, (self.window_y//10)) * 10]
			if self.fruit_position not in self.snake_body:
				break

	def start_game_loop(self):
     
		while True:
			self.check_events()
			self.direction = self.check_direction(self.direction, self.change_to)
			self.snake_position = self.move_snake(self.direction, self.snake_position)
			
   
			if self.check_fruit_collision(self.snake_position, self.fruit_position):
				self.score += 1
				self.spawn_fruit()
				self.change_snake_body(1)
    
			
			self.game_draw()
			
			pygame.display.update()
			self.check_game_over_states(self.snake_position)
			self.fps.tick(self.snake_speed)

if __name__ == '__main__':
	game = snake_game()
	game.start_game_loop()
