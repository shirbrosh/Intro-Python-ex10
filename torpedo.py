class Torpedo:
    TOR_RADIUS = 4

    def __init__(self, x, y, v_x, v_y, deg):
        """
        A constructor for a Torpedo object
        :param x: A int representing the torpedo's location on the axis x
        :param y: A int representing the torpedo's location on the axis y
        :param v_x: A float representing the torpedo's speed on the axis x
        :param v_y: A float representing the torpedo's speed on the axis y
        :param deg: a float representing the torpedo's angle in degrease
        """
        self.__x = x
        self.__y = y
        self.__v_x = v_x
        self.__v_y = v_y
        self.__deg = deg
        self.__radius = self.TOR_RADIUS

    def get_x(self):
        """A function that returns the x coordinate of this torpedo"""
        return self.__x

    def get_y(self):
        """A function that returns the y coordinate of this torpedo"""
        return self.__y

    def get_v_x(self):
        """A function that returns the speed of the torpedo on the axis x"""
        return self.__v_x

    def get_v_y(self):
        """A function that returns the speed of the torpedo on the axis y"""
        return self.__v_y

    def get_deg(self):
        """A function that returns the torpedo's angle in degrease"""
        return self.__deg

    def get_radius(self):
        """A function that returns this torpedo's radius"""
        return self.__radius

    def set_x(self, x):
        """A function that receives a new x coordinate and sets the x coordinate of
        the torpedo to the new one"""
        self.__x = x

    def set_y(self, y):
        """A function that receives a new y coordinate and sets the y coordinate of
        the torpedo to the new one"""
        self.__y = y