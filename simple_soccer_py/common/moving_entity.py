from pathlib import Path

from .telegram import Telegram
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
        self._scale = Vector2D()

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
    def __init__(self, id: int) -> None:
        super().__init__(id)
        self.velocity = Vector2D()
        # a normalized vector pointing in the direction the entity is heading.
        self.heading = Vector2D()
        # a vector perpendicular to the heading vector
        self.side = Vector2D()
        self.mass = Vector2D()
        # the maximum speed this entity may travel at.
        self.max_speed = 0.0
        # the maximum force this entity can produce to power itself
        # (think rockets and thrust)
        self.max_force = 0.0
        # the maximum rate (radians per second)this vehicle can rotate
        self.max_turn_rate = 0.0
