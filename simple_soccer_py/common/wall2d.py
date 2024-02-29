from .vector2d import Vector2D


class Wall2D:
    """
    class to create and render 2D walls.
    Defined as the two vectors A - B with a perpendicular normal.
    """

    def __init__(
        self,
        A: Vector2D,
        B: Vector2D,
        N: Vector2D | None = None,
    ) -> None:
        self._v_A = A
        self._v_B = B

        # 可以优化
        if N is None:
            self._calculate_normal()
        else:
            self._v_N = N

    def _calculate_normal(self) -> None:
        temp = self._v_B - self._v_A
        temp.normalize()
        self._v_N = Vector2D(x=-temp.y, y=temp.x)

    @property
    def from_(self) -> Vector2D:
        return self._v_A

    @from_.setter
    def from_(self, new_A: Vector2D) -> None:
        self._v_A = new_A
        self._calculate_normal()

    @property
    def to(self) -> Vector2D:
        return self._v_B

    @to.setter
    def to(self, new_B: Vector2D) -> None:
        self._v_B = new_B
        self._calculate_normal()

    @property
    def normal(self) -> Vector2D:
        return self._v_N

    @normal.setter
    def normal(self, new_N: Vector2D) -> None:
        self._v_N = new_N

    def center(self) -> Vector2D:
        return (self._v_A + self._v_B) / 2

    def render(self) -> None:
        ...

    def read(self) -> None:
        ...

    def write(self) -> None:
        ...
