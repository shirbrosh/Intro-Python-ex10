from screen import Screen
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
import sys
import random
import math

DEFAULT_ASTEROIDS_NUM = 5


class GameRunner:
    MOVE_DEG = 7
    STRAIGHT_ANGLE = 180
    MIN_ASTEROID_SPEED = 1
    MAX_ASTEROID_SPEED = 4
    START_ASTEROID_SIZE = 3
    ZERO = 0
    ACCELERATION_FACTOR = 2
    SCORE = {3: 20, 2: 50, 1: 100}
    SIZE1 = 1
    SIZE2 = 2
    SIZE3 = 3
    CHANGE_DIRECTION = -1
    NUM_TORPEDOES_ALLOWED = 10
    MAX_TORPEDO_LIFE = 200
    END_MSG = {1: "you exploded all the asteroids, you won!",
               2: "you ran out of life, you lost :( ",
               3: "you pressed the quit button"}

    def __init__(self, asteroids_amount=DEFAULT_ASTEROIDS_NUM):
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__ship = self.create_ship()
        self.__asteroid_lst = []
        self.create_asteroid(asteroids_amount)
        self.__torpedo_dict = {}
        self.__score = self.ZERO

    def create_ship(self):
        """A function that creates the ship object in the game"""
        start_ship_loc_x = random.randrange(self.__screen_min_x,
                                            self.__screen_max_x)
        start_ship_loc_y = random.randrange(self.__screen_min_y,
                                            self.__screen_max_y)
        v_x_ship = self.ZERO
        v_y_ship = self.ZERO
        deg = self.ZERO
        ship = Ship(start_ship_loc_x, start_ship_loc_y,
                    v_x_ship, v_y_ship, deg)
        self.__screen.draw_ship(start_ship_loc_x, start_ship_loc_y,
                                deg)
        return ship

    def create_asteroid(self, asteroids_amount):
        """A function that creates the asteroids objects in the game"""
        asteroid_size = self.START_ASTEROID_SIZE
        for i in range(0, asteroids_amount):
            start_asteroid_loc_x = random.randrange(self.__screen_min_x,
                                                    self.__screen_max_x)
            start_asteroid_loc_y = random.randrange(self.__screen_min_y,
                                                    self.__screen_max_y)
            v_x_asteroid = random.randrange(self.MIN_ASTEROID_SPEED,
                                            self.MAX_ASTEROID_SPEED)
            v_y_asteroid = random.randrange(self.MIN_ASTEROID_SPEED,
                                            self.MAX_ASTEROID_SPEED)
            asteroid_to_add = Asteroid(start_asteroid_loc_x,
                                       start_asteroid_loc_y,
                                       v_x_asteroid,
                                       v_y_asteroid, asteroid_size)
            self.__screen.register_asteroid(asteroid_to_add, asteroid_size)
            self.__screen.draw_asteroid(asteroid_to_add, start_asteroid_loc_x,
                                        start_asteroid_loc_y)
            self.__asteroid_lst.append(asteroid_to_add)

    def move_ship(self, delta_x, delta_y):
        """A function that moves a Ship object"""
        v_x = self.__ship.get_v_x()
        v_y = self.__ship.get_v_y()
        x = self.__ship.get_x()
        y = self.__ship.get_y()
        newcord_x = ((v_x + x - self.__screen.SCREEN_MIN_X) % delta_x) + \
                    self.__screen.SCREEN_MIN_X
        newcord_y = ((v_y + y - self.__screen.SCREEN_MIN_Y) % delta_y) + \
                    self.__screen.SCREEN_MIN_Y
        self.__ship.set_x(newcord_x)
        self.__ship.set_y(newcord_y)

    def move_asteroid(self, delta_x, delta_y):
        """A function that moves an Asteroid object"""
        for ast in self.__asteroid_lst:
            v_x = ast.get_v_x()
            v_y = ast.get_v_y()
            x = ast.get_x()
            y = ast.get_y()
            newcord_x = ((v_x + x - self.__screen.SCREEN_MIN_X) % delta_x) + \
                        self.__screen.SCREEN_MIN_X
            newcord_y = ((v_y + y - self.__screen.SCREEN_MIN_Y) % delta_y) + \
                        self.__screen.SCREEN_MIN_Y
            ast.set_x(newcord_x)
            ast.set_y(newcord_y)

    def move_torpedo(self, delta_x, delta_y):
        """A function that moves a torpedo object"""
        for tor in self.__torpedo_dict.keys():
            self.__torpedo_dict[tor] += 1  # change the torpedo lifetime
            v_x = tor.get_v_x()
            v_y = tor.get_v_y()
            x = tor.get_x()
            y = tor.get_y()
            newcord_x = ((v_x + x - self.__screen.SCREEN_MIN_X) % delta_x) + \
                        self.__screen.SCREEN_MIN_X
            newcord_y = ((v_y + y - self.__screen.SCREEN_MIN_Y) % delta_y) + \
                        self.__screen.SCREEN_MIN_Y
            tor.set_x(newcord_x)
            tor.set_y(newcord_y)
            self.__screen.draw_torpedo(tor, newcord_x, newcord_y, tor.get_deg())
            if self.__torpedo_dict[tor] >= self.MAX_TORPEDO_LIFE:
                self.remove_torpedo(tor)
                self.__screen.unregister_torpedo(tor)

    def move_object(self):
        """A function that calculate the parameter 'delta' in the move objects
        calculation and calls the functions 'move_ship' and 'move_asteroid' """
        delta_x = self.__screen_max_x - self.__screen_min_x
        delta_y = self.__screen_max_y - self.__screen_min_y
        self.move_ship(delta_x, delta_y)
        self.move_asteroid(delta_x, delta_y)
        self.move_torpedo(delta_x, delta_y)

    def change_deg_right(self):
        """A function that changes the angle of a ship object to the right"""
        current_deg = self.__ship.get_deg()
        after_move_deg = current_deg - self.MOVE_DEG
        self.__ship.set_deg(after_move_deg)

    def change_deg_left(self):
        """A function that changes the angle of a ship object to the left"""
        current_deg = self.__ship.get_deg()
        after_move_deg = current_deg + self.MOVE_DEG
        self.__ship.set_deg(after_move_deg)

    def rad_trans(self, deg):
        """A function that receives an angle in degrease and transfer it to radians"""
        return (deg * math.pi) / self.STRAIGHT_ANGLE

    def speed_up(self):
        """A function that changes the speed of a Ship object"""
        v_x = self.__ship.get_v_x()
        v_y = self.__ship.get_v_y()
        deg = self.__ship.get_deg()
        new_speed_x = v_x + math.cos(self.rad_trans(deg))
        new_speed_y = v_y + math.sin(self.rad_trans(deg))
        self.__ship.set_v_x(new_speed_x)
        self.__ship.set_v_y(new_speed_y)

    def after_intersection_ship_ast(self):
        """A function that updates the game if a ship intersected an asteroid"""
        for ast in self.__asteroid_lst:
            if ast.has_intersect(self.__ship):
                self.__screen.show_message("Crush",
                                           "you have crushed into an asteroid")
                self.__ship.set_lives_one_down()
                self.__screen.remove_life()
                self.remove_asteroid(ast)
                self.__screen.unregister_asteroid(ast)

    def after_intersection_tor_ast(self):
        """A function that updates the game if a torpedo intersected an asteroid"""
        for tor in self.__torpedo_dict.keys():
            for ast in self.__asteroid_lst:
                if ast.has_intersect(tor):
                    self.score(ast)
                    self.splitting_asteroid(tor, ast)
                    self.remove_torpedo(tor)
                    self.__screen.unregister_torpedo(tor)

    def calculate_new_speed_for_split(self, torpedo, asteroid):
        """A function that calculates the speed for an asteroid after a split"""
        new_speed_x = (torpedo.get_v_x() + asteroid.get_v_x()) / (
                ((asteroid.get_v_x() ** 2) + (asteroid.get_v_y() ** 2)) ** 0.5)
        new_speed_y = (torpedo.get_v_y() + asteroid.get_v_y()) / (
                ((asteroid.get_v_x() ** 2) + (asteroid.get_v_y() ** 2)) ** 0.5)
        return new_speed_x, new_speed_y

    def splitting_asteroid(self, torpedo, asteroid):
        """A function that creates new asteroids after an intersect with a torpedo"""
        if asteroid.get_size() == self.SIZE3:
            new_size = self.SIZE2
        elif asteroid.get_size() == self.SIZE2:
            new_size = self.SIZE1
        elif asteroid.get_size() == self.SIZE1:
            self.remove_asteroid(asteroid)
            self.__screen.unregister_asteroid(asteroid)
            return
        new_speed_x1, new_speed_y1 = self.calculate_new_speed_for_split(torpedo,
                                                                        asteroid)
        new_speed_x2 = new_speed_x1 * self.CHANGE_DIRECTION
        new_speed_y2 = new_speed_y1 * self.CHANGE_DIRECTION
        asteroid1 = Asteroid(asteroid.get_x(), asteroid.get_y(), new_speed_x1,
                             new_speed_y1, new_size)
        asteroid2 = Asteroid(asteroid.get_x(), asteroid.get_y(), new_speed_x2,
                             new_speed_y2, new_size)
        self.__screen.register_asteroid(asteroid1, new_size)
        self.__screen.register_asteroid(asteroid2, new_size)
        self.__screen.draw_asteroid(asteroid1, asteroid.get_x(), asteroid.get_y())
        self.__screen.draw_asteroid(asteroid2, asteroid.get_x(), asteroid.get_y())
        self.__asteroid_lst.append(asteroid1)
        self.__asteroid_lst.append(asteroid2)
        self.remove_asteroid(asteroid)
        self.__screen.unregister_asteroid(asteroid)

    def remove_asteroid(self, ast_to_remove):
        """A function that removes an asteroid object from the game"""
        new_ast_lst = []
        for ast in self.__asteroid_lst:
            if id(ast) != id(ast_to_remove):
                new_ast_lst.append(ast)
        self.__asteroid_lst = new_ast_lst

    def remove_torpedo(self, tor_to_remove):
        """A function that removes a torpedo object from the game"""
        new_tor_dict = {}
        for tor in self.__torpedo_dict.keys():
            if id(tor) != id(tor_to_remove):
                new_tor_dict[tor] = self.__torpedo_dict[tor]
        self.__torpedo_dict = new_tor_dict

    def shoot(self):
        """A function that operates the shoot of the torpedo"""
        if len(self.__torpedo_dict) == self.NUM_TORPEDOES_ALLOWED:
            return
        x_tor = self.__ship.get_x()
        y_tor = self.__ship.get_y()
        deg_tor = self.__ship.get_deg()
        current_speed_x = self.__ship.get_v_x()
        current_speed_y = self.__ship.get_v_y()
        new_speed_x = current_speed_x + self.ACCELERATION_FACTOR * math.cos(
            self.rad_trans(deg_tor))
        new_speed_y = current_speed_y + self.ACCELERATION_FACTOR * math.sin(
            self.rad_trans(deg_tor))
        new_torpedo = Torpedo(x_tor, y_tor, new_speed_x, new_speed_y, deg_tor)
        self.__screen.register_torpedo(new_torpedo)
        self.__screen.draw_torpedo(new_torpedo, x_tor, y_tor, deg_tor)
        # set the lifetime of a new torpedo on 0:
        self.__torpedo_dict[new_torpedo] = self.ZERO

    def set_score(self, score):
        """A function that sets the game's score to the received parameter score"""
        self.__score = score

    def score(self, asteroid):
        """A function that calculates the new score and sets it using the function
        'set_score'"""
        new_score = self.__score + self.SCORE[asteroid.get_size()]
        self.set_score(new_score)
        self.__screen.set_score(new_score)

    def end_game(self):
        """A function that determines whether the game has ended and prints a
        suitable massage"""
        check_if_needs_to_end = self.ZERO
        if len(self.__asteroid_lst) == self.ZERO:
            print(self.END_MSG[1])
            check_if_needs_to_end = self.SIZE1  # i used this constant just to apply a number different than 0
        elif self.__ship.get_lives() == self.ZERO:
            print(self.END_MSG[2])
            check_if_needs_to_end = self.SIZE1
        elif self.__screen.should_end():
            print(self.END_MSG[3])
            check_if_needs_to_end = self.SIZE1
        if check_if_needs_to_end != self.ZERO:
            self.__screen.end_game()
            sys.exit()

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def call_for_draw_ship(self):
        """A function that calls for the draw ship function, just to make the
        functions- 'which_move' and '_game_loop' shorter"""
        self.__screen.draw_ship(self.__ship.get_x(), self.__ship.get_y(),
                                self.__ship.get_deg())

    def teleport(self):
        """A function that teleports the ship to a random location on the board"""
        new_ship_loc_x = random.randrange(self.__screen_min_x,
                                          self.__screen_max_x)
        new_ship_loc_y = random.randrange(self.__screen_min_y,
                                          self.__screen_max_y)
        teleported_ship = Ship(new_ship_loc_x, new_ship_loc_y, self.__ship.get_v_x(),
                               self.__ship.get_v_y(), self.__ship.get_deg())
        for ast in self.__asteroid_lst:
            while ast.has_intersect(teleported_ship):
                new_ship_loc_x = random.randrange(self.__screen_min_x,
                                                  self.__screen_max_x)
                new_ship_loc_y = random.randrange(self.__screen_min_y,
                                                  self.__screen_max_y)
                teleported_ship = Ship(new_ship_loc_x, new_ship_loc_y,
                                       self.__ship.get_v_x(), self.__ship.get_v_y(),
                                       self.__ship.get_deg())
        self.__ship = teleported_ship
        self.__screen.draw_ship(new_ship_loc_x, new_ship_loc_y,
                                self.__ship.get_deg())

    def which_move(self):
        """A function that checks which key the player is pressing and activates the
        suitable changing function"""
        if self.__screen.is_right_pressed():
            self.change_deg_right()
            self.call_for_draw_ship()
        if self.__screen.is_left_pressed():
            self.change_deg_left()
            self.call_for_draw_ship()
        if self.__screen.is_up_pressed():
            self.speed_up()
            self.call_for_draw_ship()
        if self.__screen.is_space_pressed():
            self.shoot()
        if self.__screen.is_teleport_pressed():
            self.teleport()

    def _game_loop(self):
        """A function that runs the game"""
        for ast in self.__asteroid_lst:
            self.__screen.draw_asteroid(ast, ast.get_x(), ast.get_y())
        self.which_move()
        self.move_object()
        self.call_for_draw_ship()
        self.after_intersection_ship_ast()
        self.after_intersection_tor_ast()
        self.end_game()


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
