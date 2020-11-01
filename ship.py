class Ship:
    SHIP_RADIUS = 1
    START_LIVES = 3

    def __init__(self, x, y, v_x, v_y, deg):
        """
        A constructor for a Ship object
        :param x: A int representing the ship's location on the axis x
        :param y: A int representing the ship's location on the axis y
        :param v_x: A float representing the ship's speed on the axis x
        :param v_y: A float representing the ship's speed on the axis y
        :param deg: a float representing the ship's angle in degrease
        """
        self.__x = x
        self.__y = y
        self.__v_x = v_x
        self.__v_y = v_y
        self.__deg = deg
        self.__radius = self.SHIP_RADIUS
        self.__lives = self.START_LIVES

    def get_x(self):
        """A function that returns the x coordinate of this ship"""
        return self.__x

    def get_y(self):
        """A function that returns the y coordinate of this ship"""
        return self.__y

    def get_v_x(self):
        """A function that returns the speed of the ship on the axis x"""
        return self.__v_x

    def get_v_y(self):
        """A function that returns the speed of the ship on the axis y"""
        return self.__v_y

    def get_deg(self):
        """A function that returns the ship's angle in degrease"""
        return self.__deg

    def get_radius(self):
        """A function that returns the ship's radius"""
        return self.__radius

    def get_lives(self):
        """A function that returns the ship's remaining life"""
        return self.__lives

    def set_x(self, x):
        """A function that receives a new x coordinate and sets the x coordinate of
        the ship to the new one"""
        self.__x = x

    def set_y(self, y):
        """A function that receives a new y coordinate and sets the y coordinate of
        the ship to the new one"""
        self.__y = y

    def set_v_x(self, v_x):
        """A function that sets the ship's speed on the axis x to the received
        parameter v_x"""
        self.__v_x = v_x

    def set_v_y(self, v_y):
        """A function that sets the ship's speed on the axis y to the received
        parameter v_y"""
        self.__v_y = v_y

    def set_deg(self, deg):
        """A function that sets the ship's angle in degrease to the received
        parameter deg"""
        self.__deg = deg

    def set_lives_one_down(self):
        """A function that sets the ship's life count one down"""
        self.__lives -= 1
