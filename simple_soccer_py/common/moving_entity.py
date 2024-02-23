import math
from pathlib import Path

from .c2d_matrix import C2DMatrix
from .telegram import Telegram
from .utils import clamp
from .vector2d import Vector2D


class BaseGameEntity:
    """
    一个定义了 id，类型，位置，包围半径和缩放比例的实体
    """

    def __init__(self, id: int) -> None:
        # each entity has a unique ID
        self._id = id
        # every entity has a type associated with it (health, troll, ammo etc)
        self._type = 0
        # this is a generic flag.
        self._tag = False

        # its location in the environment
        self._position = Vector2D()
        self._scale = Vector2D(1, 1)

        self._bounding_radius = 0.0

    def update(self) -> None:
        ...

    def render(self) -> None:
        ...

    def handle_message(self, msg: Telegram) -> bool:
        return False

    # entities should be able to read/write their data to a stream
    def write(self, path: Path) -> None:
        ...

    def read(self, path: Path) -> None:
        ...

    @property
    def position(self) -> Vector2D:
        return self._position

    @position.setter
    def position(self, new_pos: Vector2D) -> None:
        self._position = new_pos

    @property
    def bounding_radius(self) -> float:
        return self._bounding_radius

    @bounding_radius.setter
    def bounding_radius(self, new_radius: float) -> None:
        self._bounding_radius = new_radius

    @property
    def id(self) -> int:
        return self._id

    def is_tagged(self) -> bool:
        return self._tag

    def tag(self) -> None:
        self._tag = True

    def untag(self) -> None:
        self._tag = False

    @property
    def scale(self) -> Vector2D:
        return self._scale

    @scale.setter
    def scale(self, new_scale: Vector2D) -> None:
        self._bounding_radius *= max(new_scale.x, new_scale.y) / max(
            self._scale.x, self._scale.y
        )
        self._scale = new_scale

    @property
    def type(self) -> int:
        return self._type

    @type.setter
    def type(self, new_type: int) -> None:
        self._type = new_type


class MovingEntity(BaseGameEntity):
    def __init__(
        self,
        id: int,
        position: Vector2D,
        radius: float,
        velocity: Vector2D,
        max_speed: float,
        heading: Vector2D,
        mass: float,
        scale: Vector2D,
        turn_rate: float,
        max_force: float,
    ) -> None:
        super().__init__(id)
        self._velocity = velocity
        # a normalized vector pointing in the direction the entity is heading.
        self._heading = heading
        # a vector perpendicular to the heading vector
        self._side = heading.perp()
        self._mass = mass
        # the maximum speed this entity may travel at.
        self._max_speed = max_speed
        # the maximum force this entity can produce to power itself
        # (think rockets and thrust)
        self._max_force = max_force
        # the maximum rate (radians per second)this vehicle can rotate
        self._max_turn_rate = turn_rate

        self._position = position
        self._bounding_radius = radius
        self._scale = scale

    @property
    def velocity(self) -> Vector2D:
        return self._velocity

    @velocity.setter
    def velocity(self, new_vel: Vector2D) -> None:
        self._velocity = new_vel

    @property
    def mass(self) -> float:
        return self._mass

    @property
    def side(self) -> Vector2D:
        return self._side

    @side.setter
    def side(self, new_side: Vector2D) -> None:
        self._side = new_side

    @property
    def max_speed(self) -> float:
        return self._max_speed

    @max_speed.setter
    def max_speed(self, new_speed: float) -> None:
        self._max_speed = new_speed

    @property
    def max_force(self) -> float:
        return self._max_force

    @max_force.setter
    def max_force(self, mf: float) -> None:
        self._max_force = mf

    @property
    def is_speed_maxed_out(self) -> bool:
        return self.max_speed * self.max_speed >= self.velocity.length_sq()

    @property
    def speed(self) -> float:
        return self.velocity.length()

    @property
    def speed_sq(self) -> float:
        return self.velocity.length_sq()

    @property
    def heading(self) -> Vector2D:
        return self._heading

    @heading.setter
    def heading(self, new_heading: Vector2D) -> None:
        assert (new_heading.length_sq() - 1.0) < 0.00001
        self._heading = new_heading
        # the side vector must always be perpendicular to the heading
        self._side = self._heading.perp()

    def rotate_heading_to_face_position(self, target: Vector2D) -> bool:
        """
        given a target position, this method rotates the entity's heading
        and side vectors by an amount not greater than m_dMaxTurnRate
        until it directly faces the target.

        returns true when the heading is facing in the desired direction
        """
        to_target = target - self.position
        to_target.normalize()
        dot = self.heading.dot(to_target)

        # some compilers lose acurracy
        # so the value is clamped to ensure it remains valid for the acos
        dot = clamp(dot, -1, 1)

        # first determine the angle between the heading vector and the target
        angle = math.acos(dot)

        # return true if the player is facing the target
        if angle < 0.00001:
            return True

        # clamp the amount to turn to the max turn rate
        if angle > self.max_turn_rate:
            angle = self.max_turn_rate

        # The next few lines use a rotation matrix
        # to rotate the player's heading vector accordingly
        rotation_matrix = C2DMatrix()

        # notice how the direction of rotation has to be determined
        # when creating the rotation matrix
        rotation_matrix.rotate_by_angle(angle * self.heading.sign(to_target))
        rotation_matrix.transform_vector2ds(self.heading)
        rotation_matrix.transform_vector2ds(self.velocity)

        # finally recreate m_vSide
        self.side = self.heading.perp()

        return False

    @property
    def max_turn_rate(self) -> float:
        return self._max_turn_rate

    @max_turn_rate.setter
    def max_turn_rate(self, val: float) -> None:
        self._max_turn_rate = val
