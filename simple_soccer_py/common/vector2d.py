import math


class Vector2D:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector2D":
        return Vector2D(self.x * scalar, self.y * scalar)

    def __floatdiv__(self, scalar: float) -> "Vector2D":
        return Vector2D(self.x / scalar, self.y / scalar)

    def __truediv__(self, scalar: float) -> "Vector2D":
        return self.__floatdiv__(scalar)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return (self.x != other.x) or (self.y != other.y)

    def zero(self) -> None:
        """sets x and y to zero"""
        self.x = 0
        self.y = 0

    def is_zero(self) -> bool:
        """returns true if both x and y are zero"""
        return (self.x**2 + self.y**2) < 0.000001

    def length_sq(self) -> float:
        """
        returns the squared length of the vector (thereby avoiding the sqrt)
        """
        return self.x**2 + self.y**2

    def length(self) -> float:
        """returns the length of the vector"""
        return math.sqrt(self.length_sq())

    def normalize(self) -> None:
        """normalizes a 2D Vector"""
        if (length := self.length()) > 0:
            self.x /= length
            self.y /= length

    def dot(self, v2: "Vector2D") -> float:
        """returns the dot product of this vector and v2"""
        return self.x * v2.x + self.y * v2.y

    def sign(self, v2: "Vector2D") -> int:
        """
        returns positive if v2 is clockwise of this vector,
        negative if anticlockwise (assuming the Y axis is pointing down,
        X axis to right like a Window app)
        """
        if self.y * v2.x > self.x * v2.y:
            return -1
        else:
            return 1

    def perp(self) -> "Vector2D":
        """returns the vector that is perpendicular to this one."""
        return Vector2D(-self.y, self.x)

    def truncate(self, max: float) -> None:
        """
        adjusts x and y so that the length of the vector does not exceed max
        """
        if self.length() > max:
            self.normalize()
            self.x *= max
            self.y *= max

    def distance_sq(self, v2: "Vector2D") -> float:
        """
        squared version of distance.
        """
        return (v2.x - self.x) ** 2 + (v2.y - self.y) ** 2

    def distance(self, v2: "Vector2D") -> float:
        """
        returns the distance between this vector and th one passed as a parameter
        """
        return math.sqrt(self.distance_sq(v2))

    def get_reverse(self) -> "Vector2D":
        """returns the vector that is the reverse of this vector"""
        return Vector2D(-self.x, -self.y)

    def reflect(self, norm: "Vector2D") -> "Vector2D":
        """
        given a normalized vector this method reflects the vector it is operating upon.
        (like the path of a ball bouncing off a wall)
        """
        return self + norm.get_reverse() * 2.0 * self.dot(norm)
