import unittest
from snake_game import snake_game

class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        self.game = snake_game()

    def test_check_direction(self):
        self.assertEqual(self.game.check_direction('UP', 'DOWN'), 'UP')
        self.assertEqual(self.game.check_direction('DOWN', 'UP'), 'DOWN')

    def test_move_snake(self):
        self.game.snake_position = [100, 50]
        self.game.direction = 'RIGHT'
        self.assertEqual(self.game.move_snake(self.game.direction, self.game.snake_position), [110, 50])

    def test_check_fruit_collision(self):
        self.game.snake_position = [100, 50]
        self.game.fruit_position = [100, 50]
        self.assertTrue(self.game.check_fruit_collision(self.game.snake_position, self.game.fruit_position))

    def test_change_snake_body(self):
        self.game.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.game.change_snake_body(1)
        self.assertEqual(len(self.game.snake_body), 5)

    def test_spawn_fruit(self):
        self.game.spawn_fruit()
        self.assertNotEqual(self.game.fruit_position, [0, 0])

if __name__ == '__main__':
    unittest.main()