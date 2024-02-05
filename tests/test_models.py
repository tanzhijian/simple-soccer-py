import pytest

from simple_soccer_py.models import Vector2D


class TestVector2D:
    @pytest.fixture
    def v2(self) -> Vector2D:
        return Vector2D(1, 2)

    def test_add(self, v2: Vector2D) -> None:
        assert v2 + Vector2D(3, 4) == Vector2D(4, 6)

    def test_sub(self, v2: Vector2D) -> None:
        assert v2 - Vector2D(3, 4) == Vector2D(-2, -2)

    def test_mul(self, v2: Vector2D) -> None:
        assert v2 * 2 == Vector2D(2, 4)

    def test_divide(self, v2: Vector2D) -> None:
        assert v2 / 2 == Vector2D(0.5, 1)

    def test_eq(self, v2: Vector2D) -> None:
        assert v2 == Vector2D(1, 2)

    def test_ne(self, v2: Vector2D) -> None:
        assert v2 != Vector2D(1, 1)

    def test_zero(self, v2: Vector2D) -> None:
        v2.zero()
        assert v2 == Vector2D(0, 0)

    def test_is_zero(self, v2: Vector2D) -> None:
        assert not v2.is_zero()
        v2.zero()
        assert v2.is_zero()

    def test_length_sq(self, v2: Vector2D) -> None:
        assert v2.length_sq() == 5

    def test_length(self, v2: Vector2D) -> None:
        assert v2.length() == 5**0.5

    def test_normalize(self, v2: Vector2D) -> None:
        v2.normalize()
        assert int(v2.length() * 100) == 99

    def test_dot(self, v2: Vector2D) -> None:
        assert v2.dot(Vector2D(3, 4)) == 11

    def test_sign(self, v2: Vector2D) -> None:
        assert v2.sign(Vector2D(3, 4)) == -1
        assert v2.sign(Vector2D(-3, -4)) == 1

    def test_perp(self, v2: Vector2D) -> None:
        assert v2.perp() == Vector2D(-2, 1)

    def test_truncate(self, v2: Vector2D) -> None:
        v2.truncate(1.5)
        assert v2.length() == 1.5

    def test_distance_sq(self, v2: Vector2D) -> None:
        assert v2.distance_sq(Vector2D(3, 4)) == 8

    def test_distance(self, v2: Vector2D) -> None:
        assert v2.distance(Vector2D(3, 4)) == 8**0.5

    def test_get_reverse(self, v2: Vector2D) -> None:
        assert v2.get_reverse() == Vector2D(-1, -2)

    def test_reflect(self, v2: Vector2D) -> None:
        assert v2.reflect(Vector2D(1, 0)) == Vector2D(-1, 2)
