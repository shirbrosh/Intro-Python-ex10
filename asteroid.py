class Asteroid:
    TEN = 10
    FIVE = 5

    def __init__(self, x, y, v_x, v_y, size):
        """
        A constructor for a Asteroid object
        :param x: A int representing the asteroid's location on the axis x
        :param y: A int representing the asteroid's location on the axis y
        :param v_x: A float representing the asteroid's speed on the axis x
        :param v_y: A float representing the asteroid's speed on the axis y
        :param size: a int between 1-3 representing the asteroid's size
        """
        self.__x = x
        self.__y = y
        self.__v_x = v_x
        self.__v_y = v_y
        self.__size = size
        self.__radius = size*self.TEN-self.FIVE

    def get_x(self):
        """A function that returns the x coordinate of this asteroid"""
        return self.__x

    def get_y(self):
        """A function that returns the y coordinate of this asteroid"""
        return self.__y

    def get_v_x(self):
        """A function that returns the speed of the asteroid on the axis x"""
        return self.__v_x

    def get_v_y(self):
        """A function that returns the speed of the asteroid on the axis y"""
        return self.__v_y

    def get_size(self):
        """A function that returns the size of this asteroid"""
        return self.__size

    def set_x(self, x):
        """A function that receives a new x coordinate and sets the x coordinate of
        the asteroid to the new one"""
        self.__x = x

    def set_y(self, y):
        """A function that receives a new y coordinate and sets the y coordinate of
        the asteroid to the new one"""
        self.__y = y

    def get_radius(self):
        """A function that returns this asteroid's radius"""
        return self.__radius

    def has_intersect(self, obj):
        """A function that returns True whether an object has intersect with this
        asteroid and False otherwise"""
        distance = ((obj.get_x()-self.__x)**2+(obj.get_y()-self.__y)**2)**0.5
        if distance <= self.__radius + obj.get_radius():
            return True
        return False
