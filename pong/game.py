class Game:
    def __init__(self):
        self.width_screen = 800
        self.height_screen = 600
        self.__ball_position = (0, 0)
        self.__ball_delta_x = 1
        self.__ball_delta_y = 1

        self.paddle_left_position = (-self.width_screen / 2 + 50, 0)
        self.paddle_right_position = (self.width_screen / 2 - 50, 0)
        self.paddle_height = self.height_screen * 0.2
        self.paddle_width = 20

        self.left_player_points = 0
        self.right_player_points = 0

    def tick(self):
        self.__border_checker()
        self.__hit_cheker()
        x, y = self.__ball_position
        self.__ball_position = (x + self.__ball_delta_x, y + self.__ball_delta_y)

    def __border_checker(self):
        x, y = self.__ball_position
        if abs(y) >= (self.height_screen / 2):
            self.__ball_delta_y *= -1
        if x >= (self.width_screen / 2):
            self.left_player_points += 1
            self.__ball_position = (0, 0)
        if x <= -(self.width_screen / 2):
            self.right_player_points += 1
            self.__ball_position = (0, 0)
    def __hit_cheker(self):
        x, y = self.__ball_position
        left_x, left_y = self.paddle_left_position
        right_x, right_y = self.paddle_right_position
        hit_left_paddle = left_x + self.paddle_width / 2 == x and \
                          ((left_y - self.paddle_height / 2) <= y <= (left_y + self.paddle_height / 2))
        hit_right_paddle = right_x - self.paddle_width / 2 == x and \
                           ((right_y - self.paddle_height / 2) <= y <= (right_y + self.paddle_height / 2))
        if hit_left_paddle or hit_right_paddle:
            self.__ball_delta_x *= -1

    def ball_pos(self):
        return self.__ball_position

    def left_paddle_up(self):
        x, y = self.paddle_left_position
        if abs((y + self.paddle_height / 2) + 20) <= self.height_screen / 2:
            self.paddle_left_position = (x, y + 20)

    def left_paddle_down(self):
        x, y = self.paddle_left_position
        if abs((y - self.paddle_height / 2) - 20) <= self.height_screen / 2:
            self.paddle_left_position = (x, y - 20)

    def right_paddle_up(self):
        x, y = self.paddle_right_position
        if abs((y + self.paddle_height / 2) + 20) <= self.height_screen / 2:
            self.paddle_right_position = (x, y + 20)

    def right_paddle_down(self):
        x, y = self.paddle_right_position
        if abs((y - self.paddle_height / 2) - 20) <= self.height_screen / 2:
            self.paddle_right_position = (x, y - 20)
